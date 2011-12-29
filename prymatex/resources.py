#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from PyQt4 import QtGui, QtCore
from prymatex import resources_rc

INTERNAL = {
    #Bundles
    "bundle": ":/icons/bundles/bundle.png",
    "template": ":/icons/bundles/templates.png",
    "command": ":/icons/bundles/commands.png",
    "syntax": ":/icons/bundles/languages.png",
    "preference": ":/icons/bundles/preferences.png",
    "dragcommand": ":/icons/bundles/drag-commands.png",
    "snippet": ":/icons/bundles/snippets.png",
    "macro": ":/icons/bundles/macros.png",
    "templatefile": ":/icons/bundles/template-files.png",
    #Editor Sidebar
    "foldingtop": ":/editor/sidebar/folding-top.png",
    "foldingbottom": ":/editor/sidebar/folding-bottom.png",
    "foldingcollapsed": ":/editor/sidebar/folding-collapsed.png",
    "foldingellipsis": ":/editor/sidebar/folding-ellipsis.png",
    "bookmarkflag": ":/editor/sidebar/bookmark-flag.png",
    #Icons
    "save": ":/icons/actions/document-save.png",
    "inserttext": ":/icons/actions/insert-text.png",
    "codefunction": ":/icons/actions/code-function.png",
    "projectnew": ":/icons/actions/project-development-new-template.png",
    "projectopen": ":/icons/actions/project-open.png",
    "projectclose": ":/icons/actions/project-development-close.png"
}

EXTERNAL = {}

FileIconProvider = QtGui.QFileIconProvider()

def getImagePath(index):
    return INTERNAL.get(index) or EXTERNAL.get(index)

def getImage(index):
    path = getImagePath(index) 
    if path is not None:
        return QtGui.QPixmap(path)

def getIcon(index):
    '''
    Makes the best effort to find an icon for an index.
    Index can be a path, a Qt resource path, an integer.
    @return: QIcon instance or None if no icon could be retrieved
    '''
    path = getImagePath(index)
    if path is not None:
        return QtGui.QIcon(path)
    elif isinstance(index, (str, unicode)):
        #Try file path
        if os.path.isfile(index):
            return FileIconProvider.icon(QtCore.QFileInfo(index))
        elif os.path.isdir(index):
            return FileIconProvider.icon(QtGui.QFileIconProvider.Folder)
        return FileIconProvider.icon(QtGui.QFileIconProvider.File)
    elif isinstance(index, int):
        return FileIconProvider.icon(index)
    
    # Fallback 
    #elif isinstance(index, QtGui.QIcon):
    #    return index
    #return QtGui.QIcon() # Empty Icon

def getFileType(fileInfo):
    return FileIconProvider.type(fileInfo)

def registerImagePath(index, path):
    EXTERNAL[index] = path