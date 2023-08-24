import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.uic import loadUi

class rotational_linear_converter(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = loadUi("Converter1.ui", self)  
        self.setWindowTitle("Converter")

        self.ui.convert_button.clicked.connect(self.perform_conversion)
        self.ui.rot_input_type.currentIndexChanged.connect(self.update_rotation_input)
        self.ui.lin_input_type.currentIndexChanged.connect(self.update_linear_input)
        self.ui.radius_input_type.currentIndexChanged.connect(self.update_radius_input)

        self.ui.help_button.clicked.connect(self.show_help_window) 

        self.change_convertion_direction_button()
        self.store_default_values() 
        self.store_previous_positions()



    def show_help_window(self):
        self.help_window = loadUi("help.ui")  
        self.help_window.show()  # Yardım penceresini göster

    def change_convertion_direction_button(self):
        self.direction_button.clicked.connect(self.toggle_conversion_direction)

    def store_default_values(self):
        self.rotation_input_unit = "rpm"
        self.linear_input_unit = "km/h"
        self.radius_input_unit = "m"  
        self.rot_to_lin = True

        self.ui.rpm_input.setEnabled(True)
        self.ui.kmh_input.setEnabled(False)  

        self.spacing = 20  

    def store_previous_positions(self):
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
            self.changePosition()
        else:
            self.direction_button.setText("lineer to rotational")
            self.ui.rpm_input.setEnabled(False)
            self.ui.kmh_input.setEnabled(True)
            self.changePosition()

    def update_rotation_input(self, index):
        self.rotation_input_unit = self.ui.rot_input_type.currentText()

    def update_linear_input(self, index):
        self.linear_input_unit = self.ui.lin_input_type.currentText()

    def update_radius_input(self, index):
        self.radius_input_unit = self.ui.radius_input_type.currentText()

    def convert_any_rot_value_type_to_kmh(self, rot_value, radius):            
        if self.rotation_input_unit == "rad/s":
            value = rot_value * 9.549296 # 1 rad/s = 9.5492965855137 rpm
            
        elif self.rotation_input_unit == "rps":
            value = rot_value * 60 # 1 rps = 60 rpm
        else:
            value = rot_value
            
        return value * (60 * 2 * 3.14159 * radius) / 1000

    def convert_to_meters(self, radius):
        if self.radius_input_unit == "cm":
            radius /= 100.0  # Convert cm to m
        elif self.radius_input_unit == "mm":
            radius /= 1000.0  # Convert mm to m
        elif self.radius_input_unit == "inches":
            radius *= 0.0254  # Convert inches to m
        
        return radius

    def convert_any_lin_value_type_to_rpm(self, lin_value, radius):    
        if self.linear_input_unit == "m/s":
            value = lin_value * 3.6 
        elif self.linear_input_unit == "mph":
            value = lin_value * (1/0.621371)
        else:
            value = lin_value    

        return value * 1000 / (60 * 2 * 3.14159 * radius)
    
    def show_requested_lin_output(self,result):
        if self.linear_input_unit == "mph":
            result = result * 0.621371  # km/h to mph
        elif self.linear_input_unit == "m/s":
            result = result * 0.277778  # km/h to m/s
        self.ui.kmh_input.setText("{:.6f}".format(result))
        
    def show_requested_rot_output(self,result):
        if self.rotation_input_unit == "rps":
            result = result * (1/60)
        elif self.rotation_input_unit == "rad/s":
            result = result * (1/9.549296) 
        self.ui.rpm_input.setText("{:.6f}".format(result))

    def perform_conversion(self):
        try:
            value = float(self.ui.rpm_input.text()) if self.rot_to_lin else float(self.ui.kmh_input.text())
            radius = float(self.ui.radius_input.text())
            
            radius = self.convert_to_meters(radius)
            result = 0
            if self.rot_to_lin:
                rot_value = value
                result = self.convert_any_rot_value_type_to_kmh(rot_value, radius)
                self.show_requested_lin_output(result)
            else:
                lin_value = value
                result = self.convert_any_lin_value_type_to_rpm(lin_value, radius)
                self.show_requested_rot_output(result)

        except ValueError:
            pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = rotational_linear_converter()
    window.show()
    sys.exit(app.exec())
