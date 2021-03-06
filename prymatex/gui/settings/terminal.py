
import os

from PyQt4 import QtGui, QtCore
from prymatex.ui.configure.terminal import Ui_Terminal
from prymatex.gui.settings.models import PMXSettingTreeNode
from prymatex.utils.i18n import ugettext as _
from prymatex import resources

class PMXTerminalSettings(QtGui.QWidget, PMXSettingTreeNode, Ui_Terminal):
    TITLE = "Terminal"
    ICON = resources.getIcon("terminal")
    
    def __init__(self, settingGroup, parent = None):
        QtGui.QWidget.__init__(self, parent)
        PMXSettingTreeNode.__init__(self, "terminal", settingGroup)
        self.setupUi(self)
        
        try:
            from QTermWidget import QTermWidget
        except ImportError:
            return
        
        t = QTermWidget()
        
        self.comboScrollBar.addItem(_("No scrollbar"), t.NoScrollBar)
        self.comboScrollBar.addItem(_("Left scrollbar"), t.ScrollBarLeft)
        self.comboScrollBar.addItem(_("Right scrollbar"), t.ScrollBarRight)
        
        for name in t.availableColorSchemes():
            self.comboColorScheme.addItem(name, name)
        
        del t
        
    def loadSettings(self):
        colorScheme = self.settingGroup.value('colorScheme')
        self.comboColorScheme.setCurrentIndex(self.comboColorScheme.findData(colorScheme))    
        font = self.settingGroup.value('font')
        self.lineFont.setFont(font)
        self.lineFont.setText("%s, %d" % (font.family(), font.pointSize()))
        
    @QtCore.pyqtSlot(int)
    def on_comboColorScheme_activated(self, index):
        scheme = self.comboColorScheme.itemData(index)
        self.settingGroup.setValue('colorScheme', scheme)

    @QtCore.pyqtSlot()
    def on_pushButtonChangeFont_pressed(self):
        font = self.settingGroup.value('font')
        font, ok = QtGui.QFontDialog.getFont(font, self, _("Select terminal font"))
        if ok:
            self.settingGroup.setValue('font', font)
            self.lineFont.setFont(font)
            self.lineFont.setText("%s, %d" % (font.family(), font.pointSize()))