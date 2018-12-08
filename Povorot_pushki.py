import sys
from PyQt5.QtWidgets import QApplication, QWidget, \
    QPushButton, QLabel, QLineEdit, QLCDNumber, QHBoxLayout
from PyQt5.QtGui import QPixmap, QTransform


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 10000, 960)
        self.setWindowTitle('показ картинки')

        self.btn = QPushButton('показать', self)
        self.btn.resize(100, 50)
        self.btn.move(200, 50)
        self.btn.clicked.connect(self.hello)

        self.url = QLabel(self)
        self.url.setText('Что показать')
        self.url.move(200, 250)

    def hello(self):
        try:
            self.pixmap = QPixmap('1.jpg')
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
            self.label.setPixmap(self.pixmap.pixmap.transformed(t))
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
