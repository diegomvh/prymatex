#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from PyQt4 import QtCore, QtGui

#TODO: en inicialize deberia pasar un proveedro de servicios o otra forma menos directa de que un plguin hable con el core
class PMXBasePlugin(object):
    
    def initialize(self):
        raise NotImplemented
    
    def finalize(self):
        pass
    
class PMXBaseWidgetPlugin(PMXBasePlugin):
    def __init__(self):
        self.overlays = []
            
    def initialize(self):
        for overlay in self.overlays:
            overlay.initialize()

    def updateOverlays(self):
        for overlay in self.overlays:
            overlay.updateOverlay()
    
    def addOverlay(self, overlay):
        self.overlays.append(overlay)
    
    def showMessage(self, *largs, **kwargs):
        for overlay in self.overlays:
            overlay.showMessage(*largs, **kwargs)

class PMXBaseOverlay(PMXBasePlugin):
    def initialize(self):
        pass
    
    def updateOverlay(self):
        pass
    
    def showMessage(self, *largs, **kwargs):
        pass

Key_Any = 0
class PMXBaseKeyHelper(PMXBasePlugin):
    KEY = Key_Any
    def accept(self, editor, event, cursor = None, scope = None):
        pass
    
    def execute(self, editor, event, cursor = None, scope = None):
        pass
    
class PMXBaseAddon(PMXBasePlugin):
    pass