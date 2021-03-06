#!/usr/bin/env python
#-*- encoding: utf-8 -*-

import os

from PyQt4 import QtGui, QtCore

from prymatex import resources
from prymatex.ui.dockers.search import Ui_SearchDock
from prymatex.core.plugin.dock import PMXBaseDock
from prymatex.utils.i18n import ugettext as _
from prymatex.gui.dockers.models import PMXSearchTreeModel, LineTreeNode
from prymatex.gui.dialogs.filesearch import PMXFileSearchDialog

class PMXSearchDock(QtGui.QDockWidget, Ui_SearchDock, PMXBaseDock):
    SHORTCUT = "Shift+F4"
    ICON = resources.getIcon("find")
    PREFERED_AREA = QtCore.Qt.BottomDockWidgetArea
    
    def __init__(self, parent):
        QtGui.QDockWidget.__init__(self, parent)
        PMXBaseDock.__init__(self)
        self.setupUi(self)
        self.searchTreeModel = PMXSearchTreeModel(self)
        self.treeView.setModel(self.searchTreeModel)

    def on_actionFileSearch_triggered(self):
        if not self.isVisible():
            self.show()
        self.raise_()
        fileSearch = PMXFileSearchDialog.search(self.searchTreeModel, self)
        #TODO: Si no se encontro nada o se cancelo cerrarlo
    
    @classmethod
    def contributeToMainMenu(cls, addonClasses):
        edit = {
            'items': [
                "-",
                {'title': "File Search",
                 'callback': cls.on_actionFileSearch_triggered }
            ]}
        return { "Edit": edit }
        
    def on_treeView_activated(self, index):
        node = self.searchTreeModel.node(index)
        if isinstance(node, LineTreeNode):
            self.application.openFile(node.path, cursorPosition = (node.lineNumber - 1, 0))
    
    def on_treeView_doubleClicked(self, index):
        node = self.searchTreeModel.node(index)
        if isinstance(node, LineTreeNode):
            self.application.openFile(node.path, cursorPosition = (node.lineNumber - 1, 0))