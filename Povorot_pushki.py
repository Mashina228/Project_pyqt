import sys
from PyQt5.QtWidgets import QApplication, QWidget, \
    QPushButton, QLabel, QLineEdit, QLCDNumber, QHBoxLayout, QInputDialog, QMainWindow
from PyQt5.QtGui import QPixmap, QTransform
from PyQt5 import uic


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.flag = True
        uic.loadUi('project.ui', self)
        self.nach_okno()

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

    def nach_okno(self):
        try:
            pixmap = QPixmap('w.png')
            self.label_1 = QLabel(self)
            self.label_1.resize(pixmap.width(), pixmap.height())
            self.label_1.setPixmap(pixmap)
            self.label_1.move(190, 170)

            pixmap_2 = QPixmap('s.png')
            self.label_2 = QLabel(self)
            self.label_2.resize(pixmap_2.width(), pixmap_2.height())
            self.label_2.setPixmap(pixmap_2)
            self.label_2.move(370, 170)

            pixmap_3 = QPixmap('space.png')
            self.label_3 = QLabel(self)
            self.label_3.resize(pixmap_3.width(), pixmap_3.height())
            self.label_3.setPixmap(pixmap_3)
            self.label_3.move(500, 170)

            self.show()
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
