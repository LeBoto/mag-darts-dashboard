# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'plotterkTZeBb.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QSpacerItem,
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
        self.plot_layout = QGridLayout()
        self.plot_layout.setObjectName(u"plot_layout")
        self.plot_layout.setVerticalSpacing(0)
        self.plot = PlotWidget(plotter)
        self.plot.setObjectName(u"plot")

        self.plot_layout.addWidget(self.plot, 0, 0, 3, 1)

        self.widget = QWidget(plotter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 99999, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.plot_layout.addWidget(self.widget, 1, 1, 2, 2)


        self.verticalLayout_2.addLayout(self.plot_layout)


        self.retranslateUi(plotter)

        QMetaObject.connectSlotsByName(plotter)
    # setupUi

    def retranslateUi(self, plotter):
        plotter.setWindowTitle(QCoreApplication.translate("plotter", u"Form", None))
    # retranslateUi

