import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.uic import loadUi

class RPMtoKmHConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = loadUi("Converter.ui", self)  
        self.setWindowTitle("RPM to km/h Converter")

        self.ui.convert_button.clicked.connect(self.perform_conversion)
        
        self.direction_button = QPushButton("Rotational to lineer", self)
        self.direction_button.setGeometry(10, 10, 180, 30)
        self.direction_button.clicked.connect(self.toggle_conversion_direction)

        self.rot_to_lin = True  

        self.ui.rpm_input.setEnabled(True)
        self.ui.kmh_input.setEnabled(False)  

        self.spacing = 20  # Bileşenler arasına ekleyeceğimiz boşluk miktarı

        # Bileşenlerin önceki konumlarını saklamak için değişkenler
        self.prev_rpm_input_y = self.ui.rpm_input.y()
        self.prev_kmh_input_y = self.ui.kmh_input.y()

        self.prev_rotvel_text_y = self.ui.rotvel_text.y()
        self.prev_linvel_text_y = self.ui.linvel_text.y()

        self.prev_rot_input_type_y = self.ui.rot_input_type.y()
        self.prev_lin_input_type_y = self.ui.lin_input_type.y()


        #yer değiştirme fonksiyonu
    def changePosition(self):
        #changes input text components position
        self.ui.rpm_input.move(self.ui.rpm_input.x(), self.prev_kmh_input_y)
        self.ui.kmh_input.move(self.ui.kmh_input.x(), self.prev_rpm_input_y)
        self.prev_rpm_input_y, self.prev_kmh_input_y = self.prev_kmh_input_y, self.prev_rpm_input_y
        #changes type text position
        self.ui.rotvel_text.move(self.ui.rotvel_text.x(), self.prev_linvel_text_y)
        self.ui.linvel_text.move(self.ui.linvel_text.x(), self.prev_rotvel_text_y)
        self.prev_rotvel_text_y, self.prev_linvel_text_y = self.prev_linvel_text_y, self.prev_rotvel_text_y
        #changes input type changers position
        self.ui.rot_input_type.move(self.ui.rot_input_type.x(), self.prev_lin_input_type_y)
        self.ui.lin_input_type.move(self.ui.lin_input_type.x(), self.prev_rot_input_type_y)
        self.prev_rot_input_type_y, self.prev_lin_input_type_y = self.prev_lin_input_type_y, self.prev_rot_input_type_y


    def toggle_conversion_direction(self):
        self.rot_to_lin = not self.rot_to_lin
        if self.rot_to_lin:
            self.direction_button.setText("rotational to lineer")
            self.ui.rpm_input.setEnabled(True)
            self.ui.kmh_input.setEnabled(False)
            self.changePosition()
    
        else:
            self.direction_button.setText("lineer to rotational")
            self.ui.rpm_input.setEnabled(False)
            self.ui.kmh_input.setEnabled(True)
            self.changePosition()

            
    def perform_conversion(self):
        try:
            value = float(self.ui.rpm_input.text()) if self.rot_to_lin else float(self.ui.kmh_input.text())
            radius = float(self.ui.radius_input.text())
            if self.ui.rot_to_lin:
                result = value * (60 * 2 * 3.14159 * radius) / 1000
                self.ui.kmh_input.setText("{:.6f}".format(result))
            else:
                result = value * 1000 / (60 * 2 * 3.14159 * radius)
                self.ui.rpm_input.setText("{:.6f}".format(result))
        except ValueError:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RPMtoKmHConverterApp()
    window.show()
    sys.exit(app.exec())
