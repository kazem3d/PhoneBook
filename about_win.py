# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class about_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(458, 229)
        dialog.setAutoFillBackground(False)
        self.label = QtWidgets.QLabel(dialog)
        self.label.setGeometry(QtCore.QRect(40, 150, 331, 71))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setOpenExternalLinks(True)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 90, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(dialog)
        self.label_4.setGeometry(QtCore.QRect(80, 130, 341, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setOpenExternalLinks(True)
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(dialog)
        self.label_2.setGeometry(QtCore.QRect(34, 20, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 60, 391, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(dialog)
        QtCore.QMetaObject.connectSlotsByName(dialog)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "About this app"))
        self.label.setText(_translate("dialog", "تهیه کننده کاظم قناتی Kazem3d@gmail.com"))
        self.label_3.setText(_translate("dialog", "Git hub link to access open soureces file:"))
        self.label_4.setText(_translate("dialog", "<html><head/><body><p><a href=\"https://github.com/kazem3d/PhoneBook.git\"><span style=\" text-decoration: underline; color:#0000ff;\">https://github.com/kazem3d/PhoneBook.git</span></a></p></body></html>"))
        self.label_2.setText(_translate("dialog", "Phone Book v1.0"))
        self.label_5.setText(_translate("dialog", "this app licenced under GNU General Public License v3.0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = about_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())
