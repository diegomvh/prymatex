# encoding: utf-8
from PyQt4.QtGui import QApplication


class PMXApplication(QApplication):
    def __init__(self, arguments):
        
        QApplication.__init__(self, arguments)
        
        self.setApplicationName("Prymatex Text Editor")
        self.setApplicationVersion("0.1") # hg stuff?
        self.setOrganizationDomain("org")
        self.setOrganizationName("Xurix")
        self.projectUrl = 'http://code.google.com/p/prymatex'
        #self.setWindowIcon()
        from prymatex.gui.mainwindow import PMXMainWindow
        self.main_window = PMXMainWindow()
        self.main_window.show()
    
    
    def getThemePath(self):
        #TODO: Get something from the config
        pass
    
    
        