#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from string import Template

from PyQt4 import QtCore, QtGui

from prymatex.core import exceptions
from prymatex.core.settings import pmxConfigPorperty
from prymatex.ui.mainwindow import Ui_MainWindow
from prymatex.gui.actions import MainWindowActions
from prymatex.gui import utils, dialogs
from prymatex.gui.utils import textToObjectName, extendQMenu
from prymatex.gui.statusbar import PMXStatusBar
from prymatex.gui.processors import MainWindowCommandProcessor
from prymatex.widgets.docker import DockWidgetTitleBar
from prymatex.widgets.toolbar import DockWidgetToolBar
from prymatex.utils.i18n import ugettext as _

class PMXMainWindow(QtGui.QMainWindow, Ui_MainWindow, MainWindowActions):
    """Prymatex main window"""
    #=========================================================
    # Signals
    #=========================================================
    currentEditorChanged = QtCore.pyqtSignal(object)

    #=========================================================
    # Settings
    #=========================================================
    SETTINGS_GROUP = 'MainWindow'

    @pmxConfigPorperty(default = "$PMX_APP_NAME ($PMX_VERSION)")
    def windowTitleTemplate(self, titleTemplate):
         self.titleTemplate = Template(titleTemplate)
    
    @pmxConfigPorperty(default = True)
    def showMenuBar(self, value):
        self._showMenuBar = value
        self.menuBar().setShown(value)
    
    _editorHistory = []
    _editorHistoryIndex = 0
    
    # Constructor
    def __init__(self, application):
        """
        The main window
        @param parent: The QObject parent, in this case it should be the QApp
        @param files_to_open: The set of files to be opened when the window is shown in the screen.
        """
        QtGui.QMainWindow.__init__(self)
        self.application = application
        self.setupUi(self)
        
        self.setupDialogs()
        self.setupDockToolBars()
        self.setupMenu()
        
        self.setStatusBar(PMXStatusBar(self))
        
        # Connect Signals
        self.splitTabWidget.currentWidgetChanged.connect(self.on_currentWidgetChanged)
        self.splitTabWidget.currentWidgetChanged.connect(self.setWindowTitleForEditor)
        self.splitTabWidget.tabCloseRequest.connect(self.closeEditor)
        self.splitTabWidget.tabCreateRequest.connect(self.addEmptyEditor)
        self.application.supportManager.bundleItemTriggered.connect(self.insertBundleItem)
        
        utils.centerWidget(self, scale = (0.9, 0.8))
        self.dockers = []
        self.customEditorActions = {}
        self.customDockActions = {}

        self.setAcceptDrops(True)
        
        self.setMainWindowAsActionParent()
        self.setupHelpMenuMiscConnections()
        self.commandProcessor = MainWindowCommandProcessor(self)

    #==========================================================================
    # Bundle Items
    #==========================================================================
    def insertBundleItem(self, bundleItem, **processorSettings):
        '''Insert selected bundle item in current editor if possible'''
        editor = self.currentEditor()
        if editor is not None:
            self.currentEditor().insertBundleItem(bundleItem)
        elif not bundleItem.isEditorNeeded():
            print "vamos con nuestro processor"
            self.commandProcessor.configure(processorSettings)
            bundleItem.execute(self.commandProcessor)
        else:
            QtGui.QMessageBox.information(self, _("No editor open"), 
                                          _("%s needs an editor to run") % bundleItem.name)

    def buildEnvironment(self, env = {}):
        env.update({})
        return env

    @classmethod
    def contributeToSettings(cls):
        from prymatex.gui.settings.general import PMXGeneralWidget
        return [ PMXGeneralWidget ]
        
    #============================================================
    # Setups
    #============================================================
    def setupDialogs(self):
        from prymatex.gui.dialogs.selector import PMXSelectorDialog
                
        # Create dialogs
        self.bundleSelectorDialog = PMXSelectorDialog(self, title = _("Select Bundle Item"))
        # TODO: Connect these selectors 
        self.tabSelectorDialog = PMXSelectorDialog(self, title = _("Select tab"))
        self.symbolSelectorDialog = PMXSelectorDialog(self, title = _("Select Symbol"))
        self.bookmarkSelectorDialog = PMXSelectorDialog(self, title = _("Select Bookmark"))
    
    def setupDockToolBars(self):
        self.dockToolBars = {
            QtCore.Qt.LeftDockWidgetArea: DockWidgetToolBar("Left Dockers", QtCore.Qt.LeftDockWidgetArea, self),
            QtCore.Qt.RightDockWidgetArea: DockWidgetToolBar("Right Dockers", QtCore.Qt.RightDockWidgetArea, self),
            QtCore.Qt.TopDockWidgetArea: DockWidgetToolBar("Top Dockers", QtCore.Qt.TopDockWidgetArea, self),
            QtCore.Qt.BottomDockWidgetArea: DockWidgetToolBar("Bottom Dockers", QtCore.Qt.BottomDockWidgetArea, self),
        }
        for dockArea, toolBar in self.dockToolBars.iteritems():
            self.addToolBar(DockWidgetToolBar.DOCK_AREA_TO_TB[dockArea], toolBar)
            toolBar.hide()

    def toggleDockToolBarVisibility(self):
        for toolBar in self.dockToolBars.values():
            if toolBar.isVisible():
                toolBar.hide()
            else:
                toolBar.show()

    #============================================================
    # Componer la mainWindow
    #============================================================
    def addStatusBar(self, statusBar):
        self.statusBar().addPermanentWidget(statusBar)
    
    # Dockers    
    def addDock(self, dock, area):
        self.addDockWidget(area, dock)
        toggleAction = dock.toggleViewAction()
        self.menuPanels.addAction(toggleAction)
        self.addAction(toggleAction)
        titleBar = DockWidgetTitleBar(dock)
        titleBar.collpaseAreaRequest.connect(self.on_dockWidgetTitleBar_collpaseAreaRequest)
        dock.setTitleBarWidget(titleBar)
        dock.hide()
        self.dockers.append(dock)
    
    def on_dockWidgetTitleBar_collpaseAreaRequest(self, dock):
        if not dock.isFloating():
            area = self.dockWidgetArea(dock)
            self.dockToolBars[area].show()
        
    def addEditor(self, editor, focus = True):
        self.splitTabWidget.addTab(editor)
        if focus:
            self.setCurrentEditor(editor)
            
    def createCustomEditorMainMenu(self, name):
        menu = QtGui.QMenu(name, self.menubar)
        objectName = textToObjectName(name, prefix = "menu")
        menu.setObjectName(objectName)
        setattr(self, objectName, menu)
        action = self.menubar.insertMenu(self.menuNavigation.children()[0], menu)
        return menu, action

    def contributeToMainMenu(self, name, settings):
        actions = []
        menu = getattr(self, "menu" + name, None)
        if menu is None:
            menu, action = self.createCustomEditorMainMenu(name)
            actions.append(action)
        if 'items' in settings:
            actions.extend(extendQMenu(menu, settings['items']))
        return actions

    def registerEditorClassActions(self, editorClass, actions):
        self.logger.debug("%s, actions: %d" % (str(editorClass), len(actions)))
        #Conect Actions
        for action in actions:
            if hasattr(action, 'callback'):
                receiver = lambda checked, action = action: self.currentEditorActionDispatcher(checked, action)
                self.connect(action, QtCore.SIGNAL('triggered(bool)'), receiver)
        self.customEditorActions[editorClass] = actions
    
    def registerDockClassActions(self, dockClass, actions):
        self.logger.debug("%s, actions: %d" % (str(dockClass), len(actions)))
        #Conect Actions
        for action in actions:
            if hasattr(action, 'callback'):
                receiver = lambda checked, action = action: self.dockActionDispatcher(checked, action)
                self.connect(action, QtCore.SIGNAL('triggered(bool)'), receiver)
        self.customDockActions[dockClass] = actions
        
    def registerStatusClassActions(self, statusClass, actions):
        self.statusBar().registerStatusClassActions(statusClass, actions)
    
    def dockActionDispatcher(self, checked, action):
        #Find class for action
        dockClasses = filter(lambda (cls, actions): action in actions, self.customDockActions.items())
        assert len(dockClasses) == 1, "More than one dock class for action %s" % action
        dockClass = dockClasses[0][0]
        #Find instance
        dockInstance = filter(lambda status: status.__class__ == dockClass, self.dockers)
        assert len(dockInstance) == 1, "More than one instance for class %s" % dockClass
        dockInstance = dockInstance[0]
        
        callbackArgs = [ dockInstance ]
        if action.isCheckable():
            callbackArgs.append(checked)
        action.callback(*callbackArgs)
        
    def currentEditorActionDispatcher(self, checked, action):
        callbackArgs = [self.currentEditor()]
        if action.isCheckable():
            callbackArgs.append(checked)
        action.callback(*callbackArgs)
    
    def updateMenuForEditor(self, editor):
        if editor is None:
            for editorClass, actions in self.customEditorActions.iteritems():
                map(lambda action: action.setVisible(False), actions)
        else:
            currentEditorClass = editor.__class__ 
            
            for editorClass, actions in self.customEditorActions.iteritems():
                for action in actions:
                    action.setVisible(editorClass == currentEditorClass)
                    if editorClass == currentEditorClass and action.isCheckable() and hasattr(action, 'testChecked'):
                        action.setChecked(action.testChecked(editor))

    def showMessage(self, message):
        #Busca el show message en el editor sino ver otra forma de mostrar el mensaje
        self.currentEditor().showMessage(message)
    
    #============================================================
    # Create and manage editors
    #============================================================
    def addEmptyEditor(self):
        editor = self.application.getEditorInstance(parent = self)
        self.addEditor(editor)
        return editor
        
    def removeEditor(self, editor):
        self.splitTabWidget.removeTab(editor)
        del editor

    def findEditorForFile(self, filePath):
        # Find open editor for fileInfo
        for editor in self.splitTabWidget.allWidgets():
            if editor.filePath == filePath:
                return editor

    def editors(self):
        return self.splitTabWidget.allWidgets()
        
    def setCurrentEditor(self, editor):
        self.splitTabWidget.setCurrentWidget(editor)
    
    def currentEditor(self):
        return self.splitTabWidget.currentWidget()
    
    def on_currentWidgetChanged(self, editor):
        #Update Menu
        self.updateMenuForEditor(editor)        
        
        #Avisar al manager si tenemos editor
        self.application.supportManager.setEditorAvailable(editor != None)
        
        #Emitir señal de cambio
        self.currentEditorChanged.emit(editor)

        if editor is not None:
            self.addEditorToHistory(editor)
            editor.setFocus()
            self.application.checkExternalAction(self, editor)

    def setWindowTitleForEditor(self, editor):
        #Set Window Title for editor, editor can be None
        titleChunks = [ self.titleTemplate.safe_substitute(**self.application.supportManager.buildEnvironment()) ]
        if editor is not None:
            titleChunks.insert(0, editor.tabTitle())
        self.setWindowTitle(" - ".join(titleChunks))
        
    def saveEditor(self, editor = None, saveAs = False):
        editor = editor or self.currentEditor()
        if editor.isExternalChanged():
            message = "The file '%s' has been changed on the file system, Do you want save the file with other name?"
            result = QtGui.QMessageBox.question(editor, _("File changed"),
                _(message) % editor.filePath,
                buttons = QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                defaultButton = QtGui.QMessageBox.Yes)
            if result == QtGui.QMessageBox.Yes:
                saveAs = True
        if editor.isNew() or saveAs:
            fileDirectory = self.application.fileManager.getDirectory(self.projects.currentPath()) if editor.isNew() else editor.fileDirectory()
            fileName = editor.fileName()
            fileFilters = editor.fileFilters()
            filePath = dialogs.getSaveFile( fileDirectory, title = "Save file as" if saveAs else "Save file", 
                                            filters = fileFilters, 
                                            name = fileName)
        else:
            filePath = editor.filePath

        if filePath is not None:
            editor.save(filePath)
    
    def closeEditor(self, editor = None, cancel = False):
        editor = editor or self.currentEditor()
        buttons = QtGui.QMessageBox.Ok | QtGui.QMessageBox.No
        if cancel:
            buttons |= QtGui.QMessageBox.Cancel
        if editor is None: return
        while editor and editor.isModified():
            response = QtGui.QMessageBox.question(self, "Save", 
                "Save %s" % editor.tabTitle(), 
                buttons = buttons, 
                defaultButton = QtGui.QMessageBox.Ok)
            if response == QtGui.QMessageBox.Ok:
                self.saveEditor(editor = editor)
            elif response == QtGui.QMessageBox.No:
                break
            elif response == QtGui.QMessageBox.Cancel:
                raise exceptions.UserCancelException()
        editor.close()
        self.removeEditor(editor)
    
    def tryCloseEmptyEditor(self, editor = None):
        editor = editor or self.currentEditor()
        if editor is not None and editor.isNew() and not editor.isModified():
            self.closeEditor(editor)
    
    #=========================================================
    # Handle history
    #=========================================================
    def addEditorToHistory(self, editor):
        if self._editorHistory and self._editorHistory[self._editorHistoryIndex] == editor:
            return
        self._editorHistory.insert(self._editorHistoryIndex, editor)
        
    #===========================================================================
    # MainWindow Events
    #===========================================================================
    def closeEvent(self, event):
        for editor in self.editors():
            while editor and editor.isModified():
                response = QtGui.QMessageBox.question(self, "Save", 
                    "Save %s" % editor.tabTitle(), 
                    buttons = QtGui.QMessageBox.Ok | QtGui.QMessageBox.No | QtGui.QMessageBox.Cancel, 
                    defaultButton = QtGui.QMessageBox.Ok)
                if response == QtGui.QMessageBox.Ok:
                    self.saveEditor(editor = editor)
                elif response == QtGui.QMessageBox.No:
                    break
                elif response == QtGui.QMessageBox.Cancel:
                    event.ignore()
                    return
        
    #===========================================================================
    # MainWindow State
    #===========================================================================
    def saveState(self):
        #Documentos abiertos
        openDocumentsOnQuit = []
        for editor in self.editors():
            if not editor.isNew():
                openDocumentsOnQuit.append((editor.filePath, editor.cursorPosition()))
        state = {
            "self": QtGui.QMainWindow.saveState(self),
            "dockers": dict(map(lambda dock: (dock.objectName(), dock.saveState()), self.dockers)),
            "documents": openDocumentsOnQuit,
            "geometry": self.saveGeometry(),
        }
        return state

    def restoreState(self, state):
        try:
            map(lambda dock: dock.restoreState(state["dockers"][dock.objectName()]), self.dockers)
            self.restoreGeometry(state["geometry"])
            for doc in state["documents"]:
                self.application.openFile(*doc, mainWindow = self)
            QtGui.QMainWindow.restoreState(self, state["self"])
            
        except (TypeError, ValueError) as e:
            self.logger.error("Could not restore state for %s. Reason %s" % (self, e))

    #===========================================================================
    # Drag and Drop
    #===========================================================================
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
    
    def dropEvent(self, event):
        def collectFiles(paths):
            from glob import glob
            '''Recursively collect fileInfos'''
            for path in paths:
                if os.path.isfile(path):
                    yield path
                elif os.path.isdir(path):
                    dirSubEntries = glob(os.path.join(path, '*'))
                    for entry in collectFiles(dirSubEntries):
                        yield entry
                        
        urls = map(lambda url: url.toLocalFile(), event.mimeData().urls())
        
        for path in collectFiles(urls):
            # TODO: Take this code somewhere else, this should change as more editor are added
            if not self.canBeOpened(path):
                self.logger.debug("Skipping dropped element %s" % path)
                continue
            self.logger.debug("Opening dropped file %s" % path)
            #self.openFile(QtCore.QFileInfo(path), focus = False)
            self.application.openFile(path)

    FILE_SIZE_THERESHOLD = 1024 ** 2 # 1MB file is enough, ain't it?
    STARTSWITH_BLACKLIST = ['.', '#', ]
    ENDSWITH_BLACKLIST = ['~', 'pyc', 'bak', 'old', 'tmp', 'swp', '#', ]
    
    def canBeOpened(self, path):
        # Is there any support for it?
        if not self.application.supportManager.findSyntaxByFileType(path):
            return False
        for start in self.STARTSWITH_BLACKLIST:
            if path.startswith(start):
                return False
        for end in self.ENDSWITH_BLACKLIST:
            if path.endswith(end):
                return False
        if os.path.getsize(path) > self.FILE_SIZE_THERESHOLD:
            return False
        return True
        