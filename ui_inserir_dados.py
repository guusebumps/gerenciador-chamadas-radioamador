# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'inserir_dados.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_InsertWindow(object):
    def setupUi(self, InsertWindow):
        if not InsertWindow.objectName():
            InsertWindow.setObjectName(u"InsertWindow")
        InsertWindow.resize(676, 890)
        InsertWindow.setMinimumSize(QSize(676, 890))
        InsertWindow.setMaximumSize(QSize(16777215, 16777215))
        self.centralwidget = QWidget(InsertWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(0, 0))
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(0, 0))
        self.frame.setMaximumSize(QSize(6526262, 16777215))
        self.frame.setStyleSheet(u"background-color: rgb(204, 204, 204);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(150, 0))
        self.frame_2.setMaximumSize(QSize(150, 16777215))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(16777215, 240))
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_8)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.frame_8)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_4.addWidget(self.label_4)

        self.line_3 = QFrame(self.frame_8)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_3)


        self.verticalLayout_3.addWidget(self.frame_8)

        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"padding: 5px 25px;\n"
"font-size: 24px;\n"
"text-align: center;\n"
"color: #fff;\n"
"background-color: #4CAF50;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color: green;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"  background-color: #3e8e41;\n"
"}")
        icon = QIcon()
        icon.addFile(u"Icons/Setapratras-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(25, 15))

        self.verticalLayout_3.addWidget(self.pushButton_2)


        self.horizontalLayout.addWidget(self.frame_2)

        self.line_2 = QFrame(self.frame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 25))
        self.label_5.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"font-size:18px;\n"
"font-weight: bold;\n"
"")

        self.verticalLayout_2.addWidget(self.label_5)

        self.lineEdit_4 = QLineEdit(self.frame_4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"\n"
"QLineEdit{\n"
"font-size: 20px;\n"
"text-align: center;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_2.addWidget(self.lineEdit_4)

        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 30))
        self.label_2.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"font-size:18px;\n"
"font-weight: bold;\n"
"")

        self.verticalLayout_2.addWidget(self.label_2)

        self.lineEdit_2 = QLineEdit(self.frame_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"\n"
"QLineEdit{\n"
"font-size: 20px;\n"
"text-align: center;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_2.addWidget(self.lineEdit_2)

        self.label_3 = QLabel(self.frame_4)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 25))
        self.label_3.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"font-size:18px;\n"
"font-weight: bold;\n"
"")

        self.verticalLayout_2.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.frame_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"\n"
"QLineEdit{\n"
"font-size: 20px;\n"
"text-align: center;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_2.addWidget(self.lineEdit_3)

        self.label_6 = QLabel(self.frame_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 25))
        self.label_6.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"font-size:18px;\n"
"font-weight: bold;\n"
"")

        self.verticalLayout_2.addWidget(self.label_6)

        self.lineEdit_5 = QLineEdit(self.frame_4)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"\n"
"QLineEdit{\n"
"font-size: 20px;\n"
"text-align: center;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_2.addWidget(self.lineEdit_5)

        self.label_7 = QLabel(self.frame_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 25))
        self.label_7.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"font-size:18px;\n"
"font-weight: bold;\n"
"")

        self.verticalLayout_2.addWidget(self.label_7)

        self.lineEdit_6 = QLineEdit(self.frame_4)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"\n"
"QLineEdit{\n"
"font-size: 20px;\n"
"text-align: center;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_2.addWidget(self.lineEdit_6)

        self.label_8 = QLabel(self.frame_4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 25))
        self.label_8.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"font-size:18px;\n"
"font-weight: bold;\n"
"")

        self.verticalLayout_2.addWidget(self.label_8)

        self.lineEdit_7 = QLineEdit(self.frame_4)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setStyleSheet(u"\n"
"QLineEdit{\n"
"font-size: 20px;\n"
"text-align: center;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_2.addWidget(self.lineEdit_7)

        self.label_9 = QLabel(self.frame_4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 25))
        self.label_9.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"font-size:18px;\n"
"font-weight: bold;\n"
"")

        self.verticalLayout_2.addWidget(self.label_9)

        self.lineEdit_8 = QLineEdit(self.frame_4)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setStyleSheet(u"\n"
"QLineEdit{\n"
"font-size: 20px;\n"
"text-align: center;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_2.addWidget(self.lineEdit_8)

        self.label_10 = QLabel(self.frame_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 25))
        self.label_10.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"font-size:18px;\n"
"font-weight: bold;\n"
"")

        self.verticalLayout_2.addWidget(self.label_10)

        self.lineEdit_9 = QLineEdit(self.frame_4)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setStyleSheet(u"\n"
"QLineEdit{\n"
"font-size: 20px;\n"
"text-align: center;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_2.addWidget(self.lineEdit_9)

        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 25))
        self.label_11.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"font-size:18px;\n"
"font-weight: bold;\n"
"")

        self.verticalLayout_2.addWidget(self.label_11)

        self.lineEdit_10 = QLineEdit(self.frame_4)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setStyleSheet(u"\n"
"QLineEdit{\n"
"font-size: 20px;\n"
"text-align: center;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_2.addWidget(self.lineEdit_10)

        self.label_12 = QLabel(self.frame_4)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 25))
        self.label_12.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"font-size:18px;\n"
"font-weight: bold;\n"
"")

        self.verticalLayout_2.addWidget(self.label_12)

        self.lineEdit_11 = QLineEdit(self.frame_4)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setStyleSheet(u"\n"
"QLineEdit{\n"
"font-size: 20px;\n"
"text-align: center;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_2.addWidget(self.lineEdit_11)

        self.label_13 = QLabel(self.frame_4)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMaximumSize(QSize(16777215, 25))
        self.label_13.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"font-size:18px;\n"
"font-weight: bold;\n"
"")

        self.verticalLayout_2.addWidget(self.label_13)

        self.lineEdit_12 = QLineEdit(self.frame_4)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        self.lineEdit_12.setStyleSheet(u"\n"
"QLineEdit{\n"
"font-size: 20px;\n"
"text-align: center;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_2.addWidget(self.lineEdit_12)

        self.label_14 = QLabel(self.frame_4)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"background-color: rgb(204, 204, 204);\n"
"font-size:18px;\n"
"font-weight: bold;\n"
"")

        self.verticalLayout_2.addWidget(self.label_14)

        self.lineEdit_13 = QLineEdit(self.frame_4)
        self.lineEdit_13.setObjectName(u"lineEdit_13")
        self.lineEdit_13.setStyleSheet(u"\n"
"QLineEdit{\n"
"font-size: 20px;\n"
"text-align: center;\n"
"border-radius: 10px;\n"
"background-color: rgb(255, 255, 255);\n"
"}")

        self.verticalLayout_2.addWidget(self.lineEdit_13)

        self.line = QFrame(self.frame_4)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 70))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMaximumSize(QSize(50, 16777215))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_6)

        self.pushButton = QPushButton(self.frame_5)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"padding: 5px 25px;\n"
"font-size: 24px;\n"
"text-align: center;\n"
"color: #fff;\n"
"background-color: #4CAF50;\n"
"border-radius: 15px;\n"
"}\n"
"\n"
"\n"
"QPushButton:hover{\n"
"background-color: green;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton:pressed{\n"
"  background-color: #3e8e41;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"Icons/InserirIcon-removebg-preview-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(40, 25))

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(50, 16777215))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_7)


        self.verticalLayout_2.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMinimumSize(QSize(0, 0))
        self.frame_3.setMaximumSize(QSize(150, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.frame)

        InsertWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(InsertWindow)

        QMetaObject.connectSlotsByName(InsertWindow)
    # setupUi

    def retranslateUi(self, InsertWindow):
        InsertWindow.setWindowTitle(QCoreApplication.translate("InsertWindow", u"Inserir dados", None))
        self.label_4.setText(QCoreApplication.translate("InsertWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Inserir</span></p><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">dados</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("InsertWindow", u"Voltar", None))
        self.label_5.setText(QCoreApplication.translate("InsertWindow", u"Q S O  N\u00ba.", None))
        self.label_2.setText(QCoreApplication.translate("InsertWindow", u"DATA", None))
        self.label_3.setText(QCoreApplication.translate("InsertWindow", u"PREFIXO", None))
        self.label_6.setText(QCoreApplication.translate("InsertWindow", u"Hora (In\u00edcio)", None))
        self.label_7.setText(QCoreApplication.translate("InsertWindow", u"Hora (Fim)", None))
        self.label_8.setText(QCoreApplication.translate("InsertWindow", u"Frequ\u00eancia ou Faixa", None))
        self.label_9.setText(QCoreApplication.translate("InsertWindow", u"Fonia ou CW", None))
        self.label_10.setText(QCoreApplication.translate("InsertWindow", u"R S T (Enviado)", None))
        self.label_11.setText(QCoreApplication.translate("InsertWindow", u"R S T (Recebido)", None))
        self.label_12.setText(QCoreApplication.translate("InsertWindow", u"Q S L (Enviado)", None))
        self.label_13.setText(QCoreApplication.translate("InsertWindow", u"Q S L (Recebido)", None))
        self.label_14.setText(QCoreApplication.translate("InsertWindow", u"Outras Anota\u00e7\u00f5es", None))
        self.pushButton.setText(QCoreApplication.translate("InsertWindow", u"Inserir", None))
    # retranslateUi

