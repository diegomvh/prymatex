# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files/command.ui'
#
# Created: Tue May 31 18:51:24 2011
#      by: PyQt4 UI code generator 4.8.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Command(object):
    def setupUi(self, Command):
        Command.setObjectName(_fromUtf8("Command"))
        Command.resize(361, 264)
        self.formLayout_2 = QtGui.QFormLayout(Command)
        self.formLayout_2.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout_2.setMargin(0)
        self.formLayout_2.setSpacing(2)
        self.formLayout_2.setObjectName(_fromUtf8("formLayout_2"))
        self.label = QtGui.QLabel(Command)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout_2.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.comboBox = QtGui.QComboBox(Command)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.horizontalLayout_2.addWidget(self.comboBox)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.formLayout_2.setLayout(0, QtGui.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.label_2 = QtGui.QLabel(Command)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.plainTextEdit = QtGui.QPlainTextEdit(Command)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.formLayout_2.setWidget(1, QtGui.QFormLayout.FieldRole, self.plainTextEdit)
        self.label_3 = QtGui.QLabel(Command)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout_2.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.comboBox_2 = QtGui.QComboBox(Command)
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.label_5 = QtGui.QLabel(Command)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout.addWidget(self.label_5)
        self.comboBox_3 = QtGui.QComboBox(Command)
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.comboBox_3.addItem(_fromUtf8(""))
        self.horizontalLayout.addWidget(self.comboBox_3)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.formLayout_2.setLayout(2, QtGui.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_4 = QtGui.QLabel(Command)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout_2.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.comboBox_4 = QtGui.QComboBox(Command)
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.horizontalLayout_3.addWidget(self.comboBox_4)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem2)
        self.formLayout_2.setLayout(3, QtGui.QFormLayout.FieldRole, self.horizontalLayout_3)

        self.retranslateUi(Command)
        QtCore.QMetaObject.connectSlotsByName(Command)

    def retranslateUi(self, Command):
        Command.setWindowTitle(QtGui.QApplication.translate("Command", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Command", "Save:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(0, QtGui.QApplication.translate("Command", "Nothing", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(1, QtGui.QApplication.translate("Command", "Current File", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox.setItemText(2, QtGui.QApplication.translate("Command", "All Files in Project", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Command", "Command(s):", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Command", "Input:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(0, QtGui.QApplication.translate("Command", "None", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(1, QtGui.QApplication.translate("Command", "Selected Text", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_2.setItemText(2, QtGui.QApplication.translate("Command", "Entire Document", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Command", "or", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(0, QtGui.QApplication.translate("Command", "Document", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(1, QtGui.QApplication.translate("Command", "Line", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(2, QtGui.QApplication.translate("Command", "Word", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(3, QtGui.QApplication.translate("Command", "Character", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(4, QtGui.QApplication.translate("Command", "Scope", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_3.setItemText(5, QtGui.QApplication.translate("Command", "Nothing", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Command", "Output:", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_4.setItemText(0, QtGui.QApplication.translate("Command", "Discard", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_4.setItemText(1, QtGui.QApplication.translate("Command", "Replace Selected Text", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_4.setItemText(2, QtGui.QApplication.translate("Command", "Replace Document", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_4.setItemText(3, QtGui.QApplication.translate("Command", "Insert as Text", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_4.setItemText(4, QtGui.QApplication.translate("Command", "Insert as Snippet", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_4.setItemText(5, QtGui.QApplication.translate("Command", "Show as HTML", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_4.setItemText(6, QtGui.QApplication.translate("Command", "Show as Tool Tip", None, QtGui.QApplication.UnicodeUTF8))
        self.comboBox_4.setItemText(7, QtGui.QApplication.translate("Command", "Create New Document", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Command = QtGui.QWidget()
    ui = Ui_Command()
    ui.setupUi(Command)
    Command.show()
    sys.exit(app.exec_())

