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
        self.show()

    def cleaning_first(self):
        self.label.setText('')
        self.pushButton.deleteLater()

    def hello(self):
        try:
            self.pixmap = QPixmap('fon.jpg')
            self.angle = -45
            self.label = QLabel(self)
            t = QTransform().rotate(self.angle)
            self.label.setPixmap(self.pixmap.pixmap.transformed(t))
            self.label.move(0, self.height())
            self.show()
        except Exception as e:
            print(e)


def next(self, naklon):
    try:
        t = QTransform().rotate(self.angle - naklon)
        self.label.setPixmap(self.pixmap.transformed(t))
    except Exception as e:
        print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
