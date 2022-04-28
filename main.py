import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
# from PyQt5.QtGui import QPalette, QColor
from PyQt5 import *
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication, QLineEdit, QGridLayout, QHBoxLayout, \
    QLabel, QPushButton


class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("My App")
        self.setGeometry(0,0,1000,500)
        layout = QHBoxLayout()
        grid_layout = QGridLayout()
        vertical_layout = QVBoxLayout()

        param1 = QLabel()
        param1.setText('Parameter1')
        grid_layout.addWidget(param1, 0, 0)

        param2 = QLabel()
        param2.setText('Parameter1')
        grid_layout.addWidget(param2, 1, 0)

        param3 = QLabel()
        param3.setText('Parameter1')
        grid_layout.addWidget(param3, 2, 0)

        grid_layout.addWidget(Text(), 0, 1)
        grid_layout.addWidget(Text(), 1, 1)
        grid_layout.addWidget(Text(), 2, 1)

        layout.addLayout(grid_layout)


        button = QPushButton()
        button.setText('Btn')

        calculate_price = QLabel()
        calculate_price.setText("""
        Material use: 
        Price per 1:
        Overall price:
        """)
        calculate_price.setStyleSheet("background-color: blue;font-size:18px;font-family:Calibri Light;")

        vertical_layout.addWidget(button)
        vertical_layout.addWidget(calculate_price)
        layout.addLayout(vertical_layout)


        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        # self.setWindowTitle("My App")
        #
        # layout1 = QHBoxLayout()
        # layout2 = QVBoxLayout()
        # layout3 = QVBoxLayout()
        #
        # layout2.addWidget(Color('red'))
        # layout2.addWidget(Color('yellow'))
        # layout2.addWidget(Color('purple'))
        #
        # layout1.addLayout(layout2)
        #
        # layout1.addWidget(Color('green'))
        #
        # layout3.addWidget(Color('red'))
        # layout3.addWidget(Color('purple'))
        #
        # layout1.addLayout(layout3)
        #
        # widget = QWidget()
        # widget.setLayout(layout1)
        # self.setCentralWidget(widget)

class Color(QWidget):
    def __init__(self, color):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.Window, QColor(color))
        self.setPalette(palette)

class Text(QWidget):
    def __init__(self):
        super(Text, self).__init__()
        self.title = 'PyQt5 textbox - pythonspot.com'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

# class Button(QWidget):
#     def __init__(self, text):
#         super(Button, self).__init__()
#         self.text = text
#         button = QPushButton()
#         button.setText(text)
#         button.show()



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()