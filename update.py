# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import sql_work


class update_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(491, 201)
        Dialog.setModal(False)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(190, 110, 121, 28))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(70, 50, 361, 21))
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        #display server connetction status in window 
        self.label.setText('ابتدا از اتصال به اینترنت مطمئن شوید')
        self.pushButton.clicked.connect(self.update_database)

    def update_database(self):
        self.label.setText('در حال ارسال لطفا منتظر بمانید ...')
        import google_sheet

        try:

            sql_work.clear_tabel()
            sql_work.fill_database(google_sheet.fetch_data()) 
        
        except:
            self.label.setText('خطا در دریافت اطلاعات')
            print('error in updating')

        else:

            self.label.setText('  بروز رسانی انجام گرفت.  لطفا یک مرتبه از برنامه خارج شده و مجدد وارد  شوید')
            print('database up to date')

        
       


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "بروز رسانی"))
        self.pushButton.setText(_translate("Dialog", "بروز رسانی"))
        self.label.setText(_translate("Dialog", "ابتدا از اتصال به اینترنت مطمئن شوید"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = update_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
