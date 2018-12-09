import sys
from PyQt5.QtWidgets import QApplication, QWidget, \
    QPushButton, QLabel, QLineEdit, QLCDNumber, QHBoxLayout, QInputDialog, QMainWindow
from PyQt5.Qt import QSize
from PyQt5.QtGui import QPixmap, QTransform, QImage, QPalette, QBrush
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.flag = True
        uic.loadUi('project.ui', self)

        oImage = QImage("pushka.jpg")
        sImage = oImage.scaled(QSize(self.width(), self.height()))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(sImage))
        self.setPalette(palette)
        self.pushButton.clicked.connect(self.cleaning_first)

    def cleaning_first(self):
        self.label.setText('')
        self.pushButton.deleteLater()

    def hello(self):
        try:
            self.pixmap = QPixmap('pushka.jpg')
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