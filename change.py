# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'change.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import google_sheet

# connect_message='در حال ارتباط با سرور...'


class change_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(568, 310)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(320, 180, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 180, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(80, 80, 431, 81))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(330, 40, 181, 20))
        font = QtGui.QFont()
        font.setFamily("B Homa")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 230, 411, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(170, 260, 261, 21))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.label_2.setText(google_sheet.connect_message)
        self.pushButton_2.clicked.connect(self.sending)
        
    def sending(self):
        
        message=self.textEdit.toPlainText()
        self.label_3.setText('در حال ارسال لطفا منتظر بمانید ...')
        # app.processEvents()

        try:
    
            print('sending ...')
            google_sheet.sheet.append_row([message])

        except:
            print ('sending error')
            self.label_3.setText('خطا در ارسال')
        else:
            print('sending done')
            self.label_3.setText('ارسال انجام شد')



    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "درخواست تغییر"))
        self.pushButton.setText(_translate("Dialog", "لغو"))
        self.pushButton_2.setText(_translate("Dialog", "ارسال"))
        self.label.setText(_translate("Dialog", "درخواست خود را وارد کنید :"))
        self.label_2.setText(_translate("Dialog", "قبل از ارسال نسبت به متصل بودن به اینترنت مطمئن شوید"))
        # self.label_3.setText(_translate("Dialog", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = change_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
