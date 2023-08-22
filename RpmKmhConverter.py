import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.uic import loadUi

class RPMtoKmHConverterApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = loadUi("Converter.ui", self)  
        self.setWindowTitle("RPM to km/h Converter")

        self.ui.convert_button.clicked.connect(self.perform_conversion)
        self.ui.rot_input_type.currentIndexChanged.connect(self.update_rotation_input)
        self.ui.lin_input_type.currentIndexChanged.connect(self.update_linear_input)
        self.ui.radius_input_type.currentIndexChanged.connect(self.update_radius_input)

        self.direction_button = QPushButton("Rotational to lineer", self)
        self.direction_button.setGeometry(10, 10, 180, 30)
        self.direction_button.clicked.connect(self.toggle_conversion_direction)

        self.rotation_input_unit = "rpm"
        self.linear_input_unit = "kmh"
        self.radius_input_unit = "m"  # Default radius unit
        self.rot_to_lin = True
        self.lin_to_rot_toggle = False  # Toggle for linear to rotational conversion

        self.ui.rpm_input.setEnabled(True)
        self.ui.kmh_input.setEnabled(False)  
        self.ui.lin_input_type.setCurrentIndex(0)  # Set the default index for linear input type

        self.spacing = 20  # Bileşenler arasına ekleyeceğimiz boşluk miktarı

        # Bileşenlerin önceki konumlarını saklamak için değişkenler
        self.prev_rpm_input_y = self.ui.rpm_input.y()
        self.prev_kmh_input_y = self.ui.kmh_input.y()

        self.prev_rotvel_text_y = self.ui.rotvel_text.y()
        self.prev_linvel_text_y = self.ui.linvel_text.y()

        self.prev_rot_input_type_y = self.ui.rot_input_type.y()
        self.prev_lin_input_type_y = self.ui.lin_input_type.y()

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
            self.ui.lin_input_type.setEnabled(True)  # Enable linear input type selection
            self.changePosition()
        else:
            self.direction_button.setText("lineer to rotational")
            self.ui.rpm_input.setEnabled(False)
            self.ui.kmh_input.setEnabled(True)
            self.ui.lin_input_type.setEnabled(False)  # Disable linear input type selection
            self.lin_to_rot_toggle = True  # Set the toggle to handle linear to rotational conversion
            self.changePosition()

    def update_rotation_input(self, index):
        self.rotation_input_unit = self.ui.rot_input_type.currentText()

    def update_linear_input(self, index):
        self.linear_input_unit = self.ui.lin_input_type.currentText()

    def update_radius_input(self, index):
        self.radius_input_unit = self.ui.radius_input_type.currentText()

    def perform_conversion(self):
        try:
            value = float(self.ui.rpm_input.text()) if self.rot_to_lin else float(self.ui.kmh_input.text())
            radius = float(self.ui.radius_input.text())
            
            if self.radius_input_unit == "cm":
                radius /= 100.0  # Convert cm to m
            elif self.radius_input_unit == "mm":
                radius /= 1000.0  # Convert mm to m
            elif self.radius_input_unit == "inches":
                radius *= 0.0254  # Convert inches to m

            result = 0
            if self.rot_to_lin:
                if self.rotation_input_unit == "rpm":
                    result = value * (60 * 2 * 3.14159 * radius) / 1000
                elif self.rotation_input_unit == "rad/s":
                    value = value * 9.549296 # 1 rad/s = 9.5492965855137 rpm
                    result = value * (60 * 2 * 3.14159 * radius) / 1000
                elif self.rotation_input_unit == "rps":
                    value = value * 60
                    result = value * (60 * 2 * 3.14159 * radius) / 1000

                if self.linear_input_unit == "mph":
                    result = result * 0.621371  # km/h to mph
                elif self.linear_input_unit == "m/s":
                    result = result * 0.277778  # km/h to m/s

                self.ui.kmh_input.setText("{:.6f}".format(result))
                
            # ... Diğer dönüşümler aynı kalsın ...

            if self.lin_to_rot_toggle:  # Handle linear to rotational conversion
                self.lin_to_rot_toggle = False
                self.ui.kmh_input.setEnabled(False)
                self.ui.rpm_input.setEnabled(True)
                self.changePosition()

        except ValueError:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RPMtoKmHConverterApp()
    window.show()
    sys.exit(app.exec())
