# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(696, 613)
        MainWindow.setStyleSheet(u"")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionQuit.setShortcutContext(Qt.WidgetShortcut)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frmMain = QFrame(self.centralwidget)
        self.frmMain.setObjectName(u"frmMain")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frmMain.sizePolicy().hasHeightForWidth())
        self.frmMain.setSizePolicy(sizePolicy)
        self.frmMain.setMinimumSize(QSize(0, 30))
        self.frmMain.setStyleSheet(u"background-color: rgb(27, 27, 27);\n"
"border-radius: 10px;")
        self.frmMain.setFrameShape(QFrame.StyledPanel)
        self.frmMain.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frmMain)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.stkPanel = QStackedWidget(self.frmMain)
        self.stkPanel.setObjectName(u"stkPanel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.stkPanel.sizePolicy().hasHeightForWidth())
        self.stkPanel.setSizePolicy(sizePolicy1)
        self.stkPanel.setStyleSheet(u"background-color: rgb(27, 27, 27);\n"
"border-radius: 10px;")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_3 = QGridLayout(self.page)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(200,200,200);\n"
"margin: 5px;")

        self.gridLayout_3.addWidget(self.label_3, 5, 1, 1, 1, Qt.AlignRight)

        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: rgb(200,200,200);\n"
"margin: 5px;")

        self.gridLayout_3.addWidget(self.label, 3, 1, 1, 1, Qt.AlignRight)

        self.txtServer = QLineEdit(self.page)
        self.txtServer.setObjectName(u"txtServer")
        self.txtServer.setStyleSheet(u"color: rgb(200,200,200);\n"
"border-radius: 10px;\n"
"border: 1px solid black;\n"
"background-color: rgb(15,15,15);\n"
"padding: 2px;\n"
"qproperty-alignment: 'AlignVCenter | AlignCenter';\n"
"margin: 5px;")

        self.gridLayout_3.addWidget(self.txtServer, 3, 2, 1, 1)

        self.txtUsername = QLineEdit(self.page)
        self.txtUsername.setObjectName(u"txtUsername")
        self.txtUsername.setStyleSheet(u"color: rgb(200,200,200);\n"
"border-radius: 10px;\n"
"border: 1px solid black;\n"
"background-color: rgb(15,15,15);\n"
"padding: 2px;\n"
"qproperty-alignment: 'AlignVCenter | AlignCenter';\n"
"margin: 5px;")

        self.gridLayout_3.addWidget(self.txtUsername, 5, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer, 8, 2, 1, 1)

        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(200,200,200);\n"
"margin: 5px;")

        self.gridLayout_3.addWidget(self.label_2, 4, 1, 1, 1, Qt.AlignRight)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 1, 2, 1, 1)

        self.btnLogin = QPushButton(self.page)
        self.btnLogin.setObjectName(u"btnLogin")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.btnLogin.sizePolicy().hasHeightForWidth())
        self.btnLogin.setSizePolicy(sizePolicy2)
        self.btnLogin.setMinimumSize(QSize(30, 30))
        self.btnLogin.setStyleSheet(u"#btnLogin {\n"
"	background-color: rgb(95, 95, 95);\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"	border: 1px solid black;\n"
"	margin: 5px;\n"
"}\n"
"\n"
"#btnLogin::hover {\n"
"	background-color: rgb(80, 80, 80);\n"
"}")

        self.gridLayout_3.addWidget(self.btnLogin, 6, 1, 1, 2)

        self.txtPort = QLineEdit(self.page)
        self.txtPort.setObjectName(u"txtPort")
        self.txtPort.setStyleSheet(u"color: rgb(200,200,200);\n"
"border-radius: 10px;\n"
"border: 1px solid black;\n"
"background-color: rgb(15,15,15);\n"
"padding: 2px;\n"
"qproperty-alignment: 'AlignVCenter | AlignCenter';\n"
"margin: 5px;")

        self.gridLayout_3.addWidget(self.txtPort, 4, 2, 1, 1)

        self.lblLoginError = QLabel(self.page)
        self.lblLoginError.setObjectName(u"lblLoginError")
        self.lblLoginError.setStyleSheet(u"color: red;\n"
"padding: 2px;\n"
"qproperty-alignment: 'AlignVCenter | AlignCenter';\n"
"margin: 5px;\n"
"")

        self.gridLayout_3.addWidget(self.lblLoginError, 7, 1, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_2, 5, 3, 1, 1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer, 5, 0, 1, 1)

        self.stkPanel.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout = QGridLayout(self.page_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.btnSend = QPushButton(self.page_2)
        self.btnSend.setObjectName(u"btnSend")
        sizePolicy3 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btnSend.sizePolicy().hasHeightForWidth())
        self.btnSend.setSizePolicy(sizePolicy3)
        self.btnSend.setMinimumSize(QSize(50, 20))
        self.btnSend.setFocusPolicy(Qt.NoFocus)
        self.btnSend.setStyleSheet(u"#btnSend {\n"
"	background-color: rgb(95, 95, 95);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"#btnSend::hover {\n"
"	background-color: rgb(80, 80, 80);\n"
"}\n"
"")

        self.gridLayout.addWidget(self.btnSend, 2, 1, 1, 1)

        self.txtChat = QTextEdit(self.page_2)
        self.txtChat.setObjectName(u"txtChat")
        self.txtChat.setStyleSheet(u"color: rgb(198, 198, 198);\n"
"border: 1px solid rgb(15,15,15);\n"
"border-radius: 10px;\n"
"padding: 10px;")
        self.txtChat.setReadOnly(True)

        self.gridLayout.addWidget(self.txtChat, 1, 0, 1, 2)

        self.txtInput = QLineEdit(self.page_2)
        self.txtInput.setObjectName(u"txtInput")
        self.txtInput.setMinimumSize(QSize(0, 40))
        self.txtInput.setStyleSheet(u"background-color: rgb(12, 12, 12);\n"
"color: rgb(198, 198, 198);\n"
"border-radius: 10px;\n"
"padding: 5px;")

        self.gridLayout.addWidget(self.txtInput, 2, 0, 1, 1)

        self.stkPanel.addWidget(self.page_2)

        self.gridLayout_4.addWidget(self.stkPanel, 3, 0, 1, 4)

        self.btnExit = QPushButton(self.frmMain)
        self.btnExit.setObjectName(u"btnExit")
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.btnExit.sizePolicy().hasHeightForWidth())
        self.btnExit.setSizePolicy(sizePolicy4)
        self.btnExit.setMinimumSize(QSize(20, 20))
        self.btnExit.setMaximumSize(QSize(20, 20))
        self.btnExit.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid rgb(150,0,0);\n"
"background-color: rgb(255,0,0)")

        self.gridLayout_4.addWidget(self.btnExit, 0, 3, 1, 1, Qt.AlignTop)

        self.lblAppName = QLabel(self.frmMain)
        self.lblAppName.setObjectName(u"lblAppName")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.lblAppName.sizePolicy().hasHeightForWidth())
        self.lblAppName.setSizePolicy(sizePolicy5)
        font = QFont()
        font.setPointSize(30)
        self.lblAppName.setFont(font)
        self.lblAppName.setStyleSheet(u"color: rgb(200,200,200);")

        self.gridLayout_4.addWidget(self.lblAppName, 0, 0, 1, 2, Qt.AlignHCenter)

        self.btnMinimize = QPushButton(self.frmMain)
        self.btnMinimize.setObjectName(u"btnMinimize")
        sizePolicy4.setHeightForWidth(self.btnMinimize.sizePolicy().hasHeightForWidth())
        self.btnMinimize.setSizePolicy(sizePolicy4)
        self.btnMinimize.setMinimumSize(QSize(20, 20))
        self.btnMinimize.setMaximumSize(QSize(20, 20))
        self.btnMinimize.setStyleSheet(u"border-radius: 10px;\n"
"border: 2px solid rgb(150,150,0);\n"
"background-color: rgb(255,255,0)")

        self.gridLayout_4.addWidget(self.btnMinimize, 0, 2, 1, 1, Qt.AlignTop)


        self.gridLayout_2.addWidget(self.frmMain, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stkPanel.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Chat", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Username: ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Server: ", None))
        self.txtServer.setText(QCoreApplication.translate("MainWindow", u"127.0.0.1", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Port: ", None))
        self.btnLogin.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.txtPort.setText(QCoreApplication.translate("MainWindow", u"55555", None))
        self.lblLoginError.setText("")
        self.btnSend.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.btnExit.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.lblAppName.setText(QCoreApplication.translate("MainWindow", u"    Chatr", None))
        self.btnMinimize.setText(QCoreApplication.translate("MainWindow", u"\u2212", None))
    # retranslateUi

