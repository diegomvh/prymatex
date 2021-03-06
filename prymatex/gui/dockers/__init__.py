#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore

from prymatex.gui.dockers.filesystem import PMXFileSystemDock
from prymatex.gui.dockers.browser import PMXBrowserDock
from prymatex.gui.dockers.console import PMXConsoleDock
from prymatex.gui.dockers.logger import PMXLoggerDock
from prymatex.gui.dockers.projects import PMXProjectDock
from prymatex.gui.dockers.terminal import PMXTerminalDock
from prymatex.gui.dockers.search import PMXSearchDock
from prymatex.gui.dockers.process import PMXProcessDock

def registerPlugin(manager):
    manager.registerDocker(PMXProjectDock)
    manager.registerDocker(PMXFileSystemDock)
    manager.registerDocker(PMXTerminalDock)
    manager.registerDocker(PMXConsoleDock)
    manager.registerDocker(PMXBrowserDock)
    manager.registerDocker(PMXSearchDock)
    manager.registerDocker(PMXProcessDock)
    #manager.registerDocker(PMXLoggerDock)