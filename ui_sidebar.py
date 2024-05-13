# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1099, 847)
        MainWindow.setStyleSheet(u"background-color: \n"
"rgb(15, 19, 27);\n"
"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 0, 2, 2))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")

        self.gridLayout.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)

        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"background-color: rgb(22, 23, 26);}\n"
"QPushButton{\n"
"color: white;\n"
"height: 30px;\n"
"border:none;\n"
"}\n"
"")
        self.verticalLayout_3 = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.icon_name_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(30, 30))
        self.label.setMaximumSize(QSize(30, 30))
        self.label.setPixmap(QPixmap(u":/images/dashboard.png"))
        self.label.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.label)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(45)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 30, -1, -1)
        self.dashboard_1 = QPushButton(self.icon_name_widget)
        self.dashboard_1.setObjectName(u"dashboard_1")
        icon = QIcon()
        icon.addFile(u":/images/520-5203406_marqueur-google-map-icon-hd-png-download-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard_1.setIcon(icon)
        self.dashboard_1.setCheckable(True)
        self.dashboard_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.dashboard_1)

        self.reports_1 = QPushButton(self.icon_name_widget)
        self.reports_1.setObjectName(u"reports_1")
        icon1 = QIcon()
        icon1.addFile(u":/images/view-details-xxl-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reports_1.setIcon(icon1)
        self.reports_1.setCheckable(True)
        self.reports_1.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.reports_1)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer = QSpacerItem(20, 527, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)

        self.pushButton_6 = QPushButton(self.icon_name_widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon2 = QIcon()
        icon2.addFile(u":/images/log_out.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pushButton_6)


        self.gridLayout.addWidget(self.icon_name_widget, 1, 1, 1, 1)

        self.icon_only_widget = QWidget(self.centralwidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.verticalLayout_5 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.heade_widget = QWidget(self.icon_only_widget)
        self.heade_widget.setObjectName(u"heade_widget")
        self.horizontalLayout_6 = QHBoxLayout(self.heade_widget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 9, -1, -1)
        self.menu = QPushButton(self.heade_widget)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"border: none;")
        icon3 = QIcon()
        icon3.addFile(u":/images/535146.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu.setIcon(icon3)
        self.menu.setIconSize(QSize(20, 20))
        self.menu.setCheckable(True)

        self.horizontalLayout_6.addWidget(self.menu)

        self.horizontalSpacer = QSpacerItem(253, 17, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.lineEdit = QLineEdit(self.heade_widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"background-color: rgb(15, 19, 27);\n"
"background-color: rgb(64, 62, 62);\n"
"background-color: rgb(22, 23, 26);\n"
"")

        self.horizontalLayout_6.addWidget(self.lineEdit)

        self.pushButton_14 = QPushButton(self.heade_widget)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setStyleSheet(u"border:none;")
        icon4 = QIcon()
        icon4.addFile(u":/images/ser.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_14.setIcon(icon4)

        self.horizontalLayout_6.addWidget(self.pushButton_14)

        self.horizontalSpacer_2 = QSpacerItem(253, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addWidget(self.heade_widget)

        self.stackedWidget = QStackedWidget(self.icon_only_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"background-color: rgb(15, 19, 27);\n"
"background-color: rgb(220, 138, 221);\n"
"background-color: rgb(15, 19, 27);\n"
"\n"
"")
        self.Dashboard_page = QWidget()
        self.Dashboard_page.setObjectName(u"Dashboard_page")
        self.label_4 = QLabel(self.Dashboard_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(310, 250, 291, 151))
        font = QFont()
        font.setPointSize(25)
        self.label_4.setFont(font)
        self.stackedWidget.addWidget(self.Dashboard_page)
        self.Notifications_page = QWidget()
        self.Notifications_page.setObjectName(u"Notifications_page")
        self.stackedWidget.addWidget(self.Notifications_page)
        self.Reports_page = QWidget()
        self.Reports_page.setObjectName(u"Reports_page")
        self.label_6 = QLabel(self.Reports_page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 70, 271, 61))
        font1 = QFont()
        font1.setPointSize(25)
        font1.setBold(True)
        self.label_6.setFont(font1)
        self.tableWidget = QTableWidget(self.Reports_page)
        if (self.tableWidget.columnCount() < 3):
            self.tableWidget.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.tableWidget.rowCount() < 1):
            self.tableWidget.setRowCount(1)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem5)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(40, 140, 801, 551))
        self.tableWidget.setMaximumSize(QSize(801, 16777215))
        self.tableWidget.setStyleSheet(u"QHeaderView::section{\n"
"font-weight: bold;\n"
"background-color: rgb(15, 19, 27);\n"
"\n"
"\n"
"}\n"
"QTableWidget{\n"
"	alternate-background-color:  rgb(15, 19, 27);\n"
"	background-color: rgb(22, 23, 26);\n"
"\n"
"}\n"
"")
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(57)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(270)
        self.tableWidget.verticalHeader().setMinimumSectionSize(21)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)
        self.stackedWidget.addWidget(self.Reports_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout.addWidget(self.icon_only_widget, 1, 3, 1, 1)

        self.main_menu = QWidget(self.centralwidget)
        self.main_menu.setObjectName(u"main_menu")
        self.main_menu.setStyleSheet(u"QWidget{\n"
"background-color: rgb(22, 23, 26);}\n"
"QPushButton{\n"
"color: white;\n"
"text-align: left;\n"
"height: 30px;\n"
"border:none;\n"
"padding-left:10px;\n"
"border-top-left-radius:10px;\n"
"border-bottom-left-radius:10px;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"background: rgb(15, 19, 27);\n"
"font-weigth: bold;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.main_menu)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, 0, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 20, -1)
        self.label_2 = QLabel(self.main_menu)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(30, 30))
        self.label_2.setMaximumSize(QSize(30, 30))
        self.label_2.setPixmap(QPixmap(u":/images/dashboard.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.main_menu)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_3.setFont(font2)

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(45)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 30, -1, -1)
        self.dashboard_2 = QPushButton(self.main_menu)
        self.dashboard_2.setObjectName(u"dashboard_2")
        self.dashboard_2.setIcon(icon)
        self.dashboard_2.setCheckable(True)
        self.dashboard_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.dashboard_2)

        self.reports_2 = QPushButton(self.main_menu)
        self.reports_2.setObjectName(u"reports_2")
        self.reports_2.setIcon(icon1)
        self.reports_2.setCheckable(True)
        self.reports_2.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.reports_2)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 338, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.pushButton_12 = QPushButton(self.main_menu)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setIcon(icon2)
        self.pushButton_12.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pushButton_12)


        self.gridLayout.addWidget(self.main_menu, 1, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu.toggled.connect(self.icon_name_widget.setHidden)
        self.menu.toggled.connect(self.main_menu.setVisible)
        self.reports_1.toggled.connect(self.reports_2.setChecked)
        self.dashboard_1.toggled.connect(self.dashboard_2.setChecked)
        self.dashboard_2.toggled.connect(self.dashboard_1.setChecked)
        self.reports_2.toggled.connect(self.reports_1.setChecked)
        self.pushButton_6.toggled.connect(MainWindow.close)
        self.pushButton_12.toggled.connect(MainWindow.close)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText("")
        self.dashboard_1.setText("")
        self.reports_1.setText("")
        self.pushButton_6.setText("")
        self.menu.setText("")
        self.pushButton_14.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Dashboard page", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Recent accidents", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Info", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Action", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem3 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Accident 1", None));
        ___qtablewidgetitem4 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"pending", None));
        ___qtablewidgetitem5 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"None", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"MyPanel", None))
        self.dashboard_2.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.reports_2.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u" Shut down", None))
    # retranslateUi

