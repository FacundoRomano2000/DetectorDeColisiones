import cv2
import numpy as np
import time
import os , sys
from PySide6.QtCore import *
from PySide6.QtWidgets import QWidget, QApplication, QGridLayout
from PySide6.QtUiTools import QUiLoader


# Función para detectar colores en una imagen
def detect_color(image, lower_color, upper_color):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    result = cv2.bitwise_and(image, image, mask=mask)
    return result

def main(source = 0):

        print(source)

        try:
            source = int(source)
            print("Es entero")
        except:
            print("Es string")
        
        # Rango de color rojo en formato HSV
        lower_red = np.array([0, 100, 100])
        upper_red = np.array([10, 255, 255])

        # Rango de color azul en formato HSV (ajustado para una mejor detección)
        lower_green = np.array([40, 40 , 40])
        upper_green = np.array([100, 255, 255])

        # Tamaño mínimo del objeto para considerarlo grande (ajusta según tus necesidades)
        min_object_area = 2000
        print("Inicio")
        # Captura de video desde la cámara (puedes cambiar esto por una imagen o fuente de video)
        # cap = cv2.VideoCapture('rtsp://192.168.50.11:8554/mjpeg/1')
        print(f" Es un numero? -> {isinstance (source,int)}")
        if isinstance (source,int):
            cap = cv2.VideoCapture(source)
        else:
            cap = cv2.VideoCapture(str(source))
        print("Final")

        # Configuración para grabación de video
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
        out = cv2.VideoWriter(os.path.join(desktop_path, 'collision_video.mp4'), fourcc, 20.0, (640, 480))
        recording_start_time = None
        record_duration = 5  # Duración de la grabación en segundos

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            red_detection = detect_color(frame, lower_red, upper_red)
            blue_detection = detect_color(frame, lower_green, upper_green)

            # Aplicar filtrado de ruido (Gaussian Blur) para mejorar la detección
            red_detection = cv2.GaussianBlur(red_detection, (5, 5), 0)
            blue_detection = cv2.GaussianBlur(blue_detection, (5, 5), 0)

            # Encuentra los contornos de los objetos detectados
            red_contours, _ = cv2.findContours(cv2.cvtColor(red_detection, cv2.COLOR_BGR2GRAY), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            blue_contours, _ = cv2.findContours(cv2.cvtColor(blue_detection, cv2.COLOR_BGR2GRAY), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for red_contour in red_contours:
                red_area = cv2.contourArea(red_contour)

                if red_area >= min_object_area:
                    red_x, red_y, red_w, red_h = cv2.boundingRect(red_contour)
                    red_rect = (red_x, red_y, red_x + red_w, red_y + red_h)

                    # Dibuja un cuadrado rojo alrededor del objeto rojo detectado
                    cv2.rectangle(frame, (red_x, red_y), (red_x + red_w, red_y + red_h), (0, 0, 255), 2)

                    for blue_contour in blue_contours:
                        blue_area = cv2.contourArea(blue_contour)

                        if blue_area >= min_object_area:
                            blue_x, blue_y, blue_w, blue_h = cv2.boundingRect(blue_contour)
                            blue_rect = (blue_x, blue_y, blue_x + blue_w, blue_y + blue_h)

                            # Dibuja un cuadrado azul alrededor del objeto azul detectado
                            cv2.rectangle(frame, (blue_x, blue_y), (blue_x + blue_w, blue_y + blue_h), (255, 0, 0), 2)

                            # Verifica si hay colisión entre los rectángulos rojo y azul
                            if (
                                red_x < blue_x + blue_w and red_x + red_w > blue_x and
                                red_y < blue_y + blue_h and red_y + red_h > blue_y
                            ):
                                # Comienza la grabación si no se está grabando actualmente
                                if recording_start_time is None:
                                    recording_start_time = time.time()
                                    out = cv2.VideoWriter(os.path.join(desktop_path, 'collision_video.mp4'), fourcc, 20.0, (640, 480))
                                    print("Inicio de grabación")

                                # Puedes agregar lógica adicional para manejar la colisión aquí
                                # Por ejemplo, mostrar un mensaje o realizar una acción específica
                                cv2.putText(frame, "Colisión detectada", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # Detiene la grabación después de 'record_duration' segundos
            if recording_start_time is not None and time.time() - recording_start_time > record_duration:
                out.release()
                recording_start_time = None
                print("Fin de grabación")

            # # Escribe el frame en el archivo de video si se está grabando
            if recording_start_time is not None:
                out.write(frame)

            cv2.imshow("Object Detection", frame)

            if cv2.waitKey(1) & 0xFF == 27:  # Presiona la tecla 'Esc' para salir
                break

        cap.release()
        cv2.destroyAllWindows()

# main()