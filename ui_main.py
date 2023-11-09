# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainui.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import resources

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(385, 300)
        MainWindow.setMinimumSize(QSize(385, 300))
        MainWindow.setMaximumSize(QSize(385, 300))
        MainWindow.setAcceptDrops(True)
        icon = QIcon()
        icon.addFile(u":/programm_icon/keyboard_FILL0_wght400_GRAD0_opsz24.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"    QWidget {\n"
"        background-color: black;\n"
"        font-family: Arial, Helvetica, sans-serif;\n"
"        font-style: oblique;\n"
"        color: aliceblue;\n"
"    }\n"
"\n"
"    QPushButton {\n"
"        border: 2px solid gray;\n"
"        border-radius: 5px;\n"
"        margin: 5px;\n"
"    }\n"
"\n"
"    QLineEdit {\n"
"        border: 2px solid grey;\n"
"        border-radius: 5px;\n"
"    }\n"
"\n"
"    QLineEdit:focus {\n"
"        border: 2px solid purple;\n"
"        border-radius: 5px;\n"
"    }\n"
"\n"
"    QLineEdit:hover {\n"
"        border: 2px solid purple;\n"
"        border-radius: 5px;\n"
"    }\n"
"\n"
"\n"
"    QPushButton#btn_status {\n"
"        padding: 5px;\n"
"        margin-left: 50px;\n"
"        margin-right: 50px;\n"
"    }\n"
"\n"
"    QPushButton:hover {\n"
"        border-color: purple;\n"
"    }\n"
"\n"
"    QPushButton:pressed {\n"
"        border: 3px solid purple;\n"
"        border-radius: 5px;\n"
"    }\n"
"\n"
"    QPushButton:checked {\n"
"        background"
                        "-color: darkmagenta;\n"
"        border-color: purple;\n"
"    }\n"
"\n"
"    QLabel#lbl_name,\n"
"    #lbl_version {\n"
"        color: white;\n"
"        font-family: sans-serif;\n"
"    }\n"
"\n"
"    QLabel#lbl_keyboard,\n"
"    #lbl_mouse {\n"
"        border-bottom: 3px solid grey;\n"
"        padding: 3px;\n"
"    }\n"
"\n"
"    QLabel#lbl_keyboard:hover,\n"
"    #lbl_mouse:hover {\n"
"        border-bottom: 3px solid purple;\n"
"        padding: 3px;\n"
"    }\n"
"\n"
"    QCheckBox::indicator {\n"
"        border: 2px solid grey;\n"
"        border-radius: 5px;\n"
"    }\n"
"\n"
"    QCheckBox::indicator:hover {\n"
"        border-color: purple;\n"
"    }\n"
"\n"
"    QCheckBox::indicator:pressed {\n"
"        border: 3px solid purple;\n"
"        border-radius: 5px;\n"
"    }\n"
"\n"
"    QCheckBox::indicator:checked {\n"
"        border: 2px solid purple;\n"
"        border-radius: 5px;\n"
"        background-color: darkmagenta\n"
"    }")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.ly_infoprg = QVBoxLayout()
        self.ly_infoprg.setObjectName(u"ly_infoprg")
        self.lbl_name = QLabel(self.centralwidget)
        self.lbl_name.setObjectName(u"lbl_name")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lbl_name.sizePolicy().hasHeightForWidth())
        self.lbl_name.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"sans-serif"])
        font.setBold(True)
        font.setItalic(True)
        self.lbl_name.setFont(font)
        self.lbl_name.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)

        self.ly_infoprg.addWidget(self.lbl_name)

        self.lbl_version = QLabel(self.centralwidget)
        self.lbl_version.setObjectName(u"lbl_version")
        sizePolicy.setHeightForWidth(self.lbl_version.sizePolicy().hasHeightForWidth())
        self.lbl_version.setSizePolicy(sizePolicy)
        self.lbl_version.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.ly_infoprg.addWidget(self.lbl_version)


        self.verticalLayout_5.addLayout(self.ly_infoprg)

        self.lbl_keyboard = QLabel(self.centralwidget)
        self.lbl_keyboard.setObjectName(u"lbl_keyboard")
        sizePolicy.setHeightForWidth(self.lbl_keyboard.sizePolicy().hasHeightForWidth())
        self.lbl_keyboard.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setBold(True)
        font1.setItalic(True)
        self.lbl_keyboard.setFont(font1)
        self.lbl_keyboard.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.lbl_keyboard)

        self.vl_keyboard = QVBoxLayout()
        self.vl_keyboard.setObjectName(u"vl_keyboard")
        self.hl_keyboard = QHBoxLayout()
        self.hl_keyboard.setObjectName(u"hl_keyboard")
        self.lbl_timesleep = QLabel(self.centralwidget)
        self.lbl_timesleep.setObjectName(u"lbl_timesleep")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lbl_timesleep.sizePolicy().hasHeightForWidth())
        self.lbl_timesleep.setSizePolicy(sizePolicy1)
        self.lbl_timesleep.setFont(font1)

        self.hl_keyboard.addWidget(self.lbl_timesleep)

        self.le_timesleep = QLineEdit(self.centralwidget)
        self.le_timesleep.setObjectName(u"le_timesleep")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.le_timesleep.sizePolicy().hasHeightForWidth())
        self.le_timesleep.setSizePolicy(sizePolicy2)
        self.le_timesleep.setMaxLength(5)

        self.hl_keyboard.addWidget(self.le_timesleep)

        self.lbl_keycode = QLabel(self.centralwidget)
        self.lbl_keycode.setObjectName(u"lbl_keycode")
        sizePolicy1.setHeightForWidth(self.lbl_keycode.sizePolicy().hasHeightForWidth())
        self.lbl_keycode.setSizePolicy(sizePolicy1)
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setBold(True)
        font2.setItalic(True)
        font2.setUnderline(False)
        font2.setKerning(True)
        self.lbl_keycode.setFont(font2)

        self.hl_keyboard.addWidget(self.lbl_keycode)

        self.le_keycode = QLineEdit(self.centralwidget)
        self.le_keycode.setObjectName(u"le_keycode")
        sizePolicy2.setHeightForWidth(self.le_keycode.sizePolicy().hasHeightForWidth())
        self.le_keycode.setSizePolicy(sizePolicy2)
        self.le_keycode.setMaxLength(1)

        self.hl_keyboard.addWidget(self.le_keycode)


        self.vl_keyboard.addLayout(self.hl_keyboard)


        self.verticalLayout_5.addLayout(self.vl_keyboard)

        self.lbl_mouse = QLabel(self.centralwidget)
        self.lbl_mouse.setObjectName(u"lbl_mouse")
        sizePolicy.setHeightForWidth(self.lbl_mouse.sizePolicy().hasHeightForWidth())
        self.lbl_mouse.setSizePolicy(sizePolicy)
        self.lbl_mouse.setFont(font1)
        self.lbl_mouse.setAlignment(Qt.AlignCenter)

        self.verticalLayout_5.addWidget(self.lbl_mouse)

        self.hl_mouse = QHBoxLayout()
        self.hl_mouse.setObjectName(u"hl_mouse")
        self.cb_mouseenable = QCheckBox(self.centralwidget)
        self.cb_mouseenable.setObjectName(u"cb_mouseenable")
        self.cb_mouseenable.setChecked(False)

        self.hl_mouse.addWidget(self.cb_mouseenable)

        self.lbl_coming = QLabel(self.centralwidget)
        self.lbl_coming.setObjectName(u"lbl_coming")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.lbl_coming.sizePolicy().hasHeightForWidth())
        self.lbl_coming.setSizePolicy(sizePolicy3)
        self.lbl_coming.setAlignment(Qt.AlignCenter)

        self.hl_mouse.addWidget(self.lbl_coming)


        self.verticalLayout_5.addLayout(self.hl_mouse)

        self.vl_status = QVBoxLayout()
        self.vl_status.setObjectName(u"vl_status")
        self.btn_status = QPushButton(self.centralwidget)
        self.btn_status.setObjectName(u"btn_status")
        sizePolicy2.setHeightForWidth(self.btn_status.sizePolicy().hasHeightForWidth())
        self.btn_status.setSizePolicy(sizePolicy2)
        self.btn_status.setStyleSheet(u"")
        self.btn_status.setCheckable(True)
        self.btn_status.setChecked(False)

        self.vl_status.addWidget(self.btn_status)


        self.verticalLayout_5.addLayout(self.vl_status)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Simple AutoClicker by ImHartash", None))
        self.lbl_name.setText(QCoreApplication.translate("MainWindow", u"Simple AutoClicker", None))
        self.lbl_version.setText(QCoreApplication.translate("MainWindow", u"v001", None))
        self.lbl_keyboard.setText(QCoreApplication.translate("MainWindow", u"KEYBOARD", None))
        self.lbl_timesleep.setText(QCoreApplication.translate("MainWindow", u"TimeSleep", None))
        self.le_timesleep.setInputMask("")
        self.le_timesleep.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Only digits and .", None))
        self.lbl_keycode.setText(QCoreApplication.translate("MainWindow", u"KeyCode", None))
        self.le_keycode.setPlaceholderText(QCoreApplication.translate("MainWindow", u"e", None))
        self.lbl_mouse.setText(QCoreApplication.translate("MainWindow", u"MOUSE", None))
        self.cb_mouseenable.setText(QCoreApplication.translate("MainWindow", u"Is Enable", None))
        self.lbl_coming.setText(QCoreApplication.translate("MainWindow", u"Coming Soon", None))
        self.btn_status.setText(QCoreApplication.translate("MainWindow", u"Start", None))
    # retranslateUi

