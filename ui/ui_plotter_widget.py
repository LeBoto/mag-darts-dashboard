# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plotterDtFudi.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QTabWidget,
    QVBoxLayout, QWidget)

from pyqtgraph import PlotWidget

class Ui_plotter(object):
    def setupUi(self, plotter):
        if not plotter.objectName():
            plotter.setObjectName(u"plotter")
        plotter.resize(700, 400)
        self.verticalLayout_2 = QVBoxLayout(plotter)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(plotter)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.East)
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout_6 = QGridLayout(self.tab)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.score_plot = PlotWidget(self.tab)
        self.score_plot.setObjectName(u"score_plot")

        self.gridLayout_5.addWidget(self.score_plot, 0, 0, 1, 1)


        self.gridLayout_6.addLayout(self.gridLayout_5, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.gridLayout_4 = QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.accuracy_plot = PlotWidget(self.tab_2)
        self.accuracy_plot.setObjectName(u"accuracy_plot")

        self.gridLayout_3.addWidget(self.accuracy_plot, 0, 0, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.gridLayout_2 = QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.aggregate_plot = PlotWidget(self.tab_3)
        self.aggregate_plot.setObjectName(u"aggregate_plot")

        self.gridLayout.addWidget(self.aggregate_plot, 0, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_3, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(plotter)

        self.tabWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(plotter)
    # setupUi

    def retranslateUi(self, plotter):
        plotter.setWindowTitle(QCoreApplication.translate("plotter", u"Form", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("plotter", u"Score", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("plotter", u"Accuracy", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("plotter", u"Aggregate", None))
    # retranslateUi

