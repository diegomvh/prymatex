#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore

from prymatex.gui import utils
from prymatex.support.processor import PMXCommandProcessor
from prymatex.support.snippet import PMXSnippet

class PMXCommandProcessor(PMXCommandProcessor):
    def __init__(self, editor):
        super(PMXCommandProcessor, self).__init__()
        self.editor = editor

    def environment(self, command):
        environment = self.editor.buildEnvironment(command.buildEnvironment())
        environment.update(self.baseEnvironment)
        return environment

    def configure(self, settings):
        self.asynchronous = settings.get("asynchronous", True)
        self.tabTriggered = settings.get("tabTriggered", False)
        self.disableIndent = settings.get("disableIndent", False)
        self.baseEnvironment = settings.get("environment", {})
        self.errorCommand = settings.get("errorCommand", False)

    def formatAsXml(self, text, firstBlock, lastBlock, startIndex, endIndex):
        result = []
        block = firstBlock
        for line in text.splitlines():
            if block == firstBlock and block == lastBlock:
                scopes = block.userData().scopeRanges(start = startIndex, end = endIndex)
            elif block == firstBlock:
                scopes = block.userData().scopeRanges(start = startIndex)
            elif block == lastBlock:
                scopes = block.userData().scopeRanges(end = endIndex)
            else:
                scopes = block.userData().scopeRanges()
            lineXML = ""
            for (start, end), scope in scopes:
                ss = scope.split()
                token = "".join(map(lambda scope: "<" + scope + ">", ss))
                token += line[start:end]
                ss.reverse()
                token += "".join(map(lambda scope: "</" + scope + ">", ss))
                lineXML += token
            result.append(lineXML)
            if block == lastBlock:
                break
            block = block.next()
        return "\n".join(result)

    #Inputs
    def document(self, format = None):
        #TODO: ver si pone los \n
        text = unicode(self.editor.document().toPlainText())
        if format == "xml":
            firstBlock = self.editor.document().firstBlock()
            lastBlock = self.editor.document().lastBlock()
            return self.formatAsXml(text, firstBlock, lastBlock, firstBlock.position(), lastBlock.position() + lastBlock.length())
        else:
            return text
        
    def line(self, format = None):
        return self.editor.textCursor().block().text()
        
    def character(self, format = None):
        cursor = self.editor.textCursor()
        return cursor.document().characterAt(cursor.position())
        
    def scope(self, format = None):
        return self.editor.getCurrentScope()
    
    def selection(self, format = None):
        cursor = self.editor.textCursor()
        if cursor.hasSelection():
            text = utils.replaceLineBreaks(cursor.selectedText())
            if format == "xml":
                firstBlock, lastBlock = self.editor.getSelectionBlockStartEnd()
                return self.formatAsXml(text, firstBlock, lastBlock, cursor.selectionStart() - firstBlock.position(), cursor.selectionEnd() - lastBlock.position())
            else:
                return text
        
    def selectedText(self, format = None):
        return self.selection
    
    def word(self, format = None):
        word, start, end = self.editor.currentWord()
        return word
    
    #beforeRunningCommand
    def saveModifiedFiles(self):
        ret = True
        for editor in self.editor.mainWindow.editors():
            if editor.isModified():
                self.editor.mainWindow.saveEditor(editor = editor)
                ret = ret and not editor.isModified()
            if ret == False:
                break
        return ret
    
    def saveActiveFile(self):
        self.editor.mainWindow.saveEditor(editor = self.editor)
        return not (self.editor.isModified() or self.editor.isNew())
    
    # deleteFromEditor
    def deleteWord(self):
        _, start, end = self.editor.currentWord()
        cursor = self.editor.textCursor()
        cursor.setPosition(start)
        cursor.setPosition(end, QtGui.QTextCursor.KeepAnchor)
        cursor.removeSelectedText()
        
    def deleteSelection(self):
        cursor = self.editor.textCursor()
        cursor.removeSelectedText()

    def deleteLine(self):
        cursor = self.editor.textCursor()
        block = cursor.block()
        cursor.setPosition(block.position())
        cursor.setPosition(block.position() + block.length() - 1, QtGui.QTextCursor.KeepAnchor)
        cursor.removeSelectedText()
        
    def deleteCharacter(self):
        cursor = self.editor.textCursor()
        cursor.deleteChar()
    
    def deleteDocument(self):
        print "borrar documento"
        self.editor.document().clear()
       
    # Outpus function
    def error(self, context):
        #TODO: Mover esto a un lugar donde no dependa del processor mostrar un error en el borwser, quiza a la mainWindow
        #para poder llamarlos como showErrorInBrowser o algo asi :)
        if self.errorCommand:
            #Prevenir la entrada recursiva
            raise Exception(context.errorValue)
        from prymatex.support.utils import makeHyperlinks
        from prymatex.utils import html
        commandScript = '''
            source "$TM_SUPPORT_PATH/lib/webpreview.sh" 
            
            html_header "An error has occurred while executing command %(name)s"
            echo -e "<pre>%(output)s</pre>"
            echo -e "<p>Exit code was: %(exitcode)d</p>"
            html_footer
        ''' % {'output': html.escape(context.errorValue),
               'name': html.escape(context.description()),
               'exitcode': context.outputType}
        command = self.editor.application.supportManager.buildAdHocCommand(commandScript, context.bundleItem.bundle,
            name = "Error runing %s" % context.description(),
            commandOutput = 'showAsHTML')
        self.editor.insertBundleItem(command, errorCommand = True)
        
    def discard(self, context):
        pass
        
    def replaceSelectedText(self, context):
        cursor = self.editor.textCursor()
        if cursor.hasSelection():
            position = cursor.selectionStart()
            cursor.insertText(context.outputValue)
            cursor.setPosition(position, position + len(context.outputValue))
        else:
            cursor.insertText(context.outputValue)
        self.editor.setTextCursor(cursor)
        
    def replaceDocument(self, context):
        #1 Recuperar la posicion actual del cursor
        position = self.editor.textCursor().position()
        currentText = self.editor.toPlainText()
        newText = context.outputValue
        #if currentText[:position] != newText[:position]:
        #    position += (len(newText) - len(currentText))
        self.editor.setPlainText(newText)
        cursor = self.editor.textCursor()
        cursor.setPosition(position)
        self.editor.setTextCursor(cursor)
        
    def insertText(self, context):
        cursor = self.editor.textCursor()
        cursor.insertText(context.outputValue)
        
    def afterSelectedText(self, context):
        cursor = self.editor.textCursor()
        position = cursor.selectionEnd()
        cursor.setPosition(position)
        cursor.insertText(context.outputValue)
        
    def insertAsSnippet(self, context):
        snippet = self.editor.application.supportManager.buildAdHocSnippet(context.outputValue, context.bundleItem.bundle, tabTrigger = context.bundleItem.tabTrigger)
        self.editor.insertBundleItem(snippet, tabTriggered = self.tabTriggered, disableIndent = self.disableIndent)
            
    def showAsHTML(self, context):
        self.editor.mainWindow.browser.setHtml(context.outputValue, context.bundleItem)

    timespanFactor = 1
    def showAsTooltip(self, context):
        # Chicho's sense of statistics
        linesToRead = context.outputValue.count('\n') or context.outputValue.count('<br')
        if linesToRead > 10:
            timeout = 8000
        else:
            timeout = linesToRead * 700
            
        #TODO: Una mejor forma de mostrar en html la salida 
        cursor = self.editor.textCursor()
        point = self.editor.cursorRect(cursor).bottomRight()
        html = """
            <span>%s</span><hr>
            <div style='text-align: right; font-size: small;'><a href='copy'>Copy</a>
            </div>""" % context.outputValue.strip().replace('\n', '<br/>').replace(' ', '&nbsp;')
        timeout = timeout * self.timespanFactor
        callbacks = {
                   'copy': lambda s = context.outputValue: QtGui.qApp.instance().clipboard().setText(s)
        }
        pos = (point.x() + 30, point.y() + 5)
        timeout = timeout * self.timespanFactor
        
        self.editor.showMessage(html, timeout = timeout, pos = pos, hrefCallbacks = callbacks)
        
    def createNewDocument(self, context):
        editor= self.editor.mainWindow.addEmptyEditor()
        editor.setPlainText(context.outputValue)
        
    def openAsNewDocument(self, context):
        editor= self.editor.mainWindow.addEmptyEditor()
        editor.setPlainText(context.outputValue)