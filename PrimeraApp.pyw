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
        uic.loadUi("Principal.ui", self)
        self.listaProcesos = _listaProcesos
        self.lineNombreProceso.textChanged.connect(self.validar_nombre_nuevo_proceso)
        self.pushButtonAgregarNuevoProceso.clicked.connect(self.validar_creacion_proceso)
        self.comboBoxProcesos.currentIndexChanged.connect(self.info_proceso_seleccionado)

    def closeEvent(self, event):
        resultado = QMessageBox.question(self, "Salir...", "¿Seguro que quieres salir de la aplicacion",
                                         QMessageBox.Yes | QMessageBox.No)
        if resultado == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

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
            else:
                QMessageBox.warning(self, "Formulario incorrecto", "Nombre Repetido", QMessageBox.Discard)
        else:
            QMessageBox.warning(self, "Formulario incorrecto", "Validación incorrecta", QMessageBox.Discard)

    def info_proceso_seleccionado(self):
        i = self.comboBoxProcesos.currentIndex()
        proceso = self.listaProcesos.buscarXindice(i)
        self.labelInfoCabal.setText(proceso.getCabal())
        self.labelInfoTam.setText(proceso.getTamanio())

class Proceso:
    _tam: int
    _nombre: str
    _cabal: int

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

# Instancia para iniciar la aplicacion
app = QApplication(sys.argv)
# Crear un objeto de la clase
_listaProcesos = ManejadorProcesos()
_ventana = MiVentana(_listaProcesos)
# Mostrar la ventana
_ventana.show()
# Ejecutar la aplicacion
app.exec_()
