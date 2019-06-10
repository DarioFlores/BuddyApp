import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt5 import uic


# clase heredada de QMainWindows (Constructor de ventanas)
class MiVentana(QMainWindow):

    # Metodo contructor de la clase
    def __init__(self, _listaProcesos):
        # Inciar el objeto QmainWindow
        QMainWindow.__init__(self)
        # Cargar la configuracion del archivo .ui en el objeto
        uic.loadUi("app/Principal.ui", self)
        #Lista de procesos en memoria secundaria
        self.listaProcesos = _listaProcesos
        self.memoriaPrincipal = None
        #Eventos
        self.lineNombreProceso.textChanged.connect(self.validar_nombre_nuevo_proceso)
        self.pushButtonAgregarNuevoProceso.clicked.connect(self.validar_creacion_proceso)
        self.comboBoxProcesos.currentIndexChanged.connect(self.info_proceso_seleccionado)
        self.pushButtonNuevaMemoria.clicked.connect(self.nueva_memoria_principal)
        self.pushButtonAgregarMP.clicked.connect(self.agregar_proceso_memoria_principal)

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

    def validar_cabal_nuevo_proceso(self):
        cabal = self.lineCabalProceso.text()
        validar = cabal.isdigit()
        if cabal == "":
            self.lineCabalProceso.setStyleSheet("border: 1px solid yellow;")
            return False
        elif not validar:
            self.lineCabalProceso.setStyleSheet("border: 1px solid red;")
            return False
        else:
            self.lineCabalProceso.setStyleSheet("border: 1px solid green;")
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
        if self.validar_nombre_nuevo_proceso() and self.validar_cabal_nuevo_proceso():
            nombre = self.lineNombreProceso.text()
            cabal = self.lineCabalProceso.text()
            if self.listaProcesos.buscarRepiteNombre(nombre):
                self.listaProcesos.agregarProceso(nombre, cabal)
                proceso = self.listaProcesos.ultimoProceso()
                self.comboBoxProcesos.addItem(proceso.getNombre())
                text = "Se agrego el proceso:"
                self.plainTextEditAcciones.appendPlainText(text)
                self.plainTextEditAcciones.appendPlainText(proceso.info())
                self.finInstruccion()
            else:
                QMessageBox.warning(self, "Formulario incorrecto", "Nombre Repetido", QMessageBox.Discard)
        else:
            QMessageBox.warning(self, "Formulario incorrecto", "Validación incorrecta", QMessageBox.Discard)

    def info_proceso_seleccionado(self):
        i = self.comboBoxProcesos.currentIndex()
        proceso = self.listaProcesos.buscarXindice(i)
        self.labelInfoCabal.setText(proceso.getCabal())
        self.labelInfoTam.setText(proceso.getTamanio())

    def nueva_memoria_principal(self):
        if self.validar_cabal_nuevo_memoria_principal():
            kval = self.lineEditCabalMemoriaPrincipal.text()
            proceso = Proceso('Libre', kval)
            particion = Particion(kval, proceso, 0, None)
            self.memoriaPrincipal = Memoria(particion)
            text = self.memoriaPrincipal.imprimirVL()
            self.plainTextEditAcciones.appendPlainText(text)
            self.finInstruccion()
        else:
            QMessageBox.warning(self, "Formulario incorrecto", "Cabal tiene que ser Numerico", QMessageBox.Discard)

    def agregar_proceso_memoria_principal(self):
        i = self.comboBoxProcesos.currentIndex()
        proceso = self.listaProcesos.buscarXindice(i)
        print("accion" + proceso._nombre)
        self.memoriaPrincipal.agregar(proceso)
        text = "Se llevo a Memoria Principal el proceso:"
        self.plainTextEditAcciones.appendPlainText(text)
        self.plainTextEditAcciones.appendPlainText(proceso.info())
        self.finInstruccion()


class Proceso:

    def __init__(self, nombre, cabal):
        self._nombre = nombre
        self._cabal = cabal
        self._tam = 2 ** int(cabal)

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

    def agregarProceso(self, nom, ca):
        proceso = Proceso(nom, ca)
        self.lista_procesos.append(proceso)

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
        return self.lista_procesos[i]


class Dispo:
    def __init__(self, dir, cabal):
        self.dirCom = dir
        self.cabal = cabal
        self.punteroAnterior = None
        self.punteroSiguiente = None


class BloqueLibre:
    def __init__(self, particion, dispo):
        self.particion = particion
        self.dispo = dispo
        self.punteroAnterior = None
        self.punteroSiguiente = None

    def ocuparBL(self):
        dispo = self.dispo
        if self.punteroSiguiente is None:
            dispo.punteroSiguiente = None
            dispo.punteroAnterior = None
            self.dispo = None
        else:
            siguiente = self.punteroSiguiente
            dispo.punteroSiguiente = siguiente
            siguiente.punteroAnterir = None
            self.dispo = None
            self.punteroSiguiente = None
            self.punteroAnterior = None

    @property
    def imprimir(self):
        if self.punteroAnterior and self.punteroSiguiente:
            string = "+---------+-------+--------+---------+\n" \
                     "| PunterA |  MAR  |  KVAL  | PunterA |\n" \
                     "|---------+-------+--------+---------+\n" \
                     "|                          +---------+\n" \
                     "|                          | Dir. In |\n" \
                     "+--------------------------+---------+"
            return string
        return False


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

#LISTOOO
    def crearVL(self, cabal):
        kval = int(cabal)
        dircomienzo = 2 ** kval
        i = 0
        while i <= kval:
            dir = dircomienzo+(2*i)
            dispo = Dispo(dir, i)
            if i == kval:
                bloqueLibre = BloqueLibre(self.raiz, dispo)
                dispo.punteroAnterior = bloqueLibre
                dispo.punteroSiguiente = bloqueLibre
            self.vectorLibre.append(dispo)
            i = i + 1

        return True

#LISTOOOO
    def imprimirVL(self):
        vl: list = self.vectorLibre
        vectorLibre = "Vector Libre: \n"
        for p in vl:
            if p.cabal < 10:
                if p.punteroAnterior is not None and p.punteroSiguiente is not None:  # TIENE 1 O MAS BLOQUES LIBRES
                    string = "--|------" + str(p.dirCom) + "\n" \
                             "  |---" + str(p.punteroAnterior.particion.direccionComienzo) + "\n" \
                             " " + str(p.cabal) + "|--\n" \
                             "  |---" + str(p.punteroSiguiente.particion.direccionComienzo) + "\n"
                else:
                    string = "--|------" + str(p.dirCom) + "\n" \
                             "  |---" + str(p.dirCom) + "\n" \
                             " " + str(p.cabal) + "|--\n" \
                             "  |---" + str(p.dirCom) + "\n"
            else:
                if p.punteroAnterior is not None and p.punteroSiguiente is not None:  # TIENE 1 O MAS BLOQUES LIBRES
                    string = "--|------" + str(p.dirCom) + "\n" \
                             "  |---" + str(p.punteroAnterior.particion.direccionComienzo) + "\n" \
                             "" + str(p.cabal) + "|--\n" \
                             "  |---" + str(p.punteroSiguiente.particion.direccionComienzo) + "\n"
                else:
                    string = "--|------" + str(p.dirCom) + "\n" \
                             "  |---" + str(p.dirCom) + "\n" \
                             "" + str(p.cabal) + "|--\n" \
                             "  |---" + str(p.dirCom) + "\n"

            vectorLibre = vectorLibre + string

        return vectorLibre

    def buscarDispo_kval(self, kval):
        for p in self.vectorLibre:
            if p.cabal == kval:
                return p

    def tieneBloqueLibre(self, kval): #LA IDEA ES QUE DEVUELVA FALSE CUANDO NO TENGA Y TRUE CUANDO TENGA
        vl = self.vectorLibre
        for p in vl:
            print(p.punteroSiguiente)
            if p.cabal >= kval:
                if p.punteroAnterior is not None and p.punteroSiguiente is not None:
                    return True

        return False

    def primerBloqueLibre(self, kval):        #LA IDEA ES QUE DEVUELVA EL PRIMER BLOQUE DISPONIBLE QUE ENCUENTRE
        print("buscando primer BL")
        vl = self.vectorLibre
        for p in vl:
            if p.cabal >= kval:
                if p.punteroAnterior is not None and p.punteroSiguiente is not None:
                    return p.punteroSiguiente

    def agregar(self, proceso):
        kval = int(proceso.getCabal())
        print("agregar" + str(kval))
        if self.tieneBloqueLibre(kval):
            print("tiene bloque libre")
            bloqueLibre = self.primerBloqueLibre(kval)
            print(bloqueLibre.particion.proceso.getNombre())
            if int(bloqueLibre.particion.cabal) == kval:   #JUSTO TENEMOS UN BLOQUE LIBRE DEL MISMO KVAL
                bloqueLibre.particion.proceso = proceso
                bloqueLibre.ocuparBL()
            else:                                     #TENEMOS BLOQUE LIBRE PERO TENEDREMOS QUE DIVIDIR LAS PARTICIONES :(
                self._agregar(bloqueLibre.dispo, proceso)
        else:
            print("NO HAY BLOQUES DISPONIBLES")

    def _agregar(self, dispo, proceso):
        dispo.punteroSiguiente.particion.dividirParticion()
        dispoAnterior = self.buscarDispo_kval(dispo.cabal - 1)
        particionLibre1 = dispo.punteroSiguiente.particion.hijoIzquierdo
        particionLibre2 = dispo.punteroSiguiente.particion.hijoDerecho
        bloqueLibre1 = BloqueLibre(particionLibre1, dispoAnterior)
        bloqueLibre2 = BloqueLibre(particionLibre2, dispoAnterior)
        dispoAnterior.punteroSiguiente = bloqueLibre1
        dispoAnterior.punteroAnterior = bloqueLibre2
        bloqueLibre1.punteroSiguiente = bloqueLibre2
        bloqueLibre2.punteroAnterior = bloqueLibre1
        dispo.punteroSiguiente.ocuparBL()
        self.agregar(proceso)



# Instancia para iniciar la aplicacion
app = QApplication(sys.argv)
# Crear un objeto de la clase
_listaProcesos = ManejadorProcesos()
_ventana = MiVentana(_listaProcesos)
# Mostrar la ventana
_ventana.show()
# Ejecutar la aplicacion
app.exec_()
