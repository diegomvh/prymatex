# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'resources/ui/dialogs/newfromtemplate.ui'
#
# Created: Thu May 10 16:19:51 2012
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from prymatex.utils.i18n import ugettext as _
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_NewFromTemplateDialog(object):
    def setupUi(self, NewFromTemplateDialog):
        NewFromTemplateDialog.setObjectName(_fromUtf8("NewFromTemplateDialog"))
        NewFromTemplateDialog.setWindowModality(QtCore.Qt.WindowModal)
        NewFromTemplateDialog.resize(450, 115)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/prymatex/logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        NewFromTemplateDialog.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(NewFromTemplateDialog)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout_2 = QtGui.QFormLayout()
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label3 = QtGui.QLabel(NewFromTemplateDialog)
        self.label3.setObjectName(_fromUtf8("label3"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label3)
        self.label2 = QtGui.QLabel(NewFromTemplateDialog)
        self.label2.setObjectName(_fromUtf8("label2"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label2)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.lineLocation = QtGui.QLineEdit(NewFromTemplateDialog)
        self.lineLocation.setObjectName(_fromUtf8("lineLocation"))
        self.horizontalLayout_5.addWidget(self.lineLocation)
        self.buttonChoose = QtGui.QPushButton(NewFromTemplateDialog)
        self.buttonChoose.setObjectName(_fromUtf8("buttonChoose"))
        self.horizontalLayout_5.addWidget(self.buttonChoose)
        self.formLayout_2.setLayout(1, QtGui.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.label1 = QtGui.QLabel(NewFromTemplateDialog)
        self.label1.setObjectName(_fromUtf8("label1"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label1)
        self.lineFileName = QtGui.QLineEdit(NewFromTemplateDialog)
        self.lineFileName.setObjectName(_fromUtf8("lineFileName"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.FieldRole, self.lineFileName)
        self.comboTemplates = QtGui.QComboBox(NewFromTemplateDialog)
        self.comboTemplates.setObjectName(_fromUtf8("comboTemplates"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.FieldRole, self.comboTemplates)
        self.verticalLayout.addLayout(self.formLayout_2)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.buttonCreate = QtGui.QPushButton(NewFromTemplateDialog)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/actions/document-new.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonCreate.setIcon(icon1)
        self.buttonCreate.setObjectName(_fromUtf8("buttonCreate"))
        self.horizontalLayout.addWidget(self.buttonCreate)
        self.buttonCancel = QtGui.QPushButton(NewFromTemplateDialog)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8(":/icons/actions/dialog-cancel.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonCancel.setIcon(icon2)
        self.buttonCancel.setObjectName(_fromUtf8("buttonCancel"))
        self.horizontalLayout.addWidget(self.buttonCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(NewFromTemplateDialog)
        QtCore.QObject.connect(self.buttonCancel, QtCore.SIGNAL(_fromUtf8("clicked()")), NewFromTemplateDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewFromTemplateDialog)
        NewFromTemplateDialog.setTabOrder(self.lineFileName, self.lineLocation)
        NewFromTemplateDialog.setTabOrder(self.lineLocation, self.comboTemplates)
        NewFromTemplateDialog.setTabOrder(self.comboTemplates, self.buttonChoose)
        NewFromTemplateDialog.setTabOrder(self.buttonChoose, self.buttonCreate)

    def retranslateUi(self, NewFromTemplateDialog):
        NewFromTemplateDialog.setWindowTitle(_('New File From Template'))
        self.label3.setText(_('Template:'))
        self.label2.setText(_('Location:'))
        self.buttonChoose.setText(_('Ch&oose'))
        self.label1.setText(_('File Name:'))
        self.buttonCreate.setText(_('&Create'))
        self.buttonCancel.setText(_('C&ancel'))

from prymatex import resources_rc
