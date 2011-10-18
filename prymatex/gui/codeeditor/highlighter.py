import re
from PyQt4 import QtGui

from prymatex.gui.codeeditor.processors import PMXSyntaxProcessor
from prymatex.gui.codeeditor.userdata import PMXBlockUserData
from prymatex.support.syntax import PMXSyntax

WHITESPACE = re.compile(r'^(?P<whitespace>\s+)', re.UNICODE)
def whiteSpace(text):
    match = WHITESPACE.match(text)
    try:
        ws = match.group('whitespace')
        return ws
    except AttributeError:
        return ''

class PMXSyntaxHighlighter(QtGui.QSyntaxHighlighter):
    NO_STATE = -1
    SINGLE_LINE = 0
    MULTI_LINE = 1
    FORMAT_CACHE = {}
    
    def __init__(self, editor, syntax, theme = None):
        super(PMXSyntaxHighlighter, self).__init__(editor.document())
        assert syntax is not None, "Syntax cannot be None"
        self.editor = editor
        self.processor = PMXSyntaxProcessor()
        self.syntax = syntax
        self.theme = theme
        self.lastBlockCount = 0

    def setTheme(self, theme):
        PMXSyntaxHighlighter.FORMAT_CACHE = {}
        self.theme = theme
        
    def _analyze_all_text(self, text):
        self.syntax.parse(text, self.processor)
        for index, data in enumerate(self.processor.lines):
            block = self.document().findBlockByNumber(index)
            userData, state = self.buildBlockUserData(block, data)
            block.setUserData(userData)
            block.setUserState(state)
    
    def applyFormat(self, userData):
        for scope, start, end in userData.getAllScopes():
            format = self.getFormat(scope)
            if format is not None:
                self.setFormat(start, end - start, format)
    
    def setupBlockUserData(self, block, userData, data):
        state = self.SINGLE_LINE
        userData.setScopes(data[0])
        if data[1] is not None:
            state = self.MULTI_LINE
            userData.setStackAndScopes(*data[1])
        
        text = block.text()
        
        #Folding
        userData.foldingMark = self.syntax.folding(text)
        
        #Indent
        userData.indent = whiteSpace(text)
        
        #Symbols
        spaceLen = len(userData.indent)
        scope = userData.getScopeAtPosition(spaceLen)
        preferences = self.editor.getPreference(scope)
        userData.symbol = preferences.extractSymbol(text[spaceLen:])
        
        #Hash the text and scope
        userData.textHash = hash(self.syntax.scopeName) + hash(text)
        
        return state
        
    def highlightBlock(self, text):
        if self.lastBlockCount > self.document().blockCount():
            self.editor.textBlocksRemoved.emit()
        
        userData = self.currentBlock().userData()
        if userData is not None and userData.textHash == hash(self.syntax.scopeName) + hash(text):
            self.applyFormat(userData)
        else:
            self.processor.startParsing(self.syntax.scopeName)
            if self.previousBlockState() == self.MULTI_LINE:
                #Recupero una copia del stack y los scopes del user data
                stack, scopes = self.currentBlock().previous().userData().getStackAndScopes()
                self.processor.setScopes(scopes)
            else:
                #Creo un stack y scopes nuevos
                stack = [[self.syntax.grammar, None]]
    
            # A parserar mi amor, vamos a parsear mi amor
            self.syntax.parseLine(stack, text, self.processor)
            
            data = self.processor.lines[-1]
            if userData is None:
                userData = PMXBlockUserData()
                self.setCurrentBlockUserData(userData)
            
            oldSymbol = userData.symbol
            oldFoldingMark = userData.foldingMark
            
            state = self.setupBlockUserData(self.currentBlock(), userData, data)
            self.setCurrentBlockState(state)
            
            if userData.symbol != oldSymbol:
                self.editor.symbolChanged.emit(self.currentBlock())
            if userData.foldingMark != oldFoldingMark:
                self.editor.foldingChanged.emit(self.currentBlock())
            #self.editor.folding.deprecateFolding(self.currentBlock().blockNumber())
            self.applyFormat(userData)
        
        self.lastBlockCount = self.document().blockCount()
        
    def getFormat(self, scope):
        if self.theme is None:
            return None
        if scope not in PMXSyntaxHighlighter.FORMAT_CACHE: 
            format = QtGui.QTextCharFormat()
            settings = self.theme.getStyle(scope)
            if 'foreground' in settings:
                format.setForeground(settings['foreground'])
            if 'background' in settings:
                format.setBackground(settings['background'])
            if 'fontStyle' in settings:
                if 'bold' in settings['fontStyle']:
                    format.setFontWeight(QtGui.QFont.Bold)
                if 'underline' in settings['fontStyle']:
                    format.setFontUnderline(True)
                if 'italic' in settings['fontStyle']:
                    format.setFontItalic(True)
            PMXSyntaxHighlighter.FORMAT_CACHE[scope] = format 
        return PMXSyntaxHighlighter.FORMAT_CACHE[scope]
