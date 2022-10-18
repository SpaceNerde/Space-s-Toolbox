# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(142, 160)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QSize(142, 160))
        Form.setMaximumSize(QSize(142, 160))
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(10, 10, 121, 141))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.button_2 = QPushButton(self.gridLayoutWidget)
        self.button_2.setObjectName(u"button_2")

        self.gridLayout.addWidget(self.button_2, 2, 1, 1, 1)

        self.button_1 = QPushButton(self.gridLayoutWidget)
        self.button_1.setObjectName(u"button_1")

        self.gridLayout.addWidget(self.button_1, 2, 0, 1, 1)

        self.button_7 = QPushButton(self.gridLayoutWidget)
        self.button_7.setObjectName(u"button_7")

        self.gridLayout.addWidget(self.button_7, 4, 0, 1, 1)

        self.screen = QLineEdit(self.gridLayoutWidget)
        self.screen.setObjectName(u"screen")
        self.screen.setLayoutDirection(Qt.RightToLeft)
        self.screen.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.gridLayout.addWidget(self.screen, 1, 0, 1, 3)

        self.button_dot = QPushButton(self.gridLayoutWidget)
        self.button_dot.setObjectName(u"button_dot")

        self.gridLayout.addWidget(self.button_dot, 5, 2, 1, 1)

        self.button_0 = QPushButton(self.gridLayoutWidget)
        self.button_0.setObjectName(u"button_0")

        self.gridLayout.addWidget(self.button_0, 5, 1, 1, 1)

        self.button_ce = QPushButton(self.gridLayoutWidget)
        self.button_ce.setObjectName(u"button_ce")

        self.gridLayout.addWidget(self.button_ce, 5, 0, 1, 1)

        self.button_6 = QPushButton(self.gridLayoutWidget)
        self.button_6.setObjectName(u"button_6")

        self.gridLayout.addWidget(self.button_6, 3, 2, 1, 1)

        self.button_3 = QPushButton(self.gridLayoutWidget)
        self.button_3.setObjectName(u"button_3")

        self.gridLayout.addWidget(self.button_3, 2, 2, 1, 1)

        self.button_4 = QPushButton(self.gridLayoutWidget)
        self.button_4.setObjectName(u"button_4")

        self.gridLayout.addWidget(self.button_4, 3, 0, 1, 1)

        self.button_8 = QPushButton(self.gridLayoutWidget)
        self.button_8.setObjectName(u"button_8")

        self.gridLayout.addWidget(self.button_8, 4, 1, 1, 1)

        self.button_9 = QPushButton(self.gridLayoutWidget)
        self.button_9.setObjectName(u"button_9")

        self.gridLayout.addWidget(self.button_9, 4, 2, 1, 1)

        self.button_5 = QPushButton(self.gridLayoutWidget)
        self.button_5.setObjectName(u"button_5")

        self.gridLayout.addWidget(self.button_5, 3, 1, 1, 1)

        self.button_div = QPushButton(self.gridLayoutWidget)
        self.button_div.setObjectName(u"button_div")

        self.gridLayout.addWidget(self.button_div, 2, 3, 1, 1)

        self.button_mul = QPushButton(self.gridLayoutWidget)
        self.button_mul.setObjectName(u"button_mul")

        self.gridLayout.addWidget(self.button_mul, 3, 3, 1, 1)

        self.button_minus = QPushButton(self.gridLayoutWidget)
        self.button_minus.setObjectName(u"button_minus")

        self.gridLayout.addWidget(self.button_minus, 4, 3, 1, 1)

        self.button_plus = QPushButton(self.gridLayoutWidget)
        self.button_plus.setObjectName(u"button_plus")

        self.gridLayout.addWidget(self.button_plus, 5, 3, 1, 1)

        self.button_equals = QPushButton(self.gridLayoutWidget)
        self.button_equals.setObjectName(u"button_equals")

        self.gridLayout.addWidget(self.button_equals, 1, 3, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Calculator", None))
        self.button_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.button_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.button_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.screen.setText("")
        self.button_dot.setText(QCoreApplication.translate("Form", u".", None))
        self.button_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.button_ce.setText(QCoreApplication.translate("Form", u"CE", None))
        self.button_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.button_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.button_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.button_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.button_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.button_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.button_div.setText(QCoreApplication.translate("Form", u"/", None))
        self.button_mul.setText(QCoreApplication.translate("Form", u"*", None))
        self.button_minus.setText(QCoreApplication.translate("Form", u"-", None))
        self.button_plus.setText(QCoreApplication.translate("Form", u"+", None))
        self.button_equals.setText(QCoreApplication.translate("Form", u"=", None))
    # retranslateUi

