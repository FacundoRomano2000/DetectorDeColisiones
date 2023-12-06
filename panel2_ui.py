# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'panel2.ui'
##
## Created by: Qt User Interface Compiler version 6.0.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(626, 281)
        self.gridLayout_2 = QGridLayout(Widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 4, 6, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 4, 3, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 0, 6, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.Seleccionarcamara = QLabel(Widget)
        self.Seleccionarcamara.setObjectName(u"Seleccionarcamara")

        self.verticalLayout_2.addWidget(self.Seleccionarcamara)

        self.Margenruido = QLabel(Widget)
        self.Margenruido.setObjectName(u"Margenruido")

        self.verticalLayout_2.addWidget(self.Margenruido)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Seleccionarcamara1 = QLineEdit(Widget)
        self.Seleccionarcamara1.setObjectName(u"Seleccionarcamara1")

        self.verticalLayout.addWidget(self.Seleccionarcamara1)

        self.Margenruido1 = QLineEdit(Widget)
        self.Margenruido1.setObjectName(u"Margenruido1")

        self.verticalLayout.addWidget(self.Margenruido1)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 4, 0, 1, 3)

        self.pbFinalizar = QPushButton(Widget)
        self.pbFinalizar.setObjectName(u"pbFinalizar")

        self.gridLayout_2.addWidget(self.pbFinalizar, 5, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 2, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 4, 5, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_5, 5, 0, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 4, 4, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pbGrabar = QPushButton(Widget)
        self.pbGrabar.setObjectName(u"pbGrabar")

        self.horizontalLayout.addWidget(self.pbGrabar)

        self.pbAbrir = QPushButton(Widget)
        self.pbAbrir.setObjectName(u"pbAbrir")

        self.horizontalLayout.addWidget(self.pbAbrir)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 4)

        self.pbComenzar = QPushButton(Widget)
        self.pbComenzar.setObjectName(u"pbComenzar")

        self.gridLayout_2.addWidget(self.pbComenzar, 5, 1, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.Seleccionarcamara.setText(QCoreApplication.translate("Widget", u"Seleccionar camara:", None))
        self.Margenruido.setText(QCoreApplication.translate("Widget", u"Margen de ruido:", None))
        self.pbFinalizar.setText(QCoreApplication.translate("Widget", u"Finalizar", None))
        self.pbGrabar.setText(QCoreApplication.translate("Widget", u"Grabar audio", None))
        self.pbAbrir.setText(QCoreApplication.translate("Widget", u"Abrir archivo", None))
        self.pbComenzar.setText(QCoreApplication.translate("Widget", u"Comenzar", None))
    # retranslateUi

