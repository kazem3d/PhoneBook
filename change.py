# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class change_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(491, 268)
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 180, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(30, 80, 431, 81))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 40, 350, 20))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(140, 210, 321, 31))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        # self.label_3.setText(google_sheet.connect_message)
        self.label_3.setText('ابتدا از اتصال به اینترنت مطمئن شوید')

        self.pushButton_2.clicked.connect(self.sending)
        # app.processEvents()
        
    def sending(self):
        
        self.label_3.setText('در حال ارسال لطفا منتظر بمانید ...')
        import google_sheet

        message=self.textEdit.toPlainText()
        

        try:
    
            print('sending ...')
            google_sheet.sheet_request.append_row([message])

        except:
            print ('sending error')
            self.label_3.setText('خطا در ارسال')
        else:
            print('sending done')
            self.label_3.setText('ارسال انجام شد')



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "درخواست تغییر"))
        self.pushButton_2.setText(_translate("Dialog", "ارسال"))
        self.label.setText(_translate("Dialog", "درخواست خود را به صورت پیام  وارد کنید :"))
        self.label_3.setText(_translate("Dialog", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = change_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
