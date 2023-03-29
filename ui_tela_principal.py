# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_principal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 768)
        MainWindow.setMinimumSize(QSize(1024, 768))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        icon = QIcon()
        icon.addFile(u"Icons/icone.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"background-color: rgb(202, 202, 194);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(200, 16777215))
        self.frame_3.setStyleSheet(u"background-color: rgb(202, 202, );")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 60))
        self.label.setStyleSheet(u"font-size:25px;\n"
"font-weight: bold;\n"
"")

        self.verticalLayout_3.addWidget(self.label)

        self.lineEdit = QLineEdit(self.frame_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"  font-size: 20px;\n"
"  text-align: center;\n"
"  border-radius: 10px;\n"
"\n"
"}")

        self.verticalLayout_3.addWidget(self.lineEdit)

        self.radioButton = QRadioButton(self.frame_3)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setStyleSheet(u"font-size:15px;\n"
"font-weight: bold;\n"
"")

        self.verticalLayout_3.addWidget(self.radioButton)

        self.radioButton_6 = QRadioButton(self.frame_3)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setStyleSheet(u"font-size:15px;\n"
"font-weight: bold;\n"
"")

        self.verticalLayout_3.addWidget(self.radioButton_6)

        self.radioButton_2 = QRadioButton(self.frame_3)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setStyleSheet(u"font-size:15px;\n"
"font-weight: bold;\n"
"")

        self.verticalLayout_3.addWidget(self.radioButton_2)

        self.radioButton_3 = QRadioButton(self.frame_3)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setStyleSheet(u"font-size:15px;\n"
"font-weight: bold;\n"
"")

        self.verticalLayout_3.addWidget(self.radioButton_3)

        self.radioButton_4 = QRadioButton(self.frame_3)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setStyleSheet(u"font-size:15px;\n"
"font-weight: bold;\n"
"")

        self.verticalLayout_3.addWidget(self.radioButton_4)

        self.radioButton_7 = QRadioButton(self.frame_3)
        self.radioButton_7.setObjectName(u"radioButton_7")
        self.radioButton_7.setStyleSheet(u"font-size:15px;\n"
"font-weight: bold;\n"
"")

        self.verticalLayout_3.addWidget(self.radioButton_7)

        self.radioButton_8 = QRadioButton(self.frame_3)
        self.radioButton_8.setObjectName(u"radioButton_8")
        self.radioButton_8.setStyleSheet(u"font-size:15px;\n"
"font-weight: bold;\n"
"")

        self.verticalLayout_3.addWidget(self.radioButton_8)

        self.radioButton_9 = QRadioButton(self.frame_3)
        self.radioButton_9.setObjectName(u"radioButton_9")
        self.radioButton_9.setStyleSheet(u"font-size:15px;\n"
"font-weight: bold;\n"
"")

        self.verticalLayout_3.addWidget(self.radioButton_9)

        self.radioButton_10 = QRadioButton(self.frame_3)
        self.radioButton_10.setObjectName(u"radioButton_10")
        self.radioButton_10.setStyleSheet(u"font-size:15px;\n"
"font-weight: bold;\n"
"")

        self.verticalLayout_3.addWidget(self.radioButton_10)

        self.radioButton_11 = QRadioButton(self.frame_3)
        self.radioButton_11.setObjectName(u"radioButton_11")
        self.radioButton_11.setStyleSheet(u"font-size:15px;\n"
"font-weight: bold;\n"
"")

        self.verticalLayout_3.addWidget(self.radioButton_11)

        self.radioButton_12 = QRadioButton(self.frame_3)
        self.radioButton_12.setObjectName(u"radioButton_12")
        self.radioButton_12.setStyleSheet(u"font-size:15px;\n"
"font-weight: bold;\n"
"")

        self.verticalLayout_3.addWidget(self.radioButton_12)

        self.radioButton_5 = QRadioButton(self.frame_3)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setStyleSheet(u"font-size:15px;\n"
"font-weight: bold;\n"
"")

        self.verticalLayout_3.addWidget(self.radioButton_5)

        self.pushButton_7 = QPushButton(self.frame_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setMinimumSize(QSize(50, 50))
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"  padding: 15px 25px;\n"
"  font-size: 24px;\n"
"  text-align: center;\n"
"  color: #fff;\n"
"  background-color: #4CAF50;\n"
"  border-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: green;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color: #3e8e41;\n"
"\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"Icons/searchicon-removebg-preview-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setIconSize(QSize(25, 25))

        self.verticalLayout_3.addWidget(self.pushButton_7)

        self.line_3 = QFrame(self.frame_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_3.addWidget(self.line_3)


        self.horizontalLayout.addWidget(self.frame_3)

        self.line_2 = QFrame(self.frame_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.horizontalLayout.addWidget(self.line_2)

        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"background-color: rgb(202, 202, 194);")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tableWidget = QTableWidget(self.frame_4)
        if (self.tableWidget.columnCount() < 13):
            self.tableWidget.setColumnCount(13)
        font = QFont()
        font.setFamily(u"Times New Roman")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        self.tableWidget.setObjectName(u"tableWidget")
        font1 = QFont()
        font1.setPointSize(14)
        self.tableWidget.setFont(font1)
        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(110)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(110)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)

        self.verticalLayout_4.addWidget(self.tableWidget)


        self.horizontalLayout.addWidget(self.frame_4)

        self.frame_4.raise_()
        self.frame_3.raise_()
        self.line_2.raise_()

        self.verticalLayout.addWidget(self.frame_2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(9898989, 120))
        self.frame.setStyleSheet(u"background-color: rgb(202, 202, 194);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(200, 16777215))
        self.frame_5.setStyleSheet(u"background-color: rgb(202, 202, 194);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_5 = QPushButton(self.frame_5)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(50, 80))
        font2 = QFont()
        self.pushButton_5.setFont(font2)
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"  padding: 15px 25px;\n"
"  font-size: 16px;\n"
"  text-align: center;\n"
"  color: #fff;\n"
"  background-color: #4CAF50;\n"
"  border-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: green;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color: #3e8e41;\n"
"\n"
"}")
        self.pushButton_5.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.pushButton_5)


        self.horizontalLayout_2.addWidget(self.frame_5)

        self.frame_6 = QFrame(self.frame)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color: rgb(202, 202, 194);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.pushButton_2 = QPushButton(self.frame_6)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(50, 50))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"  padding: 15px 25px;\n"
"  font-size: 24px;\n"
"  text-align: center;\n"
"  color: #fff;\n"
"  background-color: #4CAF50;\n"
"  border-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: blue;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color: #3e8e41;\n"
"\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"Icons/InserirIcon-removebg-preview-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(50, 20))

        self.horizontalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_6)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(50, 50))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"  padding: 15px 25px;\n"
"  font-size: 24px;\n"
"  text-align: center;\n"
"  color: #fff;\n"
"  background-color: #4CAF50;\n"
"  border-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: orange;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color: #3e8e41;\n"
"\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"Icons/updateicon-removebg-preview-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon3)
        self.pushButton_3.setIconSize(QSize(60, 25))

        self.horizontalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_6)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(50, 50))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"  padding: 15px 25px;\n"
"  font-size: 24px;\n"
"  text-align: center;\n"
"  color: #fff;\n"
"  background-color: #4CAF50;\n"
"  border-radius: 15px;\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: red;\n"
"\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"  background-color: #3e8e41;\n"
"\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"Icons/deleteicon-removebg-preview-removebg-preview.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setIconSize(QSize(50, 25))

        self.horizontalLayout_3.addWidget(self.pushButton_4)


        self.horizontalLayout_2.addWidget(self.frame_6)


        self.verticalLayout.addWidget(self.frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Gerenciador de matriculas", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">Gerenciamento </span></p><p><span style=\" font-size:14pt;\">de chamadas</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.radioButton.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Pesquisar por id do aluno. (Valores v\u00e1lidos: id entre 1 e 300).</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton.setText(QCoreApplication.translate("MainWindow", u"Q S O  N.\u00ba", None))
#if QT_CONFIG(tooltip)
        self.radioButton_6.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Pesquisa pelo nome do aluno.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_6.setText(QCoreApplication.translate("MainWindow", u"Data", None))
#if QT_CONFIG(tooltip)
        self.radioButton_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Pesquisar por matricula ativa. (Valores v\u00e1lidos: 1 e 0)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_2.setText(QCoreApplication.translate("MainWindow", u"Prefixo", None))
#if QT_CONFIG(tooltip)
        self.radioButton_3.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Pesquisar por tipo da matr\u00edcula. (Valores v\u00e1lidos: 30, 90, 180, 360.)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_3.setText(QCoreApplication.translate("MainWindow", u"Hora(In\u00edcio)", None))
#if QT_CONFIG(tooltip)
        self.radioButton_4.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Pesquisar por data de inicio. (Formato v\u00e1lido: AAAA-MM-DD)</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_4.setText(QCoreApplication.translate("MainWindow", u"Hora(Fim)", None))
        self.radioButton_7.setText(QCoreApplication.translate("MainWindow", u"Frequ\u00eancia ou Faixa", None))
        self.radioButton_8.setText(QCoreApplication.translate("MainWindow", u"Fonia ou CW", None))
        self.radioButton_9.setText(QCoreApplication.translate("MainWindow", u"R S T (Enviado)", None))
        self.radioButton_10.setText(QCoreApplication.translate("MainWindow", u"R S T (Recebido)", None))
        self.radioButton_11.setText(QCoreApplication.translate("MainWindow", u"Q S L (Enviado)", None))
        self.radioButton_12.setText(QCoreApplication.translate("MainWindow", u"Q S L (Recebido)", None))
#if QT_CONFIG(tooltip)
        self.radioButton_5.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Pesuisar todos os registros de alunos.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.radioButton_5.setText(QCoreApplication.translate("MainWindow", u"Todos os registros", None))
#if QT_CONFIG(tooltip)
        self.pushButton_7.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Bot\u00e3o pesquisar. A pesquisa \u00e9 feita de acordo com o tipo de pesquisa selecionado acima.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(whatsthis)
        self.pushButton_7.setWhatsThis("")
#endif // QT_CONFIG(whatsthis)
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Pesquisar", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Q S O \n"
"   N\u00ba.", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"DATA", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"PREFIXO", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"HORA \n"
"IN\u00cdCIO", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"HORA \n"
" FIM", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"FREQ. \n"
"  ou \n"
"FAIXA", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"FONIA \n"
"   ou \n"
"  CW", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"RST\n"
"ENV.", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"RST \n"
"REC.", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Q S L \n"
" ENV.", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Q S L \n"
" REC.", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"  OUTRAS \n"
"ANOTA\u00c7\u00d5ES", None));
#if QT_CONFIG(tooltip)
        self.pushButton_5.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Bot\u00e3o voltar. Volta ao modulo inicial.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Gerar Excel", None))
#if QT_CONFIG(tooltip)
        self.pushButton_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Bot\u00e3o inserir. Abre uma nova janela para a inser\u00e7\u00e3o de registros.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Inserir", None))
#if QT_CONFIG(tooltip)
        self.pushButton_3.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Bot\u00e3o alterar. Abre uma nova janela para altera\u00e7\u00e3o de registros.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
#if QT_CONFIG(tooltip)
        self.pushButton_4.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Bot\u00e3o excluir. Abre uma nova janela para e exclus\u00e3o de registros.</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
    # retranslateUi

