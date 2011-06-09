# -*- coding: utf-8 -*-
#!/usr/bin/env python

######################### SyntaxProcessor #########################

class PMXSyntaxProcessor(object):
    '''
        Syntax Processor, clase base para los procesadores de sintaxis
    '''
    def __init__(self):
        pass

    def openTag(self, name, position):
        pass

    def closeTag(self, name, position):
        pass

    def newLine(self, line):
        pass

    def startParsing(self, name):
        pass

    def endParsing(self, name):
        pass

######################### Command Processor #########################
class PMXCommandProcessor(object):
    def __init__(self):
        pass
    
    def startCommand(self, command):
        pass
    def endCommand(self, command):
        pass
    
    # beforeRunningCommand
    def saveActiveFile(self):
        return True
    def saveModifiedFiles(self):
        return True
    def nop(self):
        return True
    
    # deleteFromEditor
    def deleteWord(self):
        pass
    def deleteSelection(self):
        pass
    def deleteCharacter(self):
        pass

    # on error
    def commandError(self, text, code):
        pass
    
    # Outpus function
    def discard(self, text):
        pass
    def replaceSelectedText(self, text):
        pass
    def replaceDocument(self, text):
        pass
    def insertText(self, text):
        pass
    def afterSelectedText(self, text):
        pass
    def insertAsSnippet(self, text):
        pass
    def showAsHTML(self, text):
        pass
    def showAsTooltip(self, text):
        pass
    def createNewDocument(self, text):
        pass

class PMXSnippetProcessor(object):
    def __init__(self):
        pass
    
    def startSnippet(self, snippet):
        pass
    def endSnippet(self):
        pass

######################### Macro Processor #########################
class PMXMacroProcessor(object):
    def __init__(self):
        pass

    # Move
    def moveRight(self):
        pass
   
    def moveLeft(self):
        pass
        
    def moveUp(self):
        pass
        
    def moveToEndOfLine(self):
        pass
        
    def moveToEndOfParagraph(self):
        pass
        
    def moveToBeginningOfLine(self):
        pass
        
    def moveToEndOfDocumentAndModifySelection(self):
        pass
        
    def moveToBeginningOfDocumentAndModifySelection(self):
        pass
        
    def moveRightAndModifySelection(self):
        pass
        
    def centerSelectionInVisibleArea(self):
        pass
    def alignLeft(self):
        pass
    # Inserts
    def insertText(self, argument):
        pass
        
    def insertNewline(self):
        pass
    
    # Deletes
    def deleteForward(self):
        pass
        
    def deleteBackward(self):
        pass
    
    def deleteWordLeft(self):
        pass
        
    def deleteToBeginningOfLine(self):
        pass
    # Selects
    def selectWord(self):
        pass
        
    def selectAll(self):
        pass
        
    def selectHardLine(self):
        pass
    def executeCommandWithOptions(self, argument):
        pass
        
    def insertSnippetWithOptions(self):
        pass
        
    def findWithOptions(self, argument):
        pass
        
    def indent(self):
        pass
############# DebugS Preocessors ###############
class PMXDebugSyntaxProcessor(PMXSyntaxProcessor):
    def __init__(self):
        self.line_number = 0
        self.printable_line = ''

    def pprint(self, line, string, position = 0):
        line = line[:position] + string + line[position:]
        return line

    def openTag(self, name, position):
        print self.pprint( '', '{ %d - %s' % (position, name), position + len(self.line_marks))

    def closeTag(self, name, position):
        print self.pprint( '', '} %d - %s' % (position, name), position + len(self.line_marks))

    def newLine(self, line):
        self.line_number += 1
        self.line_marks = '[%04s] ' % self.line_number
        print '%s%s' % (self.line_marks, line)

    def startParsing(self, name):
        print '{%s' % name

    def endParsing(self, name):
        print '}%s' % name
