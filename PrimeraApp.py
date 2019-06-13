import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic
import imgagen_rc


# clase heredada de QMainWindows (Constructor de ventanas)
class MiVentana(QMainWindow):

    # Metodo contructor de la clase
    def __init__(self, _listaProcesos):
        # Inciar el objeto QmainWindow
        QMainWindow.__init__(self)
        # Cargar la configuracion del archivo .ui en el objeto
        uic.loadUi("Principal.ui", self)
        #Lista de procesos en memoria secundaria
        self.listaProcesos = _listaProcesos
        self.memoriaPrincipal = None
        #Eventos
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
            self.plainTextEditAcciones.clear()
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
            print(str(tamC) + " y " + str(i))
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


# Instancia para iniciar la aplicacion
app = QApplication(sys.argv)
# Crear un objeto de la clase
_listaProcesos = ManejadorProcesos()
_ventana = MiVentana(_listaProcesos)
# Mostrar la ventana
_ventana.show()
# Ejecutar la aplicacion
app.exec_()
