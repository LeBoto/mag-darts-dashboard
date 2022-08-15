# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'player_item_widgetOvuNPa.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QSizePolicy, QWidget)

class Ui_player_list_item(object):
    def setupUi(self, player_list_item):
        if not player_list_item.objectName():
            player_list_item.setObjectName(u"player_list_item")
        player_list_item.resize(121, 50)
        self.horizontalLayout_2 = QHBoxLayout(player_list_item)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.display_check = QCheckBox(player_list_item)
        self.display_check.setObjectName(u"display_check")

        self.horizontalLayout.addWidget(self.display_check)

        self.color = QLabel(player_list_item)
        self.color.setObjectName(u"color")
        self.color.setMinimumSize(QSize(30, 20))
        self.color.setMaximumSize(QSize(30, 20))

        self.horizontalLayout.addWidget(self.color)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(player_list_item)

        QMetaObject.connectSlotsByName(player_list_item)
    # setupUi

    def retranslateUi(self, player_list_item):
        player_list_item.setWindowTitle(QCoreApplication.translate("player_list_item", u"Form", None))
        self.display_check.setText(QCoreApplication.translate("player_list_item", u"player", None))
        self.color.setText("")
    # retranslateUi

