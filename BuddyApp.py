# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Principal.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):

    def __init__(self, _listaProcesos):
        self.listaProcesos = _listaProcesos
        self.memoriaPrincipal = None

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(798, 584)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(0, 0))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/img/img/logoico.png"), QtGui.QIcon.Selected, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(270, 0, 521, 581))
        self.groupBox_2.setObjectName("groupBox_2")
        self.plainTextEditAcciones = QtWidgets.QPlainTextEdit(self.groupBox_2)
        self.plainTextEditAcciones.setGeometry(QtCore.QRect(0, 20, 521, 561))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.plainTextEditAcciones.setFont(font)
        self.plainTextEditAcciones.setReadOnly(True)
        self.plainTextEditAcciones.setObjectName("plainTextEditAcciones")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 10, 251, 121))
        self.label_9.setStyleSheet("border-image: url(:/img/img/logofin.png);")
        self.label_9.setObjectName("label_9")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 190, 261, 391))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 110, 241, 73))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineNombreProceso = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineNombreProceso.setObjectName("lineNombreProceso")
        self.gridLayout.addWidget(self.lineNombreProceso, 1, 1, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)
        self.lineTamProceso = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineTamProceso.setObjectName("lineTamProceso")
        self.gridLayout.addWidget(self.lineTamProceso, 2, 1, 1, 1)
        self.pushButtonAgregarNuevoProceso = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButtonAgregarNuevoProceso.setObjectName("pushButtonAgregarNuevoProceso")
        self.gridLayout.addWidget(self.pushButtonAgregarNuevoProceso, 2, 2, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 21, 241, 81))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_4.addWidget(self.label, 0, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_4.addWidget(self.label_3, 1, 0, 1, 1)
        self.lineEditCabalMemoriaPrincipal = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEditCabalMemoriaPrincipal.setObjectName("lineEditCabalMemoriaPrincipal")
        self.gridLayout_4.addWidget(self.lineEditCabalMemoriaPrincipal, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonMostrar = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButtonMostrar.setObjectName("pushButtonMostrar")
        self.horizontalLayout_2.addWidget(self.pushButtonMostrar)
        self.pushButtonNuevaMemoria = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButtonNuevaMemoria.setObjectName("pushButtonNuevaMemoria")
        self.horizontalLayout_2.addWidget(self.pushButtonNuevaMemoria)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget3 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget3.setGeometry(QtCore.QRect(10, 20, 241, 91))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget3)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_4 = QtWidgets.QGroupBox(self.layoutWidget3)
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(10, 60, 61, 21))
        self.label_10.setObjectName("label_10")
        self.layoutWidget4 = QtWidgets.QWidget(self.groupBox_4)
        self.layoutWidget4.setGeometry(QtCore.QRect(10, 20, 101, 34))
        self.layoutWidget4.setObjectName("layoutWidget4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget4)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_6 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 0, 1, 1)
        self.labelInfoCabal = QtWidgets.QLabel(self.layoutWidget4)
        self.labelInfoCabal.setObjectName("labelInfoCabal")
        self.gridLayout_3.addWidget(self.labelInfoCabal, 0, 1, 1, 2)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget4)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)
        self.labelInfoTam = QtWidgets.QLabel(self.layoutWidget4)
        self.labelInfoTam.setObjectName("labelInfoTam")
        self.gridLayout_3.addWidget(self.labelInfoTam, 1, 1, 1, 2)
        self.gridLayout_2.addWidget(self.groupBox_4, 1, 0, 2, 1)
        self.pushButtonAgregarMP = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButtonAgregarMP.setEnabled(True)
        self.pushButtonAgregarMP.setObjectName("pushButtonAgregarMP")
        self.gridLayout_2.addWidget(self.pushButtonAgregarMP, 1, 1, 1, 1)
        self.pushButtonSacarMP = QtWidgets.QPushButton(self.layoutWidget3)
        self.pushButtonSacarMP.setObjectName("pushButtonSacarMP")
        self.gridLayout_2.addWidget(self.pushButtonSacarMP, 2, 1, 1, 1)
        self.comboBoxProcesos = QtWidgets.QComboBox(self.layoutWidget3)
        self.comboBoxProcesos.setObjectName("comboBoxProcesos")
        self.gridLayout_2.addWidget(self.comboBoxProcesos, 0, 0, 1, 2)
        self.layoutWidget5 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget5.setGeometry(QtCore.QRect(10, 121, 241, 61))
        self.layoutWidget5.setObjectName("layoutWidget5")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget5)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_7 = QtWidgets.QLabel(self.layoutWidget5)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonBL = QtWidgets.QPushButton(self.layoutWidget5)
        self.pushButtonBL.setObjectName("pushButtonBL")
        self.horizontalLayout.addWidget(self.pushButtonBL)
        self.pushButtonVL = QtWidgets.QPushButton(self.layoutWidget5)
        self.pushButtonVL.setObjectName("pushButtonVL")
        self.horizontalLayout.addWidget(self.pushButtonVL)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.pushButtonInfoApp = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonInfoApp.setGeometry(QtCore.QRect(10, 140, 251, 41))
        font = QtGui.QFont()
        font.setFamily("Blackadder ITC")
        font.setPointSize(18)
        self.pushButtonInfoApp.setFont(font)
        self.pushButtonInfoApp.setStyleSheet("background-color: rgb(255, 170, 0);")
        self.pushButtonInfoApp.setObjectName("pushButtonInfoApp")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        # Eventos
        self.lineNombreProceso.textChanged.connect(self.validar_nombre_nuevo_proceso)
        self.pushButtonAgregarNuevoProceso.clicked.connect(self.validar_creacion_proceso)
        self.comboBoxProcesos.currentIndexChanged.connect(self.info_proceso_seleccionado)
        self.pushButtonNuevaMemoria.clicked.connect(self.nueva_memoria_principal)
        self.pushButtonAgregarMP.clicked.connect(self.agregar_proceso_memoria_principal)
        self.pushButtonSacarMP.clicked.connect(self.sacar_proceso_memoria_principal)
        self.pushButtonMostrar.clicked.connect(self.mostrar_info_memoria)
        self.pushButtonBL.clicked.connect(self.mostrar_info_bloques_libres)
        self.pushButtonInfoApp.clicked.connect(self.mostrar_info_buddyapp)
        self.pushButtonVL.clicked.connect(self.mostrar_info_vector_libre)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BuddyApp"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Acciones"))
        self.label_9.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "Asignacion de Memoria y Creacion de Procesos"))
        self.label_4.setText(_translate("MainWindow", "Proceso:"))
        self.label_2.setText(_translate("MainWindow", "Nombre:"))
        self.label_5.setText(_translate("MainWindow", "Tamaño: "))
        self.pushButtonAgregarNuevoProceso.setText(_translate("MainWindow", "Agregar"))
        self.label.setText(_translate("MainWindow", "Memoria:"))
        self.label_3.setText(_translate("MainWindow", "Cabal:"))
        self.pushButtonMostrar.setText(_translate("MainWindow", "Mostrar"))
        self.pushButtonNuevaMemoria.setText(_translate("MainWindow", "Asignar"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Manejo de Procesos"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Info del Proceso"))
        self.label_10.setText(_translate("MainWindow", "Donde Esta?"))
        self.label_6.setText(_translate("MainWindow", "Cabal:"))
        self.labelInfoCabal.setText(_translate("MainWindow", "-"))
        self.label_8.setText(_translate("MainWindow", "Tamaño:"))
        self.labelInfoTam.setText(_translate("MainWindow", "-"))
        self.pushButtonAgregarMP.setText(_translate("MainWindow", "Llevar a MP"))
        self.pushButtonSacarMP.setText(_translate("MainWindow", "Llevar a MS"))
        self.label_7.setText(_translate("MainWindow", "Vector Libre:"))
        self.pushButtonBL.setText(_translate("MainWindow", "Mostrar Bloques Libres"))
        self.pushButtonVL.setText(_translate("MainWindow", "Mostrar Vector Libre"))
        self.pushButtonInfoApp.setText(_translate("MainWindow", "Sobre BuddyApp"))

    def mostrar_info_buddyapp(self):
        text = "" \
               "+----------------------------------------------------+\n" \
               "|               ¿Que es BuddyApp?                    |\n" \
               "| Es una app/simulador, que nos permite simular la   |\n" \
               "| administracion de memoria, utilizando el metodo de |\n" \
               "| buddy system.                                      |\n" \
               "| BuddyApp fue desarrollada a modo de trabajo final  |\n" \
               "| para la catedra de Sistemas Operativos de la       |\n" \
               "| carrera Ingenieria en Informatica de la facultad   |\n" \
               "| de Tecnologia y Ciencias Aplicadas de la UNCa.     |\n" \
               "|                                                    |\n" \
               "|                   Catedra:                         |\n" \
               "|              Sistemas Operativos                   |\n" \
               "|                                                    |\n" \
               "|               Jefe de Catedra:                     |\n" \
               "|             Lic. Juan Pablo Moreno                 |\n" \
               "|                                                    |\n" \
               "|           Jefe de Trabajos Practicos:              |\n" \
               "|             Lic. Manuel Baquinzay                  |\n" \
               "|                                                    |\n" \
               "|             Integrantes del Grupo:                 |\n" \
               "|          Flores, Dario Exequiel - 01228            |\n" \
               "|          Romero, Marcos Gabriel - 01190            |\n" \
               "|                                                    |\n" \
               "|                    Año:                            |\n" \
               "|                    2019                            |\n" \
               "|                                                    |\n" \
               "+----------------------------------------------------+\n"
        self.plainTextEditAcciones.appendPlainText(text)

    def closeEvent(self, event):
        resultado = QMessageBox.question(self, "Salir...", "¿Seguro que quieres salir de la aplicacion",
                                         QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

    def finInstruccion(self):
        self.plainTextEditAcciones.appendPlainText("\n######################################################\n")

    def validar_nombre_nuevo_proceso(self):
        nombre = self.lineNombreProceso.text()
        validar = nombre.isalnum()
        if nombre == "":
            self.lineNombreProceso.setStyleSheet("border: 1px solid yellow;")
            return False
        elif not validar:
            self.lineNombreProceso.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.lineNombreProceso.setStyleSheet("border: 1px solid green;")
            return True

    def validar_tam_nuevo_proceso(self):
        cabal = self.lineTamProceso.text()
        validar = cabal.isdigit()
        if cabal == "":
            self.lineTamProceso.setStyleSheet("border: 1px solid yellow;")
            return False
        elif not validar:
            self.lineTamProceso.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.lineTamProceso.setStyleSheet("border: 1px solid green;")
            return True

    def validar_cabal_nuevo_memoria_principal(self):
        cabal = self.lineEditCabalMemoriaPrincipal.text()
        validar = cabal.isdigit()
        if cabal == "":
            self.lineEditCabalMemoriaPrincipal.setStyleSheet("border: 1px solid yellow;")
            return False
        elif not validar:
            self.lineEditCabalMemoriaPrincipal.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.lineEditCabalMemoriaPrincipal.setStyleSheet("border: 1px solid green;")
            return True

    def validar_creacion_proceso(self):
        if self.validar_nombre_nuevo_proceso() and self.validar_tam_nuevo_proceso():
            nombre = self.lineNombreProceso.text()
            tam = self.lineTamProceso.text()
            if self.listaProcesos.buscarRepiteNombre(nombre):
                self.listaProcesos.agregarProceso(nombre, tam)
                proceso = self.listaProcesos.ultimoProceso()
                self.comboBoxProcesos.addItem(proceso.getNombre())
                text = "Se agrego el proceso:"
                self.plainTextEditAcciones.appendPlainText(text)
                self.plainTextEditAcciones.appendPlainText(proceso.info())
                self.finInstruccion()
                self.lineNombreProceso.clear()
                self.lineTamProceso.clear()
            else:
                QMessageBox.warning(self, "Formulario incorrecto", "Nombre Repetido", QMessageBox.Discard)
        else:
            QMessageBox.warning(self, "Formulario incorrecto", "Validación incorrecta", QMessageBox.Discard)

    def info_proceso_seleccionado(self):
        if len(self.listaProcesos.lista_procesos) != 0:
            i = self.comboBoxProcesos.currentIndex()
            proceso = self.listaProcesos.buscarXindice(i)
            self.labelInfoCabal.setText(proceso.getCabal())
            self.labelInfoTam.setText(proceso.getTamanio())
            if proceso.esta_en_memoria_principal():
                self.pushButtonAgregarMP.setEnabled(False)
                self.pushButtonSacarMP.setEnabled(True)
            else:
                self.pushButtonAgregarMP.setEnabled(True)
                self.pushButtonSacarMP.setEnabled(False)

    def nueva_memoria_principal(self):
        if self.validar_cabal_nuevo_memoria_principal():
            for p in self.listaProcesos.lista_procesos:
                p.particion = None
            if self.memoriaPrincipal is not None:
                self.info_proceso_seleccionado()
            kval = self.lineEditCabalMemoriaPrincipal.text()
            proceso = Proceso('Libre', kval)
            particion = Particion(kval, proceso, 0, None)
            self.memoriaPrincipal = Memoria(particion)
            text = self.memoriaPrincipal.imprimirMemoria()
            self.plainTextEditAcciones.appendPlainText(text)
            #self.pushButtonNuevaMemoria.setEnabled(False)
            self.finInstruccion()
            self.lineEditCabalMemoriaPrincipal.clear()
        else:
            QMessageBox.warning(self, "Formulario incorrecto", "Cabal tiene que ser Numerico", QMessageBox.Discard)

    def mostrar_info_memoria(self):
        text = self.memoriaPrincipal.imprimirMemoria()
        self.plainTextEditAcciones.appendPlainText(text)
        self.finInstruccion()

    def mostrar_info_bloques_libres(self):
        text = self.memoriaPrincipal.imprimirBL()
        self.plainTextEditAcciones.appendPlainText(text)
        self.finInstruccion()

    def mostrar_info_vector_libre(self):
        text = self.memoriaPrincipal.imprimirVL()
        self.plainTextEditAcciones.appendPlainText(text)
        self.finInstruccion()

    def agregar_proceso_memoria_principal(self):
        i = self.comboBoxProcesos.currentIndex()
        proceso = self.listaProcesos.buscarXindice(i)
        print(proceso.info())
        if self.memoriaPrincipal.agregar(proceso):
            text = "Se llevo a Memoria Principal el proceso:"
            self.plainTextEditAcciones.appendPlainText(text)
            self.plainTextEditAcciones.appendPlainText(proceso.info())
            text = self.memoriaPrincipal.imprimirMemoria()
            self.plainTextEditAcciones.appendPlainText(text)
        else:
            text = "NO hay espacio disponible para el proceso:"
            self.plainTextEditAcciones.appendPlainText(text)
            self.plainTextEditAcciones.appendPlainText(proceso.info())
        self.finInstruccion()
        self.info_proceso_seleccionado()

    def sacar_proceso_memoria_principal(self):
        i = self.comboBoxProcesos.currentIndex()
        proceso = self.listaProcesos.buscarXindice(i)
        print("accion" + proceso._nombre)
        self.memoriaPrincipal.sacar(proceso)
        text = "Se llevo a memoria secundaria el proceso:"
        self.plainTextEditAcciones.appendPlainText(text)
        self.plainTextEditAcciones.appendPlainText(proceso.info())
        text = self.memoriaPrincipal.imprimirMemoria()
        self.plainTextEditAcciones.appendPlainText(text)
        self.finInstruccion()
        self.info_proceso_seleccionado()


class Proceso:

    def __init__(self, nombre, cabal):
        self._nombre = nombre
        self._cabal = cabal
        self._tam = 2 ** int(cabal)
        self.particion = None

    def esta_en_memoria_principal(self):
        if self.particion is None:
            return False
        return True

    def getNombre(self):
        return str(self._nombre)

    def getCabal(self):
        return str(self._cabal)

    def getTamanio(self):
        return str(self._tam) + 'Kb'

    def info(self):
        return "Nombre: " + self.getNombre() + " - Cabal: " + self.getCabal() + " - Tamaño: " + self.getTamanio()


class ManejadorProcesos:
    def __init__(self):
        self.lista_procesos = []

    def agregarProceso(self, nom, tam):
        validar = True
        i = 0
        while validar:
            tamC = 2 ** i
            if tamC >= int(tam):
                proceso = Proceso(nom, i)
                proceso._tam = tam
                self.lista_procesos.append(proceso)
                validar = False
            i = i + 1

    def imprimirListaProcesos(self):
        return self.lista_procesos[0].getNombre() + " " + self.lista_procesos[0].getCabal()

    def ultimoProceso(self):
        return self.lista_procesos[-1]

    def buscarRepiteNombre(self, nombre):
        if len(self.lista_procesos) != 0:
            for i in range(len(self.lista_procesos)):
                if self.lista_procesos[i].getNombre() == nombre:
                    return False
            return True
        else:
            return True

    def buscarXindice(self, i):
        if len(self.lista_procesos) != 0:
            return self.lista_procesos[i]


class Dispo:
    def __init__(self, dir, cabal):
        self.dirCom = dir
        self.cabal = cabal
        self.ultimo = None
        self.primero = None

    def agregar_al_final(self, particion):
        nuevo = BloqueLibre(particion, self)
        if self.getVacio():
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            self.ultimo.ps = nuevo
            nuevo.pa = self.ultimo
            self.ultimo = nuevo

    def eliminarPrimero(self):
        if self.getVacio():
            print("Lista Vacia. Imposible eliminar")
        elif self.primero == self.ultimo:
            self.primero = None
            self.ultimo = None
            print("Elemento eliminado. La lista esta vacia")
        else:
            temp = self.primero
            self.primero = self.primero.ps
            self.primero.pa = None
            temp = None
            print("Elemento eliminado")

    def eliminarUltimo(self):
        if self.getVacio():
            print("Lista vacia. Imposible eliminar")
        elif self.primero == self.ultimo:
            self.primero = None
            self.ultimo = None
            print("Elemento eliminado. La lista esta vacia")
        else:
            temp = self.ultimo
            self.ultimo = self.ultimo.pa
            self.ultimo.ps = None
            temp = None
            print("Elemento eliminado")

    def eliminar(self, particion):
        if self.getVacio():
            print("Lista Vacia. Imposible eliminar")
        elif self.primero == self.ultimo and self.primero.particion == particion:
            self.primero = None
            self.ultimo = None
            print("Elemento eliminado. La lista esta vacia")
        else:
            validar = True
            temp = self.primero
            while validar:
                if temp.particion == particion:
                    if self.primero == temp:
                        self.eliminarPrimero()
                    elif self.ultimo == temp:
                        self.eliminarUltimo()
                    else:
                        temp.pa.ps = temp.ps
                        temp.ps.pa = temp.pa
                        temp = None
                    validar = False
                    print("Elemento eliminado")
                else:
                    temp = temp.ps

    def imprimir(self):
        if self.getVacio():
            print("Lista Vacia")
        else:
            print("entra")
            texto = ""
            texto = "DISPO - DIR. COM.: " + str(self.dirCom) + "\n" \
                    "--+----- PA: " + str(self.primero.particion.direccionComienzo) + "\n"\
	                "--+-- KVAL: " + str(self.cabal) + "\n"\
	                "--+----- PS: " + str(self.primero.particion.direccionComienzo) + "\n"
            validar = True
            temp = self.primero
            while validar:
                texto = texto + temp.imprimir()
                if temp == self.ultimo:
                    validar = False
                else:
                    temp = temp.ps
            return texto

    def getVacio(self):
        if self.primero is None:
            return True
        return False


class BloqueLibre:
    def __init__(self, particion, dispo):
        self.particion = particion
        self.dispo = dispo
        self.pa = None
        self.ps = None

    def getParticion(self):
        text = str(self.particion.proceso.info())
        if self.ps is None:
            text = text + " - PS: " + str(self.dispo.dirCom)
        else:
            text = text + " - PS: " + str(self.ps.particion.direccionComienzo)
        if self.pa is None:
            text = text + " - PA: " + str(self.dispo.dirCom)
        else:
            text = text + " - PA: " + str(self.pa.particion.direccionComienzo)
        return text

    def imprimir(self):
        string = "\tBloque Libre - DIR. COM.: " + str(self.particion.direccionComienzo) + "\n"
        if self.pa is None:
            string = string + "\t--+----- PA: " + str(self.dispo.dirCom) + "\n"
        else:
            string = string + "\t--+----- PA: " + str(self.pa.particion.direccionComienzo) + "\n"
        string = string + "\t--+-- MAR: 0\n" \
                          "\t--+-- KVAL: " + str(self.particion.cabal) + "\n"
        if self.ps is None:
            string = string + "\t--+----- PS: " + str(self.dispo.dirCom) + "\n"
        else:
            string = string + "\t--+----- PS: " + str(self.ps.particion.direccionComienzo) + "\n"

        return string


class Particion:
    def __init__(self, cabal, proceso, dirCom, particionPadre):
        self.cabal = cabal
        self.proceso = proceso
        self.direccionComienzo = dirCom
        self.hijoIzquierdo = None
        self.hijoDerecho = None
        self.padre = particionPadre

    def dividirParticion(self):
        nuevoKVAL = int(self.cabal) - 1
        procesoLibre1 = Proceso('Libre', nuevoKVAL)
        procesoLibre2 = Proceso('Libre', nuevoKVAL)
        dirSegundaParticion = self.direccionComienzo + 2**nuevoKVAL
        self.proceso = None
        self.hijoIzquierdo = Particion(nuevoKVAL, procesoLibre1, self.direccionComienzo, self)
        self.hijoDerecho = Particion(nuevoKVAL, procesoLibre2, dirSegundaParticion, self)

    def libre(self):
        if self.proceso is not None:
            if self.proceso.getNombre() == 'Libre':
                return True
        return False

    def matarHijos(self):
        self.hijoDerecho.padre = None
        self.hijoIzquierdo.padre = None
        self.hijoIzquierdo = None
        self.hijoDerecho = None

    def tieneHijoIzquierdo(self):
        return self.hijoIzquierdo

    def tieneHijoDerecho(self):
        return self.hijoDerecho

    def esHijoIzquierdo(self):
        return self.padre and self.padre.hijoIzquierdo == self

    def esHijoDerecho(self):
        return self.padre and self.padre.hijoDerecho == self

    def esRaiz(self):
        return not self.padre

    def esHoja(self):
        return not (self.hijoDerecho or self.hijoIzquierdo)

    def tieneAlgunHijo(self):
        return self.hijoDerecho or self.hijoIzquierdo

    def tieneAmbosHijos(self):
        return self.hijoDerecho and self.hijoIzquierdo


class Memoria:
    def __init__(self, particion):
        self.vectorLibre = []
        self.raiz = particion
        self.crearVL(particion.cabal)
        self.postorden = []

#LISTOOO
    def crearVL(self, cabal):
        kval = int(cabal)
        dircomienzo = 2 ** kval
        i = 0
        while i <= kval:
            dir = dircomienzo+(2*i)
            dispo = Dispo(dir, i)
            if i == kval:
                dispo.agregar_al_final(self.raiz)
            self.vectorLibre.append(dispo)
            dispo.imprimir()
            i = i + 1

        return True

#LISTOOOO
    def imprimirVL(self):
        vl: list = self.vectorLibre
        vectorLibre = "Vector Libre: \n"
        for p in vl:
            if p.cabal < 10:
                if p.ultimo is not None and p.primero is not None:  # TIENE 1 O MAS BLOQUES LIBRES
                    string = "--|------" + str(p.dirCom) + "\n" \
                             "  |---" + str(p.ultimo.particion.direccionComienzo) + "\n" \
                             " " + str(p.cabal) + "|--\n" \
                             "  |---" + str(p.primero.particion.direccionComienzo) + "\n"
                else:
                    string = "--|------" + str(p.dirCom) + "\n" \
                             "  |---" + str(p.dirCom) + "\n" \
                             " " + str(p.cabal) + "|--\n" \
                             "  |---" + str(p.dirCom) + "\n"
            else:
                if p.ultimo is not None and p.primero is not None:  # TIENE 1 O MAS BLOQUES LIBRES
                    string = "--|------" + str(p.dirCom) + "\n" \
                             "  |---" + str(p.ultimo.particion.direccionComienzo) + "\n" \
                             "" + str(p.cabal) + "|--\n" \
                             "  |---" + str(p.primero.particion.direccionComienzo) + "\n"
                else:
                    string = "--|------" + str(p.dirCom) + "\n" \
                             "  |---" + str(p.dirCom) + "\n" \
                             "" + str(p.cabal) + "|--\n" \
                             "  |---" + str(p.dirCom) + "\n"

            vectorLibre = vectorLibre + string

        return vectorLibre

    def recorridoPostorden(self, raiz):
        if raiz is not None:
            self.recorridoPostorden(raiz.hijoIzquierdo)
            self.recorridoPostorden(raiz.hijoDerecho)
            if raiz.proceso is not None:
                self.postorden.append(raiz)

    def imprimirMemoria(self):
        self.postorden = []
        self.recorridoPostorden(self.raiz)
        text = "Memoria:\n"
        tam = len(self.postorden)
        print(tam)
        for p in self.postorden:
            text = text + "--|------ Dir. Com.: " + str(p.direccionComienzo) + "\n" \
                       "  |-- " + p.proceso.info() + "\n"
        text = text + "--|------ Dir. Com.: " + str(2 ** int(self.raiz.cabal)) + "\n"
        return text

    def buscarDispo_kval(self, kval):
        for p in self.vectorLibre:
            if p.cabal == kval:
                return p

    def tieneBloqueLibre(self, kval): #LA IDEA ES QUE DEVUELVA FALSE CUANDO NO TENGA Y TRUE CUANDO TENGA
        vl = self.vectorLibre
        for p in vl:
            if p.cabal >= kval:
                if p.ultimo is not None and p.primero is not None:
                    return True

        return False

    def primerBloqueLibre(self, kval):        #LA IDEA ES QUE DEVUELVA EL PRIMER BLOQUE DISPONIBLE QUE ENCUENTRE
        print("buscando primer BL")
        vl = self.vectorLibre
        for p in vl:
            if p.cabal >= kval:
                if p.ultimo is not None and p.primero is not None:
                    return p.primero

    def agregar(self, proceso):
        kval = int(proceso.getCabal())
        print("agregar: " + str(kval))
        if self.tieneBloqueLibre(kval):
            print("tiene bloque libre")
            bloqueLibre = self.primerBloqueLibre(kval)
            print(bloqueLibre.particion.proceso._nombre)
            if int(bloqueLibre.particion.cabal) == kval:   #JUSTO TENEMOS UN BLOQUE LIBRE DEL MISMO KVAL
                proceso.particion = bloqueLibre.particion
                bloqueLibre.particion.proceso = proceso
                print(bloqueLibre.particion.proceso.info())
                bloqueLibre.dispo.eliminarPrimero()
            else:                                     #TENEMOS BLOQUE LIBRE PERO TENEDREMOS QUE DIVIDIR LAS PARTICIONES :(
                self._agregar(bloqueLibre.dispo, proceso)

            return True
        else:
            return False

    def _agregar(self, dispo, proceso):
        print('DIVISION DE BLOQUE LIBRE')
        dispo.primero.particion.dividirParticion()                  #SE DIVIDE LA PARTICION PORQUE EL CABAL ES MAYOR DEL QUE REQUIERE EL PROCESO
        print(dispo.cabal - 1)
        dispoAnterior = self.buscarDispo_kval(dispo.cabal - 1)              #BUSCA LA DISPO QUE SE LE AGREGARAN BLOQUES LIBRES POR LA DIVICION DE LA PARTICION
        particionLibre1 = dispo.primero.particion.hijoIzquierdo    #ASIGNACION DE LAS PARTICIONES QUE ESTAN LIBRES
        particionLibre2 = dispo.primero.particion.hijoDerecho
        dispoAnterior.agregar_al_final(particionLibre1)
        dispoAnterior.agregar_al_final(particionLibre2)
        dispo.eliminarPrimero()                                   #OCUPA EL BLOQUE LIBRE QUE SE DIVIDIO
        self.agregar(proceso)

    def sacar(self, proceso):
        dispo = self.buscarDispo_kval(int(proceso._cabal))
        particion = proceso.particion
        proceso.particion = None
        procesoLibre = Proceso('Libre', int(proceso._cabal))
        particion.proceso = procesoLibre
        dispo.agregar_al_final(particion)
        padre = particion.padre
        self.compactar(padre)

    def compactar(self, padre):

        if padre is None:                   #ES EL NODO RAIZ
            print('ES EL NODO RAIZ')
        else:                               #NO ES EL NODO RAIZ ENOTONCES SEGUIMOS COMPROBANDO SI ES QUE SE PUEDE COMPACTAR
            dispo = self.buscarDispo_kval(int(padre.cabal) - 1)
            dispoMayor = self.buscarDispo_kval(int(padre.cabal))
            if padre.hijoIzquierdo.libre() and padre.hijoDerecho.libre():
                dispo.eliminar(padre.hijoDerecho)
                padre.hijoDerecho = None
                dispo.eliminar(padre.hijoIzquierdo)
                padre.hijoIzquierdo = None
                padre.proceso = Proceso('Libre', int(padre.cabal))
                dispoMayor.agregar_al_final(padre)
                self.compactar(padre.padre)

    def imprimirBL(self):
        text = "Bloques Libres:\n"
        for p in self.vectorLibre:
            if p.primero is not None:
                text = text + str(p.imprimir())

        return text

import imgagen_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    _listaProcesos = ManejadorProcesos()
    ui = Ui_MainWindow(_listaProcesos)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

