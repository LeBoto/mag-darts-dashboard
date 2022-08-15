# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'game_widgetrqTbEb.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_game(object):
    def setupUi(self, game):
        if not game.objectName():
            game.setObjectName(u"game")
        game.resize(914, 318)
        self.gridLayout_2 = QGridLayout(game)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, -1, -1)
        self.label = QLabel(game)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 7)

        self.verticalSpacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.rm_GAME = QPushButton(game)
        self.rm_GAME.setObjectName(u"rm_GAME")

        self.gridLayout.addWidget(self.rm_GAME, 1, 6, 1, 1)

        self.horizontalSpacer = QSpacerItem(0, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 5, 1, 1)

        self.game_player_layout = QVBoxLayout()
        self.game_player_layout.setSpacing(0)
        self.game_player_layout.setObjectName(u"game_player_layout")
        self.verticalSpacer_2 = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.game_player_layout.addItem(self.verticalSpacer_2)


        self.gridLayout.addLayout(self.game_player_layout, 1, 2, 2, 3)

        self.pushButton = QPushButton(game)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(0, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(game)

        QMetaObject.connectSlotsByName(game)
    # setupUi

    def retranslateUi(self, game):
        game.setWindowTitle(QCoreApplication.translate("game", u"Form", None))
        self.label.setText(QCoreApplication.translate("game", u"Game", None))
        self.rm_GAME.setText(QCoreApplication.translate("game", u"  X  ", None))
        self.pushButton.setText(QCoreApplication.translate("game", u"+", None))
    # retranslateUi

