# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from excel_conv import tabel_list
from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindow(object):

    def getDate(self):
        self.tableWidget.setRowCount(0)
        for row_id , row_data in enumerate(tabel_list):
            self.tableWidget.insertRow(row_id)
            row_data=tabel_list[row_id]
            for column_id , column_data in enumerate(row_data) :
                self.tableWidget.setItem(row_id,column_id,QtWidgets.QTableWidgetItem(str(column_data)))
        
   
    def setupUi(self, MainWindow):
            MainWindow.setObjectName("MainWindow")
            MainWindow.resize(1070, 485)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
            MainWindow.setSizePolicy(sizePolicy)
            MainWindow.setMinimumSize(QtCore.QSize(1070, 485))
            MainWindow.setMaximumSize(QtCore.QSize(1070, 500))
            MainWindow.setSizeIncrement(QtCore.QSize(1070, 500))
            MainWindow.setBaseSize(QtCore.QSize(1070, 500))
            MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
            MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
            self.centralwidget = QtWidgets.QWidget(MainWindow)
            self.centralwidget.setObjectName("centralwidget")
            self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
            self.tableWidget.setGeometry(QtCore.QRect(10, 150, 1041, 281))
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
            self.tableWidget.setSizePolicy(sizePolicy)
            self.tableWidget.setBaseSize(QtCore.QSize(0, 0))
            font = QtGui.QFont()
            font.setFamily("B Kamran")
            font.setPointSize(12)
            font.setBold(True)
            font.setWeight(75)
            self.tableWidget.setFont(font)
            self.tableWidget.setFocusPolicy(QtCore.Qt.NoFocus)
            self.tableWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
            self.tableWidget.setAcceptDrops(False)
            self.tableWidget.setLayoutDirection(QtCore.Qt.RightToLeft)
            self.tableWidget.setAutoFillBackground(False)
            self.tableWidget.setInputMethodHints(QtCore.Qt.ImhDialableCharactersOnly|QtCore.Qt.ImhDigitsOnly|QtCore.Qt.ImhEmailCharactersOnly|QtCore.Qt.ImhFormattedNumbersOnly|QtCore.Qt.ImhLatinOnly|QtCore.Qt.ImhLowercaseOnly|QtCore.Qt.ImhUppercaseOnly|QtCore.Qt.ImhUrlCharactersOnly)
            self.tableWidget.setFrameShape(QtWidgets.QFrame.StyledPanel)
            self.tableWidget.setFrameShadow(QtWidgets.QFrame.Sunken)
            self.tableWidget.setLineWidth(1)
            self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
            self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
            self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
            self.tableWidget.setAutoScroll(True)
            self.tableWidget.setAutoScrollMargin(18)
            self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
            self.tableWidget.setTabKeyNavigation(False)
            self.tableWidget.setProperty("showDropIndicator", False)
            self.tableWidget.setDragDropOverwriteMode(False)
            self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
            self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
            self.tableWidget.setShowGrid(True)
            self.tableWidget.setGridStyle(QtCore.Qt.SolidLine)
            self.tableWidget.setWordWrap(False)
            self.tableWidget.setCornerButtonEnabled(False)
            self.tableWidget.setRowCount(3)
            self.tableWidget.setColumnCount(6)
            self.tableWidget.setObjectName("tableWidget")
            item = QtWidgets.QTableWidgetItem()
            brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
            brush.setStyle(QtCore.Qt.SolidPattern)
            item.setForeground(brush)
            self.tableWidget.setHorizontalHeaderItem(0, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(1, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(2, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(3, item)
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(4, item)
            item = QtWidgets.QTableWidgetItem()
            font = QtGui.QFont()
            font.setPointSize(8)
            item.setFont(font)
            self.tableWidget.setHorizontalHeaderItem(5, item)
            item = QtWidgets.QTableWidgetItem()
            item.setFlags(QtCore.Qt.NoItemFlags)
            self.tableWidget.setItem(0, 0, item)
            self.tableWidget.horizontalHeader().setVisible(True)
            self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
            self.tableWidget.horizontalHeader().setHighlightSections(True)
            self.tableWidget.verticalHeader().setVisible(False)
            self.tableWidget.verticalHeader().setHighlightSections(False)
            self.tableWidget.verticalHeader().setStretchLastSection(False)
            self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
            self.lineEdit.setGeometry(QtCore.QRect(650, 90, 361, 41))
            font = QtGui.QFont()
            font.setFamily("B Kamran")
            font.setPointSize(11)
            font.setBold(True)
            font.setWeight(75)
            self.lineEdit.setFont(font)
            self.lineEdit.setToolTip("")
            self.lineEdit.setStatusTip("")
            self.lineEdit.setWhatsThis("")
            self.lineEdit.setAccessibleName("")
            self.lineEdit.setAccessibleDescription("")
            self.lineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
            self.lineEdit.setAutoFillBackground(False)
            self.lineEdit.setText("")
            self.lineEdit.setFrame(True)
            self.lineEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
            self.lineEdit.setObjectName("lineEdit")
            self.label = QtWidgets.QLabel(self.centralwidget)
            self.label.setGeometry(QtCore.QRect(700, 10, 341, 31))
            font = QtGui.QFont()
            font.setFamily("B Titr")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.label.setFont(font)
            self.label.setObjectName("label")
            self.label_2 = QtWidgets.QLabel(self.centralwidget)
            self.label_2.setGeometry(QtCore.QRect(920, 50, 121, 31))
            font = QtGui.QFont()
            font.setFamily("B Titr")
            font.setPointSize(10)
            font.setBold(True)
            font.setWeight(75)
            self.label_2.setFont(font)
            self.label_2.setObjectName("label_2")
            self.label_3 = QtWidgets.QLabel(self.centralwidget)
            self.label_3.setGeometry(QtCore.QRect(190, 10, 171, 131))
            self.label_3.setText("")
            self.label_3.setPixmap(QtGui.QPixmap("l.png"))
            self.label_3.setObjectName("label_3")
            self.label_4 = QtWidgets.QLabel(self.centralwidget)
            self.label_4.setGeometry(QtCore.QRect(1020, 90, 41, 41))
            self.label_4.setText("")
            self.label_4.setPixmap(QtGui.QPixmap("searchLogo.png"))
            self.label_4.setObjectName("label_4")
            self.pushButton = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton.setGeometry(QtCore.QRect(20, 50, 121, 28))
            self.pushButton.setObjectName("pushButton")
            self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_2.setGeometry(QtCore.QRect(20, 10, 121, 28))
            self.pushButton_2.setObjectName("pushButton_2")
            self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
            self.pushButton_3.setGeometry(QtCore.QRect(20, 90, 121, 28))
            self.pushButton_3.setObjectName("pushButton_3")
            self.label_5 = QtWidgets.QLabel(self.centralwidget)
            self.label_5.setGeometry(QtCore.QRect(1020, 90, 31, 41))
            self.label_5.setText("")
            self.label_5.setPixmap(QtGui.QPixmap("searchLogo1.png"))
            self.label_5.setObjectName("label_5")
            MainWindow.setCentralWidget(self.centralwidget)
            self.menubar = QtWidgets.QMenuBar(MainWindow)
            self.menubar.setGeometry(QtCore.QRect(0, 0, 1070, 26))
            self.menubar.setObjectName("menubar")
            MainWindow.setMenuBar(self.menubar)
            self.statusbar = QtWidgets.QStatusBar(MainWindow)
            self.statusbar.setObjectName("statusbar")
            MainWindow.setStatusBar(self.statusbar)


            self.retranslateUi(MainWindow)
            QtCore.QMetaObject.connectSlotsByName(MainWindow)
    





            self.getDate()
            self.lineEdit.textChanged.connect(self.filter_items)


    def filter_items(self, text):

        rows = self.tableWidget.model().rowCount()
        for row in range(rows):
            self.filter_row(row, text)


    def filter_row(self, row, pattern):
        if not pattern:
            self.tableWidget.setRowHidden(row, False)
            return

        model = self.tableWidget.model()
        columns = model.columnCount()
        stringlist = []

        # collect text from all columns into single string for searching
        for c in range(columns):
            mdx = model.index(row, c)
            if mdx.isValid():
                val = str(mdx.data(role=QtCore.Qt.DisplayRole)).lower()
                stringlist.append(val)

        # search for string
        patterns = filter(None, [x.lower() for x in pattern.split(' ')])
        results = all(any(x in y for y in stringlist) for x in patterns)
        if results:
            self.tableWidget.setRowHidden(row, False)
        else:
            self.tableWidget.setRowHidden(row, True)  



    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "دفترچه تلفن"))
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "نام"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "شغل"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "داخلی"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "مستقیم"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "فکس"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "IP Phone"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "   جستجوی نام یا شغل ..."))
        self.label.setText(_translate("MainWindow", "اداره کل راهداری و حمل و نقل جاده ای استان مرکزی"))
        self.label_2.setText(_translate("MainWindow", "دفترچه تلفن"))
        self.pushButton.setText(_translate("MainWindow", "در خواست تغییرات"))
        self.pushButton_2.setText(_translate("MainWindow", "بروز رسانی"))
        self.pushButton_3.setToolTip(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.pushButton_3.setText(_translate("MainWindow", "درباره"))
import logo_rc



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
