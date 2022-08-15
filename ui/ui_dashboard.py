# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboardQTHMyJ.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLineEdit,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_magDartDashboard(object):
    def setupUi(self, magDartDashboard):
        if not magDartDashboard.objectName():
            magDartDashboard.setObjectName(u"magDartDashboard")
        magDartDashboard.resize(800, 600)
        self.centralwidget = QWidget(magDartDashboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.display_tab = QTabWidget(self.centralwidget)
        self.display_tab.setObjectName(u"display_tab")
        self.dash_tab = QWidget()
        self.dash_tab.setObjectName(u"dash_tab")
        self.gridLayout_4 = QGridLayout(self.dash_tab)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.player_query_dash = QLineEdit(self.dash_tab)
        self.player_query_dash.setObjectName(u"player_query_dash")

        self.gridLayout.addWidget(self.player_query_dash, 1, 0, 1, 1)

        self.submit_dash = QPushButton(self.dash_tab)
        self.submit_dash.setObjectName(u"submit_dash")

        self.gridLayout.addWidget(self.submit_dash, 1, 1, 1, 1)

        self.display_dash = QTextEdit(self.dash_tab)
        self.display_dash.setObjectName(u"display_dash")
        self.display_dash.setSizeIncrement(QSize(0, 0))
        self.display_dash.setReadOnly(True)

        self.gridLayout.addWidget(self.display_dash, 2, 0, 1, 2)


        self.gridLayout_4.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.display_tab.addTab(self.dash_tab, "")
        self.plotting_tab = QWidget()
        self.plotting_tab.setObjectName(u"plotting_tab")
        self.gridLayout_10 = QGridLayout(self.plotting_tab)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabWidget = QTabWidget(self.plotting_tab)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.East)
        self.score_tab = QWidget()
        self.score_tab.setObjectName(u"score_tab")
        self.verticalLayout_8 = QVBoxLayout(self.score_tab)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.score_layout = QVBoxLayout()
        self.score_layout.setObjectName(u"score_layout")

        self.verticalLayout_8.addLayout(self.score_layout)

        self.tabWidget.addTab(self.score_tab, "")
        self.aggregate_tab = QWidget()
        self.aggregate_tab.setObjectName(u"aggregate_tab")
        self.verticalLayout_6 = QVBoxLayout(self.aggregate_tab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.aggregate_layout = QVBoxLayout()
        self.aggregate_layout.setObjectName(u"aggregate_layout")

        self.verticalLayout_6.addLayout(self.aggregate_layout)

        self.tabWidget.addTab(self.aggregate_tab, "")

        self.gridLayout_3.addWidget(self.tabWidget, 0, 0, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_3, 1, 0, 1, 1)

        self.display_tab.addTab(self.plotting_tab, "")
        self.record_tab = QWidget()
        self.record_tab.setObjectName(u"record_tab")
        self.verticalLayout_3 = QVBoxLayout(self.record_tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.record_tab)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addWidget(self.frame)

        self.display_tab.addTab(self.record_tab, "")

        self.verticalLayout.addWidget(self.display_tab)


        self.gridLayout_2.addLayout(self.verticalLayout, 0, 0, 1, 1)

        magDartDashboard.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(magDartDashboard)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        magDartDashboard.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(magDartDashboard)
        self.statusbar.setObjectName(u"statusbar")
        magDartDashboard.setStatusBar(self.statusbar)

        self.retranslateUi(magDartDashboard)

        self.display_tab.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(magDartDashboard)
    # setupUi

    def retranslateUi(self, magDartDashboard):
        magDartDashboard.setWindowTitle(QCoreApplication.translate("magDartDashboard", u"MainWindow", None))
        self.submit_dash.setText(QCoreApplication.translate("magDartDashboard", u"OK", None))
        self.display_tab.setTabText(self.display_tab.indexOf(self.dash_tab), QCoreApplication.translate("magDartDashboard", u"Dashboard", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.score_tab), QCoreApplication.translate("magDartDashboard", u"Score", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.aggregate_tab), QCoreApplication.translate("magDartDashboard", u"Aggregate", None))
        self.display_tab.setTabText(self.display_tab.indexOf(self.plotting_tab), QCoreApplication.translate("magDartDashboard", u"Plots", None))
        self.display_tab.setTabText(self.display_tab.indexOf(self.record_tab), QCoreApplication.translate("magDartDashboard", u"Record Scores", None))
    # retranslateUi

