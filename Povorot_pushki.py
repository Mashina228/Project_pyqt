import sys
from PyQt5.QtWidgets import QApplication, QWidget, \
    QPushButton, QLabel, QLineEdit, QLCDNumber, QHBoxLayout, QInputDialog, QMainWindow
from PyQt5.Qt import QSize
from PyQt5.QtGui import QPixmap, QTransform, QImage, QPalette, QBrush
from PyQt5.QtCore import QRect
from PyQt5 import uic


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1920, 1080)

        oImage = QImage("fon.png")
        sImage = oImage.scaled(QSize(self.width(), self.height()))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.label = QLabel('название игры', self)  # test, if it's really backgroundimage
        self.label.setGeometry(860, 500, 200, 50)


        self.pushButton = QPushButton('hdsghja', self)
        self.pushButton.setGeometry(860, 540, 100, 80)
        self.pushButton.clicked.connect(self.cleaning_first)
        self.pushButton.clicked.connect(self.hello)
        self.show()

    def cleaning_first(self):
        self.label.setText('')
        self.pushButton.deleteLater()

    def hello(self):
        try:
            self.hbox = QHBoxLayout(self)
            self.label_2.move(1000, 540)
            self.pixmap = QPixmap("space.png")
            self.label_2.setPixmap(self.pixmap)
            self.hbox.addWidget(self.label_2)
            self.setLayout(self.hbox)
            self.show()
            self.next(-90)
        except Exception as e:
            print(e)

    def next(self, naklon):
        try:
            t = QTransform().rotate(naklon)
            self.label_2.setPixmap(self.pixmap.transformed(t))
            self.hbox.addWidget(self.label_2)
            self.setLayout(self.hbox)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
