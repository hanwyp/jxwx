# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dl_br.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_dlg_br(object):
    def setupUi(self, dlg_br):
        dlg_br.setObjectName("dlg_br")
        dlg_br.setWindowModality(QtCore.Qt.ApplicationModal)
        dlg_br.resize(333, 322)
        self.txt_br = QtWidgets.QLineEdit(dlg_br)
        self.txt_br.setGeometry(QtCore.QRect(180, 30, 121, 21))
        self.txt_br.setObjectName("txt_br")
        self.btnAdd = QtWidgets.QPushButton(dlg_br)
        self.btnAdd.setGeometry(QtCore.QRect(210, 90, 75, 23))
        self.btnAdd.setObjectName("btnAdd")
        self.btnDel = QtWidgets.QPushButton(dlg_br)
        self.btnDel.setGeometry(QtCore.QRect(210, 160, 75, 23))
        self.btnDel.setObjectName("btnDel")
        self.btnRev = QtWidgets.QPushButton(dlg_br)
        self.btnRev.setGeometry(QtCore.QRect(210, 220, 75, 23))
        self.btnRev.setObjectName("btnRev")
        self.list_Br = QtWidgets.QListView(dlg_br)
        self.list_Br.setGeometry(QtCore.QRect(20, 30, 151, 231))
        self.list_Br.setObjectName("list_Br")

        self.retranslateUi(dlg_br)
        QtCore.QMetaObject.connectSlotsByName(dlg_br)

    def retranslateUi(self, dlg_br):
        _translate = QtCore.QCoreApplication.translate
        dlg_br.setWindowTitle(_translate("dlg_br", "品牌维护"))
        self.btnAdd.setText(_translate("dlg_br", "添加"))
        self.btnDel.setText(_translate("dlg_br", "删除"))
        self.btnRev.setText(_translate("dlg_br", "修改"))

