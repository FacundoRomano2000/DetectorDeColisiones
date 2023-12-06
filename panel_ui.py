# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'panel.ui'
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

        self.gbResumen = QGroupBox(Widget)
        self.gbResumen.setObjectName(u"gbResumen")
        self.gridLayout = QGridLayout(self.gbResumen)
        self.gridLayout.setObjectName(u"gridLayout")
        self.lAmplMaxima = QLabel(self.gbResumen)
        self.lAmplMaxima.setObjectName(u"lAmplMaxima")

        self.gridLayout.addWidget(self.lAmplMaxima, 2, 0, 1, 1)

        self.lCantMuestras = QLabel(self.gbResumen)
        self.lCantMuestras.setObjectName(u"lCantMuestras")

        self.gridLayout.addWidget(self.lCantMuestras, 0, 0, 1, 1)

        self.lFrecMuestreo = QLabel(self.gbResumen)
        self.lFrecMuestreo.setObjectName(u"lFrecMuestreo")

        self.gridLayout.addWidget(self.lFrecMuestreo, 1, 0, 1, 1)

        self.lAmplMinima = QLabel(self.gbResumen)
        self.lAmplMinima.setObjectName(u"lAmplMinima")

        self.gridLayout.addWidget(self.lAmplMinima, 3, 0, 1, 1)


        self.gridLayout_2.addWidget(self.gbResumen, 1, 6, 3, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 0, 6, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lDesdeLaMuestra = QLabel(Widget)
        self.lDesdeLaMuestra.setObjectName(u"lDesdeLaMuestra")

        self.verticalLayout_2.addWidget(self.lDesdeLaMuestra)

        self.lCantMuestrasGraficadas = QLabel(Widget)
        self.lCantMuestrasGraficadas.setObjectName(u"lCantMuestrasGraficadas")

        self.verticalLayout_2.addWidget(self.lCantMuestrasGraficadas)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.leDesdeLaMuestra = QLineEdit(Widget)
        self.leDesdeLaMuestra.setObjectName(u"leDesdeLaMuestra")

        self.verticalLayout.addWidget(self.leDesdeLaMuestra)

        self.leCantMuestrasGraficadas = QLineEdit(Widget)
        self.leCantMuestrasGraficadas.setObjectName(u"leCantMuestrasGraficadas")

        self.verticalLayout.addWidget(self.leCantMuestrasGraficadas)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 4, 0, 1, 3)

        self.pbGraficar = QPushButton(Widget)
        self.pbGraficar.setObjectName(u"pbGraficar")

        self.gridLayout_2.addWidget(self.pbGraficar, 5, 2, 1, 1)

        self.checkSuavizar = QCheckBox(Widget)
        self.checkSuavizar.setObjectName(u"checkSuavizar")

        self.gridLayout_2.addWidget(self.checkSuavizar, 3, 0, 1, 1)

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

        self.pbCargar = QPushButton(Widget)
        self.pbCargar.setObjectName(u"pbCargar")

        self.horizontalLayout.addWidget(self.pbCargar)


        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 4)

        self.pbReproducir = QPushButton(Widget)
        self.pbReproducir.setObjectName(u"pbReproducir")

        self.gridLayout_2.addWidget(self.pbReproducir, 5, 1, 1, 1)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.gbResumen.setTitle(QCoreApplication.translate("Widget", u"Resumen", None))
        self.lAmplMaxima.setText(QCoreApplication.translate("Widget", u".", None))
        self.lCantMuestras.setText(QCoreApplication.translate("Widget", u".", None))
        self.lFrecMuestreo.setText(QCoreApplication.translate("Widget", u".", None))
        self.lAmplMinima.setText(QCoreApplication.translate("Widget", u".", None))
        self.lDesdeLaMuestra.setText(QCoreApplication.translate("Widget", u"Seleccionar camara", None))
        self.lCantMuestrasGraficadas.setText(QCoreApplication.translate("Widget", u"Color verde", None))
        self.pbGraficar.setText(QCoreApplication.translate("Widget", u"Graficar", None))
        self.checkSuavizar.setText(QCoreApplication.translate("Widget", u"Suavizar", None))
        self.pbGrabar.setText(QCoreApplication.translate("Widget", u"Mostrar", None))
        self.pbCargar.setText(QCoreApplication.translate("Widget", u"Cargar", None))
        self.pbReproducir.setText(QCoreApplication.translate("Widget", u"Comenzar", None))
    # retranslateUi

