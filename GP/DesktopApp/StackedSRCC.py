# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\StackedSRCC.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_StackedWidget(object):
    def setupUi(self, StackedWidget):
        StackedWidget.setObjectName(_fromUtf8("StackedWidget"))
        StackedWidget.resize(566, 395)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../Fifa_Logo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        StackedWidget.setWindowIcon(icon)
        StackedWidget.setStyleSheet(_fromUtf8("QToolTip\n"
"{\n"
"     border: 1px solid black;\n"
"     background-color: #ffa02f;\n"
"     padding: 1px;\n"
"     border-radius: 3px;\n"
"     opacity: 100;\n"
"}\n"
"\n"
"QWidget\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QWidget:item:hover\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #ca0619);\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:item:selected\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QMenuBar::item\n"
"{\n"
"    background: transparent;\n"
"}\n"
"\n"
"QMenuBar::item:selected\n"
"{\n"
"    background: transparent;\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QMenuBar::item:pressed\n"
"{\n"
"    background: #444;\n"
"    border: 1px solid #000;\n"
"    background-color: QLinearGradient(\n"
"        x1:0, y1:0,\n"
"        x2:0, y2:1,\n"
"        stop:1 #212121,\n"
"        stop:0.4 #343434/*,\n"
"        stop:0.2 #343434,\n"
"        stop:0.1 #ffaa00*/\n"
"    );\n"
"    margin-bottom:-1px;\n"
"    padding-bottom:1px;\n"
"}\n"
"\n"
"QMenu\n"
"{\n"
"    border: 1px solid #000;\n"
"}\n"
"\n"
"QMenu::item\n"
"{\n"
"    padding: 2px 20px 2px 20px;\n"
"}\n"
"\n"
"QMenu::item:selected\n"
"{\n"
"    color: #000000;\n"
"}\n"
"\n"
"QWidget:disabled\n"
"{\n"
"    color: #404040;\n"
"    background-color: #323232;\n"
"}\n"
"\n"
"QAbstractItemView\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0.1 #646464, stop: 1 #5d5d5d);\n"
"}\n"
"\n"
"QWidget:focus\n"
"{\n"
"    /*border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);*/\n"
"}\n"
"\n"
"QLineEdit\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #4d4d4d, stop: 0 #646464, stop: 1 #5d5d5d);\n"
"    padding: 1px;\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #b1b1b1;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 6;\n"
"    padding: 3px;\n"
"    font-size: 12px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"}\n"
"\n"
"QComboBox\n"
"{\n"
"    selection-background-color: #ffaa00;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #565656, stop: 0.1 #525252, stop: 0.5 #4e4e4e, stop: 0.9 #4a4a4a, stop: 1 #464646);\n"
"    border-style: solid;\n"
"    border: 1px solid #1e1e1e;\n"
"    border-radius: 5;\n"
"}\n"
"\n"
"QComboBox:hover,QPushButton:hover\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"\n"
"QComboBox:on\n"
"{\n"
"    padding-top: 3px;\n"
"    padding-left: 4px;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #2d2d2d, stop: 0.1 #2b2b2b, stop: 0.5 #292929, stop: 0.9 #282828, stop: 1 #252525);\n"
"    selection-background-color: #ffaa00;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView\n"
"{\n"
"    border: 2px solid darkgray;\n"
"    selection-background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QComboBox::drop-down\n"
"{\n"
"     subcontrol-origin: padding;\n"
"     subcontrol-position: top right;\n"
"     width: 15px;\n"
"\n"
"     border-left-width: 0px;\n"
"     border-left-color: darkgray;\n"
"     border-left-style: solid; /* just a single line */\n"
"     border-top-right-radius: 3px; /* same radius as the QComboBox */\n"
"     border-bottom-right-radius: 3px;\n"
" }\n"
"\n"
"QComboBox::down-arrow\n"
"{\n"
"     image: url(:/down_arrow.png);\n"
"}\n"
"\n"
"QGroupBox:focus\n"
"{\n"
"border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QTextEdit:focus\n"
"{\n"
"    border: 2px solid QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"     border: 1px solid #222222;\n"
"     background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"     height: 7px;\n"
"     margin: 0px 16px 0 16px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"      subcontrol-position: right;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      width: 14px;\n"
"     subcontrol-position: left;\n"
"     subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::right-arrow:horizontal, QScrollBar::left-arrow:horizontal\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QScrollBar:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 1, y2: 0, stop: 0.0 #121212, stop: 0.2 #282828, stop: 1 #484848);\n"
"      width: 7px;\n"
"      margin: 16px 0 16px 0;\n"
"      border: 1px solid #222222;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical\n"
"{\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 0.5 #d7801a, stop: 1 #ffa02f);\n"
"      min-height: 20px;\n"
"      border-radius: 2px;\n"
"}\n"
"\n"
"QScrollBar::add-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffa02f, stop: 1 #d7801a);\n"
"      height: 14px;\n"
"      subcontrol-position: bottom;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical\n"
"{\n"
"      border: 1px solid #1b1b19;\n"
"      border-radius: 2px;\n"
"      background: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #d7801a, stop: 1 #ffa02f);\n"
"      height: 14px;\n"
"      subcontrol-position: top;\n"
"      subcontrol-origin: margin;\n"
"}\n"
"\n"
"QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical\n"
"{\n"
"      border: 1px solid black;\n"
"      width: 1px;\n"
"      height: 1px;\n"
"      background: white;\n"
"}\n"
"\n"
"\n"
"QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical\n"
"{\n"
"      background: none;\n"
"}\n"
"\n"
"QTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QPlainTextEdit\n"
"{\n"
"    background-color: #242424;\n"
"}\n"
"\n"
"QHeaderView::section\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #616161, stop: 0.5 #505050, stop: 0.6 #434343, stop:1 #656565);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"}\n"
"\n"
"QCheckBox:disabled\n"
"{\n"
"color: #414141;\n"
"}\n"
"\n"
"QDockWidget::title\n"
"{\n"
"    text-align: center;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button, QDockWidget::float-button\n"
"{\n"
"    text-align: center;\n"
"    spacing: 1px; /* spacing between items in the tool bar */\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #323232, stop: 0.5 #242424, stop:1 #323232);\n"
"}\n"
"\n"
"QDockWidget::close-button:hover, QDockWidget::float-button:hover\n"
"{\n"
"    background: #242424;\n"
"}\n"
"\n"
"QDockWidget::close-button:pressed, QDockWidget::float-button:pressed\n"
"{\n"
"    padding: 1px -1px -1px 1px;\n"
"}\n"
"\n"
"QMainWindow::separator\n"
"{\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #4c4c4c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QMainWindow::separator:hover\n"
"{\n"
"\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #d7801a, stop:0.5 #b56c17 stop:1 #ffa02f);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    border: 1px solid #6c6c6c;\n"
"    spacing: 3px; /* spacing between items in the tool bar */\n"
"}\n"
"\n"
"QToolBar::handle\n"
"{\n"
"     spacing: 3px; /* spacing between items in the tool bar */\n"
"     background: url(:/images/handle.png);\n"
"}\n"
"\n"
"QMenu::separator\n"
"{\n"
"    height: 2px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:0 #161616, stop: 0.5 #151515, stop: 0.6 #212121, stop:1 #343434);\n"
"    color: white;\n"
"    padding-left: 4px;\n"
"    margin-left: 10px;\n"
"    margin-right: 5px;\n"
"}\n"
"\n"
"QProgressBar\n"
"{\n"
"    border: 2px solid grey;\n"
"    border-radius: 5px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"QProgressBar::chunk\n"
"{\n"
"    background-color: #d7801a;\n"
"    width: 2.15px;\n"
"    margin: 0.5px;\n"
"}\n"
"\n"
"QTabBar::tab {\n"
"    color: #b1b1b1;\n"
"    border: 1px solid #444;\n"
"    border-bottom-style: none;\n"
"    background-color: #323232;\n"
"    padding-left: 10px;\n"
"    padding-right: 10px;\n"
"    padding-top: 3px;\n"
"    padding-bottom: 2px;\n"
"    margin-right: -1px;\n"
"}\n"
"\n"
"QTabWidget::pane {\n"
"    border: 1px solid #444;\n"
"    top: 1px;\n"
"}\n"
"\n"
"QTabBar::tab:last\n"
"{\n"
"    margin-right: 0; /* the last selected tab has nothing to overlap with on the right */\n"
"    border-top-right-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:first:!selected\n"
"{\n"
" margin-left: 0px; /* the last selected tab has nothing to overlap with on the right */\n"
"\n"
"\n"
"    border-top-left-radius: 3px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected\n"
"{\n"
"    color: #b1b1b1;\n"
"    border-bottom-style: solid;\n"
"    margin-top: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:.4 #343434);\n"
"}\n"
"\n"
"QTabBar::tab:selected\n"
"{\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    margin-bottom: 0px;\n"
"}\n"
"\n"
"QTabBar::tab:!selected:hover\n"
"{\n"
"    /*border-top: 2px solid #ffaa00;\n"
"    padding-bottom: 3px;*/\n"
"    border-top-left-radius: 3px;\n"
"    border-top-right-radius: 3px;\n"
"    background-color: QLinearGradient(x1:0, y1:0, x2:0, y2:1, stop:1 #212121, stop:0.4 #343434, stop:0.2 #343434, stop:0.1 #ffaa00);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked, QRadioButton::indicator:unchecked{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:checked\n"
"{\n"
"    background-color: qradialgradient(\n"
"        cx: 0.5, cy: 0.5,\n"
"        fx: 0.5, fy: 0.5,\n"
"        radius: 1.0,\n"
"        stop: 0.25 #ffaa00,\n"
"        stop: 0.3 #323232\n"
"    );\n"
"}\n"
"\n"
"QCheckBox::indicator{\n"
"    color: #b1b1b1;\n"
"    background-color: #323232;\n"
"    border: 1px solid #b1b1b1;\n"
"    width: 9px;\n"
"    height: 9px;\n"
"}\n"
"\n"
"QRadioButton::indicator\n"
"{\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QRadioButton::indicator:hover, QCheckBox::indicator:hover\n"
"{\n"
"    border: 1px solid #ffaa00;\n"
"}\n"
"\n"
"QCheckBox::indicator:checked\n"
"{\n"
"    image:url(:/images/checkbox.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:disabled, QRadioButton::indicator:disabled\n"
"{\n"
"    border: 1px solid #444;\n"
"}"))
        self.TeamPage = QtGui.QWidget()
        self.TeamPage.setObjectName(_fromUtf8("TeamPage"))
        self.Title_TeamPage = QtGui.QLabel(self.TeamPage)
        self.Title_TeamPage.setGeometry(QtCore.QRect(120, 0, 351, 101))
        self.Title_TeamPage.setObjectName(_fromUtf8("Title_TeamPage"))
        self.FTNT = QtGui.QLabel(self.TeamPage)
        self.FTNT.setGeometry(QtCore.QRect(30, 120, 231, 31))
        self.FTNT.setObjectName(_fromUtf8("FTNT"))
        self.STNL = QtGui.QLineEdit(self.TeamPage)
        self.STNL.setGeometry(QtCore.QRect(290, 180, 231, 31))
        self.STNL.setStyleSheet(_fromUtf8("font: 14pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.STNL.setObjectName(_fromUtf8("STNL"))
        self.STNT = QtGui.QLabel(self.TeamPage)
        self.STNT.setGeometry(QtCore.QRect(30, 180, 251, 31))
        self.STNT.setObjectName(_fromUtf8("STNT"))
        self.FTNL = QtGui.QLineEdit(self.TeamPage)
        self.FTNL.setGeometry(QtCore.QRect(290, 120, 231, 31))
        self.FTNL.setStyleSheet(_fromUtf8("font: 14pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.FTNL.setObjectName(_fromUtf8("FTNL"))
        self.Back = QtGui.QPushButton(self.TeamPage)
        self.Back.setGeometry(QtCore.QRect(50, 280, 211, 41))
        self.Back.setStyleSheet(_fromUtf8("font: 19pt \"MS Shell Dlg 2\";"))
        self.Back.setObjectName(_fromUtf8("Back"))
        self.Next = QtGui.QPushButton(self.TeamPage)
        self.Next.setGeometry(QtCore.QRect(320, 280, 211, 41))
        self.Next.setStyleSheet(_fromUtf8("font: 19pt \"MS Shell Dlg 2\";"))
        self.Next.setObjectName(_fromUtf8("Next"))
        StackedWidget.addWidget(self.TeamPage)
        self.ConnectPage = QtGui.QWidget()
        self.ConnectPage.setObjectName(_fromUtf8("ConnectPage"))
        self.IP = QtGui.QLineEdit(self.ConnectPage)
        self.IP.setGeometry(QtCore.QRect(280, 120, 231, 31))
        self.IP.setStyleSheet(_fromUtf8("font: 14pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.IP.setObjectName(_fromUtf8("IP"))
        self.Port = QtGui.QLineEdit(self.ConnectPage)
        self.Port.setGeometry(QtCore.QRect(280, 180, 231, 31))
        self.Port.setStyleSheet(_fromUtf8("font: 14pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.Port.setObjectName(_fromUtf8("Port"))
        self.Title = QtGui.QLabel(self.ConnectPage)
        self.Title.setGeometry(QtCore.QRect(110, 10, 351, 101))
        self.Title.setObjectName(_fromUtf8("Title"))
        self.ConnectionError = QtGui.QLabel(self.ConnectPage)
        self.ConnectionError.setGeometry(QtCore.QRect(120, 250, 391, 41))
        self.ConnectionError.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);\n"
"font: 28pt \"MS Shell Dlg 2\";"))
        self.ConnectionError.setObjectName(_fromUtf8("ConnectionError"))
        self.Port_Title = QtGui.QLabel(self.ConnectPage)
        self.Port_Title.setGeometry(QtCore.QRect(20, 180, 231, 31))
        self.Port_Title.setObjectName(_fromUtf8("Port_Title"))
        self.ConnectButton = QtGui.QPushButton(self.ConnectPage)
        self.ConnectButton.setGeometry(QtCore.QRect(370, 330, 131, 41))
        self.ConnectButton.setStyleSheet(_fromUtf8("font: 19pt \"MS Shell Dlg 2\";"))
        self.ConnectButton.setObjectName(_fromUtf8("ConnectButton"))
        self.IP_Title = QtGui.QLabel(self.ConnectPage)
        self.IP_Title.setGeometry(QtCore.QRect(20, 120, 231, 31))
        self.IP_Title.setObjectName(_fromUtf8("IP_Title"))
        self.StateT = QtGui.QLabel(self.ConnectPage)
        self.StateT.setGeometry(QtCore.QRect(20, 250, 81, 41))
        self.StateT.setObjectName(_fromUtf8("StateT"))
        self.BTOMM = QtGui.QPushButton(self.ConnectPage)
        self.BTOMM.setGeometry(QtCore.QRect(70, 330, 131, 41))
        self.BTOMM.setStyleSheet(_fromUtf8("font: 19pt \"MS Shell Dlg 2\";"))
        self.BTOMM.setObjectName(_fromUtf8("BTOMM"))
        StackedWidget.addWidget(self.ConnectPage)
        self.Main_Page = QtGui.QWidget()
        self.Main_Page.setObjectName(_fromUtf8("Main_Page"))
        self.MMLabel = QtGui.QLabel(self.Main_Page)
        self.MMLabel.setGeometry(QtCore.QRect(110, 10, 351, 41))
        self.MMLabel.setObjectName(_fromUtf8("MMLabel"))
        self.ANCButton = QtGui.QPushButton(self.Main_Page)
        self.ANCButton.setGeometry(QtCore.QRect(60, 90, 161, 61))
        self.ANCButton.setStyleSheet(_fromUtf8("font: 12pt \"MS Shell Dlg 2\";"))
        self.ANCButton.setObjectName(_fromUtf8("ANCButton"))
        self.SCButton = QtGui.QPushButton(self.Main_Page)
        self.SCButton.setGeometry(QtCore.QRect(350, 90, 161, 61))
        self.SCButton.setStyleSheet(_fromUtf8("font: 12pt \"MS Shell Dlg 2\";"))
        self.SCButton.setObjectName(_fromUtf8("SCButton"))
        self.MMButton = QtGui.QPushButton(self.Main_Page)
        self.MMButton.setGeometry(QtCore.QRect(60, 280, 161, 61))
        self.MMButton.setStyleSheet(_fromUtf8("font: 12pt \"MS Shell Dlg 2\";"))
        self.MMButton.setObjectName(_fromUtf8("MMButton"))
        self.VLTButton = QtGui.QPushButton(self.Main_Page)
        self.VLTButton.setGeometry(QtCore.QRect(350, 280, 161, 61))
        self.VLTButton.setStyleSheet(_fromUtf8("font: 12pt \"MS Shell Dlg 2\";"))
        self.VLTButton.setObjectName(_fromUtf8("VLTButton"))
        self.ANTButton = QtGui.QPushButton(self.Main_Page)
        self.ANTButton.setGeometry(QtCore.QRect(60, 190, 161, 61))
        self.ANTButton.setStyleSheet(_fromUtf8("font: 12pt \"MS Shell Dlg 2\";"))
        self.ANTButton.setObjectName(_fromUtf8("ANTButton"))
        self.TMButton = QtGui.QPushButton(self.Main_Page)
        self.TMButton.setGeometry(QtCore.QRect(350, 190, 161, 61))
        self.TMButton.setStyleSheet(_fromUtf8("font: 12pt \"MS Shell Dlg 2\";"))
        self.TMButton.setObjectName(_fromUtf8("TMButton"))
        StackedWidget.addWidget(self.Main_Page)
        self.CardSelectPage = QtGui.QWidget()
        self.CardSelectPage.setObjectName(_fromUtf8("CardSelectPage"))
        self.MMLabel_3 = QtGui.QLabel(self.CardSelectPage)
        self.MMLabel_3.setGeometry(QtCore.QRect(110, 10, 361, 41))
        self.MMLabel_3.setObjectName(_fromUtf8("MMLabel_3"))
        self.NamesComboBox = QtGui.QComboBox(self.CardSelectPage)
        self.NamesComboBox.setGeometry(QtCore.QRect(210, 60, 191, 41))
        self.NamesComboBox.setStyleSheet(_fromUtf8("font: 12pt \"MS Shell Dlg 2\";"))
        self.NamesComboBox.setObjectName(_fromUtf8("NamesComboBox"))
        self.label = QtGui.QLabel(self.CardSelectPage)
        self.label.setGeometry(QtCore.QRect(30, 60, 161, 41))
        self.label.setStyleSheet(_fromUtf8("font: 20pt \"MS Shell Dlg 2\";"))
        self.label.setObjectName(_fromUtf8("label"))
        self.ShowIPPORT = QtGui.QPushButton(self.CardSelectPage)
        self.ShowIPPORT.setGeometry(QtCore.QRect(440, 60, 81, 41))
        self.ShowIPPORT.setStyleSheet(_fromUtf8("font: 20pt \"MS Shell Dlg 2\";"))
        self.ShowIPPORT.setObjectName(_fromUtf8("ShowIPPORT"))
        self.CardIP = QtGui.QLineEdit(self.CardSelectPage)
        self.CardIP.setEnabled(False)
        self.CardIP.setGeometry(QtCore.QRect(270, 130, 231, 31))
        self.CardIP.setStyleSheet(_fromUtf8("font: 14pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.CardIP.setObjectName(_fromUtf8("CardIP"))
        self.CardPort = QtGui.QLineEdit(self.CardSelectPage)
        self.CardPort.setEnabled(False)
        self.CardPort.setGeometry(QtCore.QRect(270, 190, 231, 31))
        self.CardPort.setStyleSheet(_fromUtf8("font: 14pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.CardPort.setObjectName(_fromUtf8("CardPort"))
        self.Port_Title_4 = QtGui.QLabel(self.CardSelectPage)
        self.Port_Title_4.setGeometry(QtCore.QRect(30, 190, 231, 31))
        self.Port_Title_4.setObjectName(_fromUtf8("Port_Title_4"))
        self.IP_Title_6 = QtGui.QLabel(self.CardSelectPage)
        self.IP_Title_6.setGeometry(QtCore.QRect(30, 130, 211, 31))
        self.IP_Title_6.setObjectName(_fromUtf8("IP_Title_6"))
        self.ApplyEdit = QtGui.QPushButton(self.CardSelectPage)
        self.ApplyEdit.setGeometry(QtCore.QRect(400, 250, 131, 41))
        self.ApplyEdit.setStyleSheet(_fromUtf8("font: 19pt \"MS Shell Dlg 2\";"))
        self.ApplyEdit.setObjectName(_fromUtf8("ApplyEdit"))
        self.BTOMMSAC = QtGui.QPushButton(self.CardSelectPage)
        self.BTOMMSAC.setGeometry(QtCore.QRect(60, 250, 131, 41))
        self.BTOMMSAC.setStyleSheet(_fromUtf8("font: 19pt \"MS Shell Dlg 2\";"))
        self.BTOMMSAC.setObjectName(_fromUtf8("BTOMMSAC"))
        self.EditIPPORT = QtGui.QPushButton(self.CardSelectPage)
        self.EditIPPORT.setGeometry(QtCore.QRect(230, 250, 131, 41))
        self.EditIPPORT.setStyleSheet(_fromUtf8("font: 19pt \"MS Shell Dlg 2\";"))
        self.EditIPPORT.setObjectName(_fromUtf8("EditIPPORT"))
        self.ConnectToCard = QtGui.QPushButton(self.CardSelectPage)
        self.ConnectToCard.setGeometry(QtCore.QRect(230, 320, 131, 41))
        self.ConnectToCard.setStyleSheet(_fromUtf8("font: 19pt \"MS Shell Dlg 2\";"))
        self.ConnectToCard.setObjectName(_fromUtf8("ConnectToCard"))
        StackedWidget.addWidget(self.CardSelectPage)
        self.LeagueTablePage = QtGui.QWidget()
        self.LeagueTablePage.setObjectName(_fromUtf8("LeagueTablePage"))
        self.MMLabel_2 = QtGui.QLabel(self.LeagueTablePage)
        self.MMLabel_2.setGeometry(QtCore.QRect(100, 0, 351, 41))
        self.MMLabel_2.setObjectName(_fromUtf8("MMLabel_2"))
        self.LeagueBack = QtGui.QPushButton(self.LeagueTablePage)
        self.LeagueBack.setGeometry(QtCore.QRect(10, 10, 75, 31))
        self.LeagueBack.setObjectName(_fromUtf8("LeagueBack"))
        StackedWidget.addWidget(self.LeagueTablePage)
        self.SelectTeam = QtGui.QWidget()
        self.SelectTeam.setObjectName(_fromUtf8("SelectTeam"))
        self.SelectTeamButton = QtGui.QPushButton(self.SelectTeam)
        self.SelectTeamButton.setGeometry(QtCore.QRect(440, 60, 81, 41))
        self.SelectTeamButton.setStyleSheet(_fromUtf8("font: 20pt \"MS Shell Dlg 2\";"))
        self.SelectTeamButton.setObjectName(_fromUtf8("SelectTeamButton"))
        self.MMLabel_4 = QtGui.QLabel(self.SelectTeam)
        self.MMLabel_4.setGeometry(QtCore.QRect(110, 10, 361, 41))
        self.MMLabel_4.setObjectName(_fromUtf8("MMLabel_4"))
        self.TeamNamesCombo = QtGui.QComboBox(self.SelectTeam)
        self.TeamNamesCombo.setGeometry(QtCore.QRect(210, 60, 191, 41))
        self.TeamNamesCombo.setStyleSheet(_fromUtf8("font: 12pt \"MS Shell Dlg 2\";"))
        self.TeamNamesCombo.setObjectName(_fromUtf8("TeamNamesCombo"))
        self.SelectTeamLabel = QtGui.QLabel(self.SelectTeam)
        self.SelectTeamLabel.setGeometry(QtCore.QRect(30, 60, 171, 41))
        self.SelectTeamLabel.setStyleSheet(_fromUtf8("font: 20pt \"MS Shell Dlg 2\";"))
        self.SelectTeamLabel.setObjectName(_fromUtf8("SelectTeamLabel"))
        self.IP_Title_7 = QtGui.QLabel(self.SelectTeam)
        self.IP_Title_7.setGeometry(QtCore.QRect(20, 110, 201, 41))
        self.IP_Title_7.setObjectName(_fromUtf8("IP_Title_7"))
        self.BTOSC = QtGui.QPushButton(self.SelectTeam)
        self.BTOSC.setGeometry(QtCore.QRect(60, 350, 131, 31))
        self.BTOSC.setStyleSheet(_fromUtf8("font: 19pt \"MS Shell Dlg 2\";"))
        self.BTOSC.setObjectName(_fromUtf8("BTOSC"))
        self.AddTeamToCardButton = QtGui.QPushButton(self.SelectTeam)
        self.AddTeamToCardButton.setGeometry(QtCore.QRect(240, 350, 131, 31))
        self.AddTeamToCardButton.setStyleSheet(_fromUtf8("font: 19pt \"MS Shell Dlg 2\";"))
        self.AddTeamToCardButton.setObjectName(_fromUtf8("AddTeamToCardButton"))
        self.TeamPlayerList = QtGui.QListWidget(self.SelectTeam)
        self.TeamPlayerList.setGeometry(QtCore.QRect(10, 161, 241, 181))
        self.TeamPlayerList.setObjectName(_fromUtf8("TeamPlayerList"))
        self.MatchPlayerList = QtGui.QListWidget(self.SelectTeam)
        self.MatchPlayerList.setGeometry(QtCore.QRect(315, 161, 241, 181))
        self.MatchPlayerList.setObjectName(_fromUtf8("MatchPlayerList"))
        self.AButton = QtGui.QPushButton(self.SelectTeam)
        self.AButton.setGeometry(QtCore.QRect(260, 190, 41, 31))
        self.AButton.setObjectName(_fromUtf8("AButton"))
        self.RButton = QtGui.QPushButton(self.SelectTeam)
        self.RButton.setGeometry(QtCore.QRect(260, 280, 41, 31))
        self.RButton.setObjectName(_fromUtf8("RButton"))
        self.IP_Title_8 = QtGui.QLabel(self.SelectTeam)
        self.IP_Title_8.setGeometry(QtCore.QRect(330, 110, 201, 41))
        self.IP_Title_8.setObjectName(_fromUtf8("IP_Title_8"))
        self.ConnectToCardButton = QtGui.QPushButton(self.SelectTeam)
        self.ConnectToCardButton.setGeometry(QtCore.QRect(410, 350, 131, 31))
        self.ConnectToCardButton.setStyleSheet(_fromUtf8("font: 19pt \"MS Shell Dlg 2\";"))
        self.ConnectToCardButton.setObjectName(_fromUtf8("ConnectToCardButton"))
        StackedWidget.addWidget(self.SelectTeam)
        self.FTIPage = QtGui.QWidget()
        self.FTIPage.setObjectName(_fromUtf8("FTIPage"))
        self.Title_TeamPage_2 = QtGui.QLabel(self.FTIPage)
        self.Title_TeamPage_2.setGeometry(QtCore.QRect(120, 10, 351, 41))
        self.Title_TeamPage_2.setObjectName(_fromUtf8("Title_TeamPage_2"))
        self.TeamName = QtGui.QLineEdit(self.FTIPage)
        self.TeamName.setGeometry(QtCore.QRect(200, 70, 251, 31))
        self.TeamName.setStyleSheet(_fromUtf8("font: 14pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.TeamName.setObjectName(_fromUtf8("TeamName"))
        self.FTNT_2 = QtGui.QLabel(self.FTIPage)
        self.FTNT_2.setGeometry(QtCore.QRect(40, 60, 161, 31))
        self.FTNT_2.setObjectName(_fromUtf8("FTNT_2"))
        self.P4NO = QtGui.QLineEdit(self.FTIPage)
        self.P4NO.setGeometry(QtCore.QRect(40, 280, 71, 31))
        self.P4NO.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P4NO.setObjectName(_fromUtf8("P4NO"))
        self.P3NO = QtGui.QLineEdit(self.FTIPage)
        self.P3NO.setGeometry(QtCore.QRect(40, 240, 71, 31))
        self.P3NO.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P3NO.setObjectName(_fromUtf8("P3NO"))
        self.P5NO = QtGui.QLineEdit(self.FTIPage)
        self.P5NO.setGeometry(QtCore.QRect(40, 320, 71, 31))
        self.P5NO.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P5NO.setObjectName(_fromUtf8("P5NO"))
        self.P2NA = QtGui.QLineEdit(self.FTIPage)
        self.P2NA.setGeometry(QtCore.QRect(120, 200, 71, 31))
        self.P2NA.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P2NA.setObjectName(_fromUtf8("P2NA"))
        self.P1NO = QtGui.QLineEdit(self.FTIPage)
        self.P1NO.setGeometry(QtCore.QRect(40, 160, 71, 31))
        self.P1NO.setStyleSheet(_fromUtf8("font: 12pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P1NO.setText(_fromUtf8(""))
        self.P1NO.setObjectName(_fromUtf8("P1NO"))
        self.P5NA = QtGui.QLineEdit(self.FTIPage)
        self.P5NA.setGeometry(QtCore.QRect(120, 320, 71, 31))
        self.P5NA.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P5NA.setText(_fromUtf8(""))
        self.P5NA.setObjectName(_fromUtf8("P5NA"))
        self.P3NA = QtGui.QLineEdit(self.FTIPage)
        self.P3NA.setGeometry(QtCore.QRect(120, 240, 71, 31))
        self.P3NA.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P3NA.setObjectName(_fromUtf8("P3NA"))
        self.IP_Title_4 = QtGui.QLabel(self.FTIPage)
        self.IP_Title_4.setGeometry(QtCore.QRect(70, 110, 461, 41))
        self.IP_Title_4.setObjectName(_fromUtf8("IP_Title_4"))
        self.P4NA = QtGui.QLineEdit(self.FTIPage)
        self.P4NA.setGeometry(QtCore.QRect(120, 280, 71, 31))
        self.P4NA.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P4NA.setObjectName(_fromUtf8("P4NA"))
        self.P2NO = QtGui.QLineEdit(self.FTIPage)
        self.P2NO.setGeometry(QtCore.QRect(40, 200, 71, 31))
        self.P2NO.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P2NO.setObjectName(_fromUtf8("P2NO"))
        self.P1NA = QtGui.QLineEdit(self.FTIPage)
        self.P1NA.setGeometry(QtCore.QRect(120, 160, 71, 31))
        self.P1NA.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P1NA.setText(_fromUtf8(""))
        self.P1NA.setObjectName(_fromUtf8("P1NA"))
        self.P9NA = QtGui.QLineEdit(self.FTIPage)
        self.P9NA.setGeometry(QtCore.QRect(290, 280, 71, 31))
        self.P9NA.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P9NA.setObjectName(_fromUtf8("P9NA"))
        self.P6NA = QtGui.QLineEdit(self.FTIPage)
        self.P6NA.setGeometry(QtCore.QRect(290, 160, 71, 31))
        self.P6NA.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P6NA.setObjectName(_fromUtf8("P6NA"))
        self.P10NO = QtGui.QLineEdit(self.FTIPage)
        self.P10NO.setGeometry(QtCore.QRect(210, 320, 71, 31))
        self.P10NO.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P10NO.setObjectName(_fromUtf8("P10NO"))
        self.P10NA = QtGui.QLineEdit(self.FTIPage)
        self.P10NA.setGeometry(QtCore.QRect(290, 320, 71, 31))
        self.P10NA.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P10NA.setText(_fromUtf8(""))
        self.P10NA.setObjectName(_fromUtf8("P10NA"))
        self.P7NO = QtGui.QLineEdit(self.FTIPage)
        self.P7NO.setGeometry(QtCore.QRect(210, 200, 71, 31))
        self.P7NO.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P7NO.setObjectName(_fromUtf8("P7NO"))
        self.P6NO = QtGui.QLineEdit(self.FTIPage)
        self.P6NO.setGeometry(QtCore.QRect(210, 160, 71, 31))
        self.P6NO.setStyleSheet(_fromUtf8("font: 12pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P6NO.setText(_fromUtf8(""))
        self.P6NO.setObjectName(_fromUtf8("P6NO"))
        self.P8NA = QtGui.QLineEdit(self.FTIPage)
        self.P8NA.setGeometry(QtCore.QRect(290, 240, 71, 31))
        self.P8NA.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P8NA.setObjectName(_fromUtf8("P8NA"))
        self.P8NO = QtGui.QLineEdit(self.FTIPage)
        self.P8NO.setGeometry(QtCore.QRect(210, 240, 71, 31))
        self.P8NO.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P8NO.setObjectName(_fromUtf8("P8NO"))
        self.P9NO = QtGui.QLineEdit(self.FTIPage)
        self.P9NO.setGeometry(QtCore.QRect(210, 280, 71, 31))
        self.P9NO.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P9NO.setObjectName(_fromUtf8("P9NO"))
        self.P7NA = QtGui.QLineEdit(self.FTIPage)
        self.P7NA.setGeometry(QtCore.QRect(290, 200, 71, 31))
        self.P7NA.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P7NA.setObjectName(_fromUtf8("P7NA"))
        self.P14NA = QtGui.QLineEdit(self.FTIPage)
        self.P14NA.setGeometry(QtCore.QRect(470, 280, 81, 31))
        self.P14NA.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P14NA.setObjectName(_fromUtf8("P14NA"))
        self.P11NA = QtGui.QLineEdit(self.FTIPage)
        self.P11NA.setGeometry(QtCore.QRect(470, 160, 81, 31))
        self.P11NA.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P11NA.setObjectName(_fromUtf8("P11NA"))
        self.P15NO = QtGui.QLineEdit(self.FTIPage)
        self.P15NO.setGeometry(QtCore.QRect(380, 320, 81, 31))
        self.P15NO.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P15NO.setObjectName(_fromUtf8("P15NO"))
        self.P15NA = QtGui.QLineEdit(self.FTIPage)
        self.P15NA.setGeometry(QtCore.QRect(470, 320, 81, 31))
        self.P15NA.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P15NA.setText(_fromUtf8(""))
        self.P15NA.setObjectName(_fromUtf8("P15NA"))
        self.P12NO = QtGui.QLineEdit(self.FTIPage)
        self.P12NO.setGeometry(QtCore.QRect(380, 200, 81, 31))
        self.P12NO.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P12NO.setObjectName(_fromUtf8("P12NO"))
        self.P11NO = QtGui.QLineEdit(self.FTIPage)
        self.P11NO.setGeometry(QtCore.QRect(380, 160, 81, 31))
        self.P11NO.setStyleSheet(_fromUtf8("font: 12pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P11NO.setText(_fromUtf8(""))
        self.P11NO.setObjectName(_fromUtf8("P11NO"))
        self.P13NA = QtGui.QLineEdit(self.FTIPage)
        self.P13NA.setGeometry(QtCore.QRect(470, 240, 81, 31))
        self.P13NA.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P13NA.setObjectName(_fromUtf8("P13NA"))
        self.P13NO = QtGui.QLineEdit(self.FTIPage)
        self.P13NO.setGeometry(QtCore.QRect(380, 240, 81, 31))
        self.P13NO.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P13NO.setObjectName(_fromUtf8("P13NO"))
        self.P14NO = QtGui.QLineEdit(self.FTIPage)
        self.P14NO.setGeometry(QtCore.QRect(380, 280, 81, 31))
        self.P14NO.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P14NO.setObjectName(_fromUtf8("P14NO"))
        self.P12NA = QtGui.QLineEdit(self.FTIPage)
        self.P12NA.setGeometry(QtCore.QRect(470, 200, 81, 31))
        self.P12NA.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P12NA.setObjectName(_fromUtf8("P12NA"))
        self.FTIB = QtGui.QPushButton(self.FTIPage)
        self.FTIB.setGeometry(QtCore.QRect(114, 360, 121, 31))
        self.FTIB.setObjectName(_fromUtf8("FTIB"))
        self.AddTeamToDB = QtGui.QPushButton(self.FTIPage)
        self.AddTeamToDB.setGeometry(QtCore.QRect(340, 360, 121, 31))
        self.AddTeamToDB.setObjectName(_fromUtf8("AddTeamToDB"))
        StackedWidget.addWidget(self.FTIPage)
        self.ANSRC = QtGui.QWidget()
        self.ANSRC.setObjectName(_fromUtf8("ANSRC"))
        self.CIP = QtGui.QLineEdit(self.ANSRC)
        self.CIP.setGeometry(QtCore.QRect(290, 120, 231, 31))
        self.CIP.setStyleSheet(_fromUtf8("font: 14pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.CIP.setObjectName(_fromUtf8("CIP"))
        self.Title_2 = QtGui.QLabel(self.ANSRC)
        self.Title_2.setGeometry(QtCore.QRect(120, 10, 351, 101))
        self.Title_2.setObjectName(_fromUtf8("Title_2"))
        self.Port_Title_2 = QtGui.QLabel(self.ANSRC)
        self.Port_Title_2.setGeometry(QtCore.QRect(30, 190, 231, 31))
        self.Port_Title_2.setObjectName(_fromUtf8("Port_Title_2"))
        self.CP = QtGui.QLineEdit(self.ANSRC)
        self.CP.setGeometry(QtCore.QRect(290, 190, 231, 31))
        self.CP.setStyleSheet(_fromUtf8("font: 14pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.CP.setObjectName(_fromUtf8("CP"))
        self.IP_Title_5 = QtGui.QLabel(self.ANSRC)
        self.IP_Title_5.setGeometry(QtCore.QRect(30, 120, 231, 31))
        self.IP_Title_5.setObjectName(_fromUtf8("IP_Title_5"))
        self.RN = QtGui.QLineEdit(self.ANSRC)
        self.RN.setGeometry(QtCore.QRect(290, 260, 231, 31))
        self.RN.setStyleSheet(_fromUtf8("font: 14pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.RN.setObjectName(_fromUtf8("RN"))
        self.Port_Title_3 = QtGui.QLabel(self.ANSRC)
        self.Port_Title_3.setGeometry(QtCore.QRect(30, 260, 261, 31))
        self.Port_Title_3.setObjectName(_fromUtf8("Port_Title_3"))
        self.ANSRCB = QtGui.QPushButton(self.ANSRC)
        self.ANSRCB.setGeometry(QtCore.QRect(64, 320, 91, 31))
        self.ANSRCB.setObjectName(_fromUtf8("ANSRCB"))
        self.AddToDB = QtGui.QPushButton(self.ANSRC)
        self.AddToDB.setGeometry(QtCore.QRect(384, 320, 81, 31))
        self.AddToDB.setObjectName(_fromUtf8("AddToDB"))
        StackedWidget.addWidget(self.ANSRC)
        self.MatchMode = QtGui.QWidget()
        self.MatchMode.setObjectName(_fromUtf8("MatchMode"))
        self.Title_Squad_2 = QtGui.QLabel(self.MatchMode)
        self.Title_Squad_2.setGeometry(QtCore.QRect(200, -10, 181, 51))
        self.Title_Squad_2.setObjectName(_fromUtf8("Title_Squad_2"))
        self.tabWidget = QtGui.QTabWidget(self.MatchMode)
        self.tabWidget.setGeometry(QtCore.QRect(10, 40, 541, 351))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.MatchTab = QtGui.QWidget()
        self.MatchTab.setObjectName(_fromUtf8("MatchTab"))
        self.MatchNotification = QtGui.QTextEdit(self.MatchTab)
        self.MatchNotification.setGeometry(QtCore.QRect(0, 0, 541, 331))
        self.MatchNotification.setStyleSheet(_fromUtf8("font: 20pt \"MS Shell Dlg 2\";"))
        self.MatchNotification.setReadOnly(True)
        self.MatchNotification.setObjectName(_fromUtf8("MatchNotification"))
        self.tabWidget.addTab(self.MatchTab, _fromUtf8(""))
        self.SubTab = QtGui.QWidget()
        self.SubTab.setObjectName(_fromUtf8("SubTab"))
        self.POutCombo = QtGui.QComboBox(self.SubTab)
        self.POutCombo.setGeometry(QtCore.QRect(10, 220, 191, 31))
        self.POutCombo.setObjectName(_fromUtf8("POutCombo"))
        self.ApplySubButton = QtGui.QPushButton(self.SubTab)
        self.ApplySubButton.setGeometry(QtCore.QRect(220, 260, 91, 41))
        self.ApplySubButton.setStyleSheet(_fromUtf8("font: 14pt \"MS Shell Dlg 2\";"))
        self.ApplySubButton.setObjectName(_fromUtf8("ApplySubButton"))
        self.label_2 = QtGui.QLabel(self.SubTab)
        self.label_2.setGeometry(QtCore.QRect(10, 170, 181, 51))
        self.label_2.setStyleSheet(_fromUtf8("font: 28pt \"MS Shell Dlg 2\";"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.PInCombo = QtGui.QComboBox(self.SubTab)
        self.PInCombo.setGeometry(QtCore.QRect(330, 220, 191, 31))
        self.PInCombo.setObjectName(_fromUtf8("PInCombo"))
        self.label_4 = QtGui.QLabel(self.SubTab)
        self.label_4.setGeometry(QtCore.QRect(330, 170, 181, 51))
        self.label_4.setStyleSheet(_fromUtf8("font: 28pt \"MS Shell Dlg 2\";"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.SubTab)
        self.label_5.setGeometry(QtCore.QRect(120, 10, 311, 31))
        self.label_5.setStyleSheet(_fromUtf8("font: 26pt \"MS Shell Dlg 2\";"))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.SubTab)
        self.label_6.setGeometry(QtCore.QRect(20, 110, 381, 41))
        self.label_6.setStyleSheet(_fromUtf8("font: 22pt \"MS Shell Dlg 2\";"))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.SubNum = QtGui.QLineEdit(self.SubTab)
        self.SubNum.setGeometry(QtCore.QRect(420, 119, 113, 31))
        self.SubNum.setReadOnly(True)
        self.SubNum.setObjectName(_fromUtf8("SubNum"))
        self.SelectTeamSubButton = QtGui.QPushButton(self.SubTab)
        self.SelectTeamSubButton.setGeometry(QtCore.QRect(430, 60, 81, 41))
        self.SelectTeamSubButton.setStyleSheet(_fromUtf8("font: 20pt \"MS Shell Dlg 2\";"))
        self.SelectTeamSubButton.setObjectName(_fromUtf8("SelectTeamSubButton"))
        self.TeamNamesSubCombo = QtGui.QComboBox(self.SubTab)
        self.TeamNamesSubCombo.setGeometry(QtCore.QRect(200, 60, 191, 41))
        self.TeamNamesSubCombo.setStyleSheet(_fromUtf8("font: 12pt \"MS Shell Dlg 2\";"))
        self.TeamNamesSubCombo.setObjectName(_fromUtf8("TeamNamesSubCombo"))
        self.SelectTeamLabel_2 = QtGui.QLabel(self.SubTab)
        self.SelectTeamLabel_2.setGeometry(QtCore.QRect(20, 60, 171, 41))
        self.SelectTeamLabel_2.setStyleSheet(_fromUtf8("font: 20pt \"MS Shell Dlg 2\";"))
        self.SelectTeamLabel_2.setObjectName(_fromUtf8("SelectTeamLabel_2"))
        self.tabWidget.addTab(self.SubTab, _fromUtf8(""))
        self.BackFromMMToMM = QtGui.QPushButton(self.MatchMode)
        self.BackFromMMToMM.setGeometry(QtCore.QRect(430, 10, 75, 41))
        self.BackFromMMToMM.setObjectName(_fromUtf8("BackFromMMToMM"))
        StackedWidget.addWidget(self.MatchMode)
        self.Squad_Page = QtGui.QWidget()
        self.Squad_Page.setObjectName(_fromUtf8("Squad_Page"))
        self.Title_Squad = QtGui.QLabel(self.Squad_Page)
        self.Title_Squad.setGeometry(QtCore.QRect(120, 10, 351, 51))
        self.Title_Squad.setObjectName(_fromUtf8("Title_Squad"))
        self.IP_Title_2 = QtGui.QLabel(self.Squad_Page)
        self.IP_Title_2.setGeometry(QtCore.QRect(30, 60, 231, 41))
        self.IP_Title_2.setObjectName(_fromUtf8("IP_Title_2"))
        self.P1T1 = QtGui.QLineEdit(self.Squad_Page)
        self.P1T1.setGeometry(QtCore.QRect(60, 110, 71, 31))
        self.P1T1.setStyleSheet(_fromUtf8("font: 12pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P1T1.setText(_fromUtf8(""))
        self.P1T1.setObjectName(_fromUtf8("P1T1"))
        self.P2T1 = QtGui.QLineEdit(self.Squad_Page)
        self.P2T1.setGeometry(QtCore.QRect(60, 150, 71, 31))
        self.P2T1.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P2T1.setObjectName(_fromUtf8("P2T1"))
        self.P3T1 = QtGui.QLineEdit(self.Squad_Page)
        self.P3T1.setGeometry(QtCore.QRect(60, 190, 71, 31))
        self.P3T1.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P3T1.setObjectName(_fromUtf8("P3T1"))
        self.P4T1 = QtGui.QLineEdit(self.Squad_Page)
        self.P4T1.setGeometry(QtCore.QRect(60, 230, 71, 31))
        self.P4T1.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P4T1.setObjectName(_fromUtf8("P4T1"))
        self.P5T1 = QtGui.QLineEdit(self.Squad_Page)
        self.P5T1.setGeometry(QtCore.QRect(60, 270, 71, 31))
        self.P5T1.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P5T1.setObjectName(_fromUtf8("P5T1"))
        self.P6T1 = QtGui.QLineEdit(self.Squad_Page)
        self.P6T1.setGeometry(QtCore.QRect(60, 310, 71, 31))
        self.P6T1.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P6T1.setObjectName(_fromUtf8("P6T1"))
        self.P7T1 = QtGui.QLineEdit(self.Squad_Page)
        self.P7T1.setGeometry(QtCore.QRect(140, 110, 71, 31))
        self.P7T1.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P7T1.setObjectName(_fromUtf8("P7T1"))
        self.P8T1 = QtGui.QLineEdit(self.Squad_Page)
        self.P8T1.setGeometry(QtCore.QRect(140, 150, 71, 31))
        self.P8T1.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P8T1.setObjectName(_fromUtf8("P8T1"))
        self.P9T1 = QtGui.QLineEdit(self.Squad_Page)
        self.P9T1.setGeometry(QtCore.QRect(140, 190, 71, 31))
        self.P9T1.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P9T1.setObjectName(_fromUtf8("P9T1"))
        self.P10T1 = QtGui.QLineEdit(self.Squad_Page)
        self.P10T1.setGeometry(QtCore.QRect(140, 230, 71, 31))
        self.P10T1.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P10T1.setObjectName(_fromUtf8("P10T1"))
        self.IP_Title_3 = QtGui.QLabel(self.Squad_Page)
        self.IP_Title_3.setGeometry(QtCore.QRect(320, 60, 231, 41))
        self.IP_Title_3.setObjectName(_fromUtf8("IP_Title_3"))
        self.P8T2 = QtGui.QLineEdit(self.Squad_Page)
        self.P8T2.setGeometry(QtCore.QRect(430, 150, 71, 31))
        self.P8T2.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P8T2.setObjectName(_fromUtf8("P8T2"))
        self.P10T2 = QtGui.QLineEdit(self.Squad_Page)
        self.P10T2.setGeometry(QtCore.QRect(430, 230, 71, 31))
        self.P10T2.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P10T2.setObjectName(_fromUtf8("P10T2"))
        self.P1T2 = QtGui.QLineEdit(self.Squad_Page)
        self.P1T2.setGeometry(QtCore.QRect(350, 110, 71, 31))
        self.P1T2.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P1T2.setObjectName(_fromUtf8("P1T2"))
        self.P2T2 = QtGui.QLineEdit(self.Squad_Page)
        self.P2T2.setGeometry(QtCore.QRect(350, 150, 71, 31))
        self.P2T2.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P2T2.setObjectName(_fromUtf8("P2T2"))
        self.P7T2 = QtGui.QLineEdit(self.Squad_Page)
        self.P7T2.setGeometry(QtCore.QRect(430, 110, 71, 31))
        self.P7T2.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P7T2.setObjectName(_fromUtf8("P7T2"))
        self.P3T2 = QtGui.QLineEdit(self.Squad_Page)
        self.P3T2.setGeometry(QtCore.QRect(350, 190, 71, 31))
        self.P3T2.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P3T2.setObjectName(_fromUtf8("P3T2"))
        self.P6T2 = QtGui.QLineEdit(self.Squad_Page)
        self.P6T2.setGeometry(QtCore.QRect(350, 310, 71, 31))
        self.P6T2.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P6T2.setObjectName(_fromUtf8("P6T2"))
        self.P5T2 = QtGui.QLineEdit(self.Squad_Page)
        self.P5T2.setGeometry(QtCore.QRect(350, 270, 71, 31))
        self.P5T2.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P5T2.setObjectName(_fromUtf8("P5T2"))
        self.P9T2 = QtGui.QLineEdit(self.Squad_Page)
        self.P9T2.setGeometry(QtCore.QRect(430, 190, 71, 31))
        self.P9T2.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P9T2.setObjectName(_fromUtf8("P9T2"))
        self.P4T2 = QtGui.QLineEdit(self.Squad_Page)
        self.P4T2.setGeometry(QtCore.QRect(350, 230, 71, 31))
        self.P4T2.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P4T2.setObjectName(_fromUtf8("P4T2"))
        self.SetSquad = QtGui.QPushButton(self.Squad_Page)
        self.SetSquad.setGeometry(QtCore.QRect(310, 350, 211, 41))
        self.SetSquad.setStyleSheet(_fromUtf8("font: 19pt \"MS Shell Dlg 2\";"))
        self.SetSquad.setObjectName(_fromUtf8("SetSquad"))
        self.BackToTeamsName = QtGui.QPushButton(self.Squad_Page)
        self.BackToTeamsName.setGeometry(QtCore.QRect(50, 350, 211, 41))
        self.BackToTeamsName.setStyleSheet(_fromUtf8("font: 19pt \"MS Shell Dlg 2\";"))
        self.BackToTeamsName.setObjectName(_fromUtf8("BackToTeamsName"))
        self.P11T1 = QtGui.QLineEdit(self.Squad_Page)
        self.P11T1.setGeometry(QtCore.QRect(140, 270, 71, 31))
        self.P11T1.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P11T1.setText(_fromUtf8(""))
        self.P11T1.setObjectName(_fromUtf8("P11T1"))
        self.P11T2 = QtGui.QLineEdit(self.Squad_Page)
        self.P11T2.setGeometry(QtCore.QRect(430, 270, 71, 31))
        self.P11T2.setStyleSheet(_fromUtf8("font: 11pt \"MS Shell Dlg 2\";\n"
"color:gb(86, 43, 0)"))
        self.P11T2.setObjectName(_fromUtf8("P11T2"))
        StackedWidget.addWidget(self.Squad_Page)

        self.retranslateUi(StackedWidget)
        StackedWidget.setCurrentIndex(3)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(StackedWidget)

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(_translate("StackedWidget", "Smart Referee Card", None))
        self.Title_TeamPage.setText(_translate("StackedWidget", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Set both teams</span></p><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">names</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.FTNT.setText(_translate("StackedWidget", "<html><head/><body><p><span style=\" font-size:22pt;\">First team name</span></p></body></html>", None))
        self.STNT.setText(_translate("StackedWidget", "<html><head/><body><p><span style=\" font-size:22pt;\">Second team name</span></p></body></html>", None))
        self.Back.setText(_translate("StackedWidget", "Back", None))
        self.Next.setText(_translate("StackedWidget", "Set", None))
        self.Title.setText(_translate("StackedWidget", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Connect to the Smart</span></p><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Referee Card</span></p></body></html>", None))
        self.ConnectionError.setText(_translate("StackedWidget", "<html><head/><body><p align=\"center\">Fill the above Info</p><p align=\"center\"><br/></p></body></html>", None))
        self.Port_Title.setText(_translate("StackedWidget", "<html><head/><body><p><span style=\" font-size:22pt;\">Card Port number</span></p></body></html>", None))
        self.ConnectButton.setText(_translate("StackedWidget", "Connect", None))
        self.IP_Title.setText(_translate("StackedWidget", "<html><head/><body><p><span style=\" font-size:22pt;\">Card IP address</span></p></body></html>", None))
        self.StateT.setText(_translate("StackedWidget", "<html><head/><body><p><span style=\" font-size:24pt;\">State </span></p></body></html>", None))
        self.BTOMM.setText(_translate("StackedWidget", "Back", None))
        self.MMLabel.setText(_translate("StackedWidget", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Main Menu</span></p></body></html>", None))
        self.ANCButton.setToolTip(_translate("StackedWidget", "<html><head/><body><p><span style=\" font-size:12pt;\">Connect to the SRC </span></p></body></html>", None))
        self.ANCButton.setWhatsThis(_translate("StackedWidget", "<html><head/><body><p><span style=\" font-size:12pt;\">Connect to the SRC </span></p></body></html>", None))
        self.ANCButton.setText(_translate("StackedWidget", "Add New Card", None))
        self.SCButton.setText(_translate("StackedWidget", "Select a Card", None))
        self.MMButton.setText(_translate("StackedWidget", "Match Mode", None))
        self.VLTButton.setText(_translate("StackedWidget", "View Reports", None))
        self.ANTButton.setToolTip(_translate("StackedWidget", "<html><head/><body><p><span style=\" font-size:12pt;\">Connect to the SRC </span></p></body></html>", None))
        self.ANTButton.setWhatsThis(_translate("StackedWidget", "<html><head/><body><p><span style=\" font-size:12pt;\">Connect to the SRC </span></p></body></html>", None))
        self.ANTButton.setText(_translate("StackedWidget", "Add New Team", None))
        self.TMButton.setToolTip(_translate("StackedWidget", "<html><head/><body><p><span style=\" font-size:12pt;\">Connect to the SRC </span></p></body></html>", None))
        self.TMButton.setWhatsThis(_translate("StackedWidget", "<html><head/><body><p><span style=\" font-size:12pt;\">Connect to the SRC </span></p></body></html>", None))
        self.TMButton.setText(_translate("StackedWidget", "Test Mode", None))
        self.MMLabel_3.setText(_translate("StackedWidget", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Select a card</span></p></body></html>", None))
        self.label.setText(_translate("StackedWidget", "Select Card", None))
        self.ShowIPPORT.setText(_translate("StackedWidget", "Ok", None))
        self.Port_Title_4.setText(_translate("StackedWidget", "<html><head/><body><p><span style=\" font-size:22pt;\">Card Port number</span></p></body></html>", None))
        self.IP_Title_6.setText(_translate("StackedWidget", "<html><head/><body><p><span style=\" font-size:22pt;\">Card IP address</span></p></body></html>", None))
        self.ApplyEdit.setText(_translate("StackedWidget", "Apply", None))
        self.BTOMMSAC.setText(_translate("StackedWidget", "Back", None))
        self.EditIPPORT.setText(_translate("StackedWidget", "Edit", None))
        self.ConnectToCard.setText(_translate("StackedWidget", "Connect", None))
        self.MMLabel_2.setText(_translate("StackedWidget", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Reports</span></p></body></html>", None))
        self.LeagueBack.setText(_translate("StackedWidget", "Back", None))
        self.SelectTeamButton.setText(_translate("StackedWidget", "Ok", None))
        self.MMLabel_4.setText(_translate("StackedWidget", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Select a Team</span></p></body></html>", None))
        self.SelectTeamLabel.setText(_translate("StackedWidget", "Select Team 1", None))
        self.IP_Title_7.setText(_translate("StackedWidget", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Team  Squad</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.BTOSC.setText(_translate("StackedWidget", "Back", None))
        self.AddTeamToCardButton.setText(_translate("StackedWidget", "Add", None))
        self.AButton.setText(_translate("StackedWidget", ">>", None))
        self.RButton.setText(_translate("StackedWidget", "<<", None))
        self.IP_Title_8.setText(_translate("StackedWidget", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Match Squad</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.ConnectToCardButton.setText(_translate("StackedWidget", "Connect", None))
        self.Title_TeamPage_2.setText(_translate("StackedWidget", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Fill Team Information</span></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p></body></html>", None))
        self.FTNT_2.setText(_translate("StackedWidget", "<html><head/><body><p><span style=\" font-size:22pt;\">Team Name </span></p><p><br/></p></body></html>", None))
        self.P4NO.setPlaceholderText(_translate("StackedWidget", "P4 Num", None))
        self.P3NO.setPlaceholderText(_translate("StackedWidget", "P3 Num", None))
        self.P5NO.setPlaceholderText(_translate("StackedWidget", "P5 Num", None))
        self.P2NA.setPlaceholderText(_translate("StackedWidget", "P2 Name", None))
        self.P1NO.setPlaceholderText(_translate("StackedWidget", "P1 Num", None))
        self.P5NA.setPlaceholderText(_translate("StackedWidget", "P5 Name", None))
        self.P3NA.setPlaceholderText(_translate("StackedWidget", "P3 Name", None))
        self.IP_Title_4.setText(_translate("StackedWidget", "<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\">Team  Squad</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.P4NA.setPlaceholderText(_translate("StackedWidget", "P4 Name", None))
        self.P2NO.setPlaceholderText(_translate("StackedWidget", "P2 Num", None))
        self.P1NA.setPlaceholderText(_translate("StackedWidget", "P1 Name", None))
        self.P9NA.setPlaceholderText(_translate("StackedWidget", "P9 Name", None))
        self.P6NA.setPlaceholderText(_translate("StackedWidget", "P6 Name", None))
        self.P10NO.setPlaceholderText(_translate("StackedWidget", "P10 Num", None))
        self.P10NA.setPlaceholderText(_translate("StackedWidget", "P10 Name", None))
        self.P7NO.setPlaceholderText(_translate("StackedWidget", "P7 Num", None))
        self.P6NO.setPlaceholderText(_translate("StackedWidget", "P6 Num", None))
        self.P8NA.setPlaceholderText(_translate("StackedWidget", "P8 Name", None))
        self.P8NO.setPlaceholderText(_translate("StackedWidget", "P8 Num", None))
        self.P9NO.setPlaceholderText(_translate("StackedWidget", "P9 Num", None))
        self.P7NA.setPlaceholderText(_translate("StackedWidget", "P7 Name", None))
        self.P14NA.setPlaceholderText(_translate("StackedWidget", "P14 Name", None))
        self.P11NA.setPlaceholderText(_translate("StackedWidget", "P11 Name", None))
        self.P15NO.setPlaceholderText(_translate("StackedWidget", "P15 Num", None))
        self.P15NA.setPlaceholderText(_translate("StackedWidget", "P15 Name", None))
        self.P12NO.setPlaceholderText(_translate("StackedWidget", "P12 Num", None))
        self.P11NO.setPlaceholderText(_translate("StackedWidget", "P11 Num", None))
        self.P13NA.setPlaceholderText(_translate("StackedWidget", "P13 Name", None))
        self.P13NO.setPlaceholderText(_translate("StackedWidget", "P13 Num", None))
        self.P14NO.setPlaceholderText(_translate("StackedWidget", "P14 Num", None))
        self.P12NA.setPlaceholderText(_translate("StackedWidget", "P12 Name", None))
        self.FTIB.setText(_translate("StackedWidget", "Back", None))
        self.AddTeamToDB.setText(_translate("StackedWidget", "Add", None))
        self.Title_2.setText(_translate("StackedWidget", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Add New Smart</span></p><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Referee Card</span></p></body></html>", None))
        self.Port_Title_2.setText(_translate("StackedWidget", "<html><head/><body><p><span style=\" font-size:22pt;\">Card Port number</span></p></body></html>", None))
        self.IP_Title_5.setText(_translate("StackedWidget", "<html><head/><body><p><span style=\" font-size:22pt;\">Card IP address</span></p></body></html>", None))
        self.Port_Title_3.setText(_translate("StackedWidget", "<html><head/><body><p><span style=\" font-size:22pt;\">Card/Referee Name</span></p></body></html>", None))
        self.ANSRCB.setText(_translate("StackedWidget", "Back", None))
        self.AddToDB.setText(_translate("StackedWidget", "Add", None))
        self.Title_Squad_2.setText(_translate("StackedWidget", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Match Mode</span></p></body></html>", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.MatchTab), _translate("StackedWidget", "Match", None))
        self.ApplySubButton.setText(_translate("StackedWidget", "Apply", None))
        self.label_2.setText(_translate("StackedWidget", "Player Out ", None))
        self.label_4.setText(_translate("StackedWidget", "Player In ", None))
        self.label_5.setText(_translate("StackedWidget", "Make a substitution", None))
        self.label_6.setText(_translate("StackedWidget", "Number of substitutions left :  ", None))
        self.SelectTeamSubButton.setText(_translate("StackedWidget", "Ok", None))
        self.SelectTeamLabel_2.setText(_translate("StackedWidget", "Select Team ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.SubTab), _translate("StackedWidget", "Substitution", None))
        self.BackFromMMToMM.setText(_translate("StackedWidget", "Back", None))
        self.Title_Squad.setText(_translate("StackedWidget", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Select teams squad</span></p><p align=\"center\"><br/></p></body></html>", None))
        self.IP_Title_2.setText(_translate("StackedWidget", "<html><head/><body><p><span style=\" font-size:22pt;\">Team 1 Squad</span></p><p><br/></p></body></html>", None))
        self.P1T1.setPlaceholderText(_translate("StackedWidget", "P1", None))
        self.P2T1.setPlaceholderText(_translate("StackedWidget", "P2", None))
        self.P3T1.setPlaceholderText(_translate("StackedWidget", "P3", None))
        self.P4T1.setPlaceholderText(_translate("StackedWidget", "P4", None))
        self.P5T1.setPlaceholderText(_translate("StackedWidget", "P5", None))
        self.P6T1.setPlaceholderText(_translate("StackedWidget", "P6", None))
        self.P7T1.setPlaceholderText(_translate("StackedWidget", "P7", None))
        self.P8T1.setPlaceholderText(_translate("StackedWidget", "P8", None))
        self.P9T1.setPlaceholderText(_translate("StackedWidget", "P9", None))
        self.P10T1.setPlaceholderText(_translate("StackedWidget", "P10", None))
        self.IP_Title_3.setText(_translate("StackedWidget", "<html><head/><body><p><span style=\" font-size:22pt;\">Team 2 Squad</span></p><p><br/></p></body></html>", None))
        self.P8T2.setPlaceholderText(_translate("StackedWidget", "P8", None))
        self.P10T2.setPlaceholderText(_translate("StackedWidget", "P10", None))
        self.P1T2.setPlaceholderText(_translate("StackedWidget", "P1", None))
        self.P2T2.setPlaceholderText(_translate("StackedWidget", "P2", None))
        self.P7T2.setPlaceholderText(_translate("StackedWidget", "P7", None))
        self.P3T2.setPlaceholderText(_translate("StackedWidget", "P3", None))
        self.P6T2.setPlaceholderText(_translate("StackedWidget", "P6", None))
        self.P5T2.setPlaceholderText(_translate("StackedWidget", "P5", None))
        self.P9T2.setPlaceholderText(_translate("StackedWidget", "P9", None))
        self.P4T2.setPlaceholderText(_translate("StackedWidget", "P4", None))
        self.SetSquad.setText(_translate("StackedWidget", "Set", None))
        self.BackToTeamsName.setText(_translate("StackedWidget", "Back", None))
        self.P11T1.setPlaceholderText(_translate("StackedWidget", "P11", None))
        self.P11T2.setPlaceholderText(_translate("StackedWidget", "P11", None))

