# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'player_widgetTUuOaQ.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QWidget)

class Ui_player(object):
    def setupUi(self, player):
        if not player.objectName():
            player.setObjectName(u"player")
        player.resize(785, 43)
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(player.sizePolicy().hasHeightForWidth())
        player.setSizePolicy(sizePolicy)
        self.gridLayout_2 = QGridLayout(player)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.player_frm = QFrame(player)
        self.player_frm.setObjectName(u"player_frm")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.player_frm.sizePolicy().hasHeightForWidth())
        self.player_frm.setSizePolicy(sizePolicy1)
        self.gridLayout = QGridLayout(self.player_frm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.lead_chk = QCheckBox(self.player_frm)
        self.lead_chk.setObjectName(u"lead_chk")

        self.gridLayout.addWidget(self.lead_chk, 0, 3, 1, 1)

        self.plyr_score_edit = QLineEdit(self.player_frm)
        self.plyr_score_edit.setObjectName(u"plyr_score_edit")
        sizePolicy2 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(150)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.plyr_score_edit.sizePolicy().hasHeightForWidth())
        self.plyr_score_edit.setSizePolicy(sizePolicy2)
        self.plyr_score_edit.setMinimumSize(QSize(150, 0))

        self.gridLayout.addWidget(self.plyr_score_edit, 0, 7, 1, 2)

        self.remove_player = QPushButton(self.player_frm)
        self.remove_player.setObjectName(u"remove_player")

        self.gridLayout.addWidget(self.remove_player, 0, 11, 1, 1)

        self.label = QLabel(self.player_frm)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 6, 1, 1)

        self.win_chk = QCheckBox(self.player_frm)
        self.win_chk.setObjectName(u"win_chk")

        self.gridLayout.addWidget(self.win_chk, 0, 2, 1, 1)

        self.horizontalSpacer = QSpacerItem(220, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 1, 7, 1, 2)

        self.label_2 = QLabel(self.player_frm)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.label_2, 0, 4, 1, 1)

        self.plyr_name_edit = QLineEdit(self.player_frm)
        self.plyr_name_edit.setObjectName(u"plyr_name_edit")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.plyr_name_edit.sizePolicy().hasHeightForWidth())
        self.plyr_name_edit.setSizePolicy(sizePolicy3)
        self.plyr_name_edit.setMinimumSize(QSize(70, 0))

        self.gridLayout.addWidget(self.plyr_name_edit, 0, 5, 1, 1)


        self.gridLayout_2.addWidget(self.player_frm, 0, 0, 1, 1)


        self.retranslateUi(player)

        QMetaObject.connectSlotsByName(player)
    # setupUi

    def retranslateUi(self, player):
        player.setWindowTitle(QCoreApplication.translate("player", u"Form", None))
        self.lead_chk.setText(QCoreApplication.translate("player", u"Lead", None))
        self.remove_player.setText(QCoreApplication.translate("player", u"  X  ", None))
        self.label.setText(QCoreApplication.translate("player", u"Score: ---", None))
        self.win_chk.setText(QCoreApplication.translate("player", u"Win", None))
        self.label_2.setText(QCoreApplication.translate("player", u"Name", None))
    # retranslateUi

