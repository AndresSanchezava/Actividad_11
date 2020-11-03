# referencia al path y la clase QMainWindow
# QfileDialog ==> conexion con cuadro de dialogo
# QMessageBox ==> mostrar cuadro de texto informativo
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
# importación de Slot
from PySide2.QtCore import Slot
# archivos con minusculas y clases con mayusculas
from ui_mainwindow import Ui_MainWindow
from administrador import Administrador
from particula import Particula
# union de codigo de archivo a programa con >
# ejemplo: pyside2-uic mainwindow.ui > ui_mainwindow.py

# llamado al constructor desde aquí
class MainWindow(QMainWindow):
    # funcion
    def __init__(self):
        # super ==> metodo
        super(MainWindow, self).__init__()
        # self se usa para que nuestro objeto exista globalmente y no solo en el constructor.
        self.administrador = Administrador()
        # Ui_MainWindow() ==> objeto referenciado
        self.ui = Ui_MainWindow()
        # setupUi ==> metodo para enbeber la instruccion
        self.ui.setupUi(self)
        # conectar las instrucciones de "conectar_final",
        # "conectar_inicio" y "mostrar"
        self.ui.agregar_final_pushButton.clicked.connect(self.click_agregar)
        self.ui.agregar_inicio_pushButton.clicked.connect(self.click_agregar_inicio)
        self.ui.mostrar_pushButton.clicked.connect(self.click_mostrar)

        # conectar las acciones
        self.ui.actionAbrir.triggered.connect(self.action_abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.action_guardar_archivo)

    @Slot()
    def action_abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            'Abrir Archivo',
            '.',
            'JSON (*.json)'
        )[0]
        if self.administrador.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Abrir",
                "Se abrió el archivo " + '\n' '\n' + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Abrir",
                "Error al abrir el archivo " + '\n' '\n' + ubicacion
            )

    @Slot()
    def action_guardar_archivo(self):
        # getSaveFileName ==> metodo para recibir parametros y guardarlos
        # ubicacion: asigna posiciones desde cero
        ubicacion = QFileDialog.getSaveFileName(
            self, # el dialogo se lanza desde aqui
            'Guardar Archivo', # titulo de la ventana de dialogo
            '.', # directorio desde el que se corre el archivo ejecutable, desde la carpeta del proyecto
            'JSON (*.json)' # extencion del archivo a guardar
        )[0]
        print(ubicacion)
        if self.administrador.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Guardar",
                "Archivo guardado en: " + '\n' '\n' + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Guardar",
                "Archivo no guardado: " + '\n' '\n' + ubicacion
            )


    @Slot()
    def click_mostrar(self):
        # limpiar pantalla de PlaintText
        self.ui.salida.clear()
        # salida datos introducidos por pantalla
        self.ui.salida.insertPlainText(str(self.administrador))

    # funcion Slot para recibir eventos
    @Slot()
    def click_agregar(self):
        # funcion de botones
        # obtener infornacion para las variables
        # .tex() ==> estrae el texto ingresado
        # self. ==> esta asociado a las variables globales de el programa
        identificador = self.ui.identificador_lineEdit.text()
        origenx = self.ui.origen_x_spinBox.value()
        origeny = self.ui.origen_y_spinBox.value()
        destinox = self.ui.destino_x_spinBox.value()
        destinoy = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        # .value() regresa un valor entero
        # elementos de la particula
        particula = Particula(identificador, origenx, origeny, destinox, destinoy, velocidad, red, green, blue)
        # asociar el apartado globalmente
        # mostrar los datos en el recuadro PlainText
        self.administrador.agregar_final(particula)
        
    # funcion Slot para recibir eventos    
    @Slot()
    def click_agregar_inicio(self):
        # funcion de botones
        # obtener infornacion para las variables
        # .tex() ==> estrae el texto ingresado
        # self. ==> esta asociado a las variables globales de el programa
        identificador = self.ui.identificador_lineEdit.text()
        origenx = self.ui.origen_x_spinBox.value()
        origeny = self.ui.origen_y_spinBox.value()
        destinox = self.ui.destino_x_spinBox.value()
        destinoy = self.ui.destino_y_spinBox.value()
        velocidad = self.ui.velocidad_lineEdit.text()
        red = self.ui.red_spinBox.value()
        green = self.ui.green_spinBox.value()
        blue = self.ui.blue_spinBox.value()
        #.value() regresa un valor entero
        # elementos de la particula
        particula = Particula(identificador, origenx, origeny, destinox, destinoy, velocidad, red, green, blue)
        # asociar el apartado globalmente
        # mostrar los datos en el recuadro PlainText
        self.administrador.agregar_inicio(particula)
