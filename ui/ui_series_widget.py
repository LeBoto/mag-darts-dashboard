# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'series_widgetXuzNES.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_series(object):
    def setupUi(self, series):
        if not series.objectName():
            series.setObjectName(u"series")
        series.resize(580, 374)
        self.verticalLayout_2 = QVBoxLayout(series)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.horizontalSpacer = QSpacerItem(40, 1, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_8.addItem(self.horizontalSpacer, 0, 1, 1, 1)

        self.submit_series_btn = QPushButton(series)
        self.submit_series_btn.setObjectName(u"submit_series_btn")

        self.gridLayout_8.addWidget(self.submit_series_btn, 0, 2, 1, 1)

        self.addGame_btn = QPushButton(series)
        self.addGame_btn.setObjectName(u"addGame_btn")

        self.gridLayout_8.addWidget(self.addGame_btn, 0, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_8)

        self.scrollArea = QScrollArea(series)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.s_widget = QWidget()
        self.s_widget.setObjectName(u"s_widget")
        self.s_widget.setGeometry(QRect(0, 0, 558, 326))
        self.s_wdg_area = QVBoxLayout(self.s_widget)
        self.s_wdg_area.setObjectName(u"s_wdg_area")
        self.s_wdg_area.setContentsMargins(0, 0, 0, 0)
        self.s_layout = QVBoxLayout()
        self.s_layout.setObjectName(u"s_layout")
        self.verticalSpacer = QSpacerItem(20, 600, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.s_layout.addItem(self.verticalSpacer)


        self.s_wdg_area.addLayout(self.s_layout)

        self.scrollArea.setWidget(self.s_widget)

        self.verticalLayout.addWidget(self.scrollArea)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(series)

        QMetaObject.connectSlotsByName(series)
    # setupUi

    def retranslateUi(self, series):
        series.setWindowTitle(QCoreApplication.translate("series", u"Form", None))
        self.submit_series_btn.setText(QCoreApplication.translate("series", u"            Submit            ", None))
        self.addGame_btn.setText(QCoreApplication.translate("series", u" + ", None))
    # retranslateUi

