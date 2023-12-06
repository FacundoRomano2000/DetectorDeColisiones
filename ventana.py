from PySide6.QtCore import *
from PySide6.QtWidgets import QWidget, QApplication, QGridLayout
from PySide6.QtUiTools import QUiLoader
import camara
import os
import sys
import sounddevice as sd

class Ventana(QWidget):
    def __init__(self):
        super(Ventana, self).__init__()

        loader = QUiLoader()
        self.ui = loader.load("panel.ui", None)  # panel.ui debe estar en la misma carpeta

        # Define un layout en Ventana y coloca allí la interfaz creada con QtDesigner
        grid = QGridLayout()
        grid.setContentsMargins(0, 0, 0, 0)
        grid.addWidget(self.ui)
        self.setLayout(grid)

        self.setWindowTitle('Panel de configuración')

        self.grabacion = 0

        self.ui.pbReproducir.clicked.connect(self.slot_reproducir)
        self.ui.pbGrabar.clicked.connect(self.slot_grabarAudio)
        #self.ui.pbCargar.clicked.connect(self.obtener_valores)


    def obtener_valores(self):
        seleccionar_camara = self.ui.leDesdeLaMuestra.text()
        margen_ruido_texto = self.ui.leCantMuestrasGraficadas.text()

        print(f"Seleccionar cámara: {seleccionar_camara}")
        return seleccionar_camara
    
    def slot_reproducir(self):
        # frecuencia_muestreo = 44100
        # sd.play( self.grabacion, frecuencia_muestreo )
        camara.main(self.obtener_valores())
        print("Boton funciona")
        # len( self.grabacion ) )

    def slot_grabarAudio(self):
        duracion = 3
        frecuencia_muestreo = 44100

        self.grabacion = sd.rec(
            int(duracion * frecuencia_muestreo),
            samplerate=frecuencia_muestreo,
            channels=1,
            blocking=True
        )

        print(type(self.grabacion))
        print(self.grabacion, self.grabacion.shape)

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()

# Función main que se ejecuta al iniciar la aplicación
if __name__ == '__main__':
    # Este objeto representa a la aplicación
    app = QApplication(sys.argv)

    os.chdir(os.path.dirname(os.path.abspath(__file__)))

    # Creamos y visualizamos el objeto Ventana que contiene la interfaz creada en QtDesigner
    ventana = Ventana()
    ventana.show()

    sys.exit(app.exec_())