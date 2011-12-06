# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/dialogs/newproject.ui'
#
# Created: Tue Dec  6 19:41:59 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from prymatex.utils.i18n import ugettext as _
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_NewProjectDialog(object):
    def setupUi(self, NewProjectDialog):
        NewProjectDialog.setObjectName(_fromUtf8("NewProjectDialog"))
        NewProjectDialog.setWindowModality(QtCore.Qt.WindowModal)
        NewProjectDialog.resize(450, 158)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/icons/Prymatex_Logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NewProjectDialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(NewProjectDialog)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.ExpandingFieldsGrow)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label1 = QtGui.QLabel(NewProjectDialog)
        self.label1.setObjectName(_fromUtf8("label1"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label1)
        self.lineProjectName = QtGui.QLineEdit(NewProjectDialog)
        self.lineProjectName.setObjectName(_fromUtf8("lineProjectName"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineProjectName)
        self.label2 = QtGui.QLabel(NewProjectDialog)
        self.label2.setObjectName(_fromUtf8("label2"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.lineLocation = QtGui.QLineEdit(NewProjectDialog)
        self.lineLocation.setEnabled(False)
        self.lineLocation.setObjectName(_fromUtf8("lineLocation"))
        self.horizontalLayout_5.addWidget(self.lineLocation)
        self.buttonChoose = QtGui.QPushButton(NewProjectDialog)
        self.buttonChoose.setEnabled(False)
        self.buttonChoose.setObjectName(_fromUtf8("buttonChoose"))
        self.horizontalLayout_5.addWidget(self.buttonChoose)
        self.formLayout_2.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.label3 = QtGui.QLabel(NewProjectDialog)
        self.label3.setObjectName(_fromUtf8("label3"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.LabelRole, self.label3)
        self.comboBoxWorkingSet = QtGui.QComboBox(NewProjectDialog)
        self.comboBoxWorkingSet.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBoxWorkingSet.sizePolicy().hasHeightForWidth())
        self.comboBoxWorkingSet.setSizePolicy(sizePolicy)
        self.comboBoxWorkingSet.setEditable(True)
        self.comboBoxWorkingSet.setObjectName(_fromUtf8("comboBoxWorkingSet"))
        self.formLayout_2.setWidget(4, QtGui.QFormLayout.FieldRole, self.comboBoxWorkingSet)
        self.checkBoxUseDefaultLocation = QtGui.QCheckBox(NewProjectDialog)
        self.checkBoxUseDefaultLocation.setChecked(True)
        self.checkBoxUseDefaultLocation.setObjectName(_fromUtf8("checkBoxUseDefaultLocation"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.checkBoxUseDefaultLocation)
        self.checkBoxAddToWorkingSet = QtGui.QCheckBox(NewProjectDialog)
        self.checkBoxAddToWorkingSet.setChecked(False)
        self.checkBoxAddToWorkingSet.setObjectName(_fromUtf8("checkBoxAddToWorkingSet"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.FieldRole, self.checkBoxAddToWorkingSet)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buttonCreate = QtGui.QPushButton(NewProjectDialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/actions/project-development-new-template.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonCreate.setIcon(icon1)
        self.buttonCreate.setObjectName(_fromUtf8("buttonCreate"))
        self.horizontalLayout.addWidget(self.buttonCreate)
        self.buttonCancel = QtGui.QPushButton(NewProjectDialog)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/actions/dialog-cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonCancel.setIcon(icon2)
        self.buttonCancel.setObjectName(_fromUtf8("buttonCancel"))
        self.horizontalLayout.addWidget(self.buttonCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(NewProjectDialog)
        QtCore.QObject.connect(self.buttonCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), NewProjectDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewProjectDialog)
        NewProjectDialog.setTabOrder(self.lineProjectName, self.lineLocation)
        NewProjectDialog.setTabOrder(self.lineLocation, self.buttonChoose)
        NewProjectDialog.setTabOrder(self.buttonChoose, self.buttonCreate)

    def retranslateUi(self, NewProjectDialog):
        NewProjectDialog.setWindowTitle(_('New Project'))
        self.label1.setText(_('Name:'))
        self.label2.setText(_('Location:'))
        self.buttonChoose.setText(_('Ch&oose'))
        self.label3.setText(_('Working Set'))
        self.checkBoxUseDefaultLocation.setText(_('Use default location'))
        self.checkBoxAddToWorkingSet.setText(_('Add to working set'))
        self.buttonCreate.setText(_('&Create'))
        self.buttonCancel.setText(_('C&ancel'))

from prymatex import resources_rc
