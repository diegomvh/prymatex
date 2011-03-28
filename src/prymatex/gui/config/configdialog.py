from ui_settings import Ui_PMXSettingsDialog
from PyQt4.Qt import *
from prymatex.gui.editor import center

class PMXSettingsItem(QStandardItem):
    def __init__(self, name, widget_index, parent = None):
        if isinstance(parent, QStandardItem):
            super(PMXSettingsItem, self).__init__(parent)
        else:
            super(PMXSettingsItem, self).__init__()
            
        self.setText(name)
        self.setEditable(False)
        self.widget_index = widget_index
        

class PMXNetworkConfigWidget(QWidget):
    def __init__(self):
        super(PMXNetworkConfigWidget, self).__init__()
        

class PMXSettingsDialog(QDialog, Ui_PMXSettingsDialog):
    def __init__(self):
        super(PMXSettingsDialog, self).__init__()
        self.setupUi(self)
        self.model = QStandardItemModel()
        self.treeView.setModel(self.model)
        self.treeView.widgetChanged.connect(self.changeWidget)
        self.model.setHeaderData(0, Qt.Horizontal, self.trUtf8("Option"))
        self.stackLayout = QStackedLayout()
        self.container.setLayout(self.stackLayout)
        
        #self.treeView.selectionChanged.connect(self.itemChanged)
        self.register("Editor", QLabel("Hola"))
        self.register("Network", QLabel("Chau"))
        self.register("Bundles", QLabel("Chau"))
        self.register("Save", QLabel("<b>TODO</b>"))
        self.register("Keyboard Shortcuts", QLabel("<b>TODO</b>"))
        self.register("Plugins", QLabel("<b>TODO</b>"))
    
    def exec_(self):
        center(self)
        super(PMXSettingsDialog, self).exec_()
    
    def changeWidget(self, index):
        print "Cambiando al widget"
        self.container.layout().setCurrentIndex(index)
        
        
    def register(self, name, widget):
        
        index = self.stackLayout.addWidget(widget)
        #item.setD
        item = PMXSettingsItem(name, widget_index = index)
        self.model.appendRow(item)
        
        
        

    