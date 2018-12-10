import sys
from PyQt5.QtCore import QSize, QRect
from PyQt5.QtGui import QImage, QPalette, QBrush
from PyQt5.QtWidgets import *



class MainWindow(QWidget):
    def __init__(self):


        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    oMainwindow = MainWindow()
    sys.exit(app.exec_())
