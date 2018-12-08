import sys
from PyQt5.QtWidgets import QApplication, QWidget, \
    QPushButton, QLabel, QLineEdit, QLCDNumber, QHBoxLayout
from PyQt5.QtGui import QPixmap, QTransform


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 10000, 10000)
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
            self.hbox = QHBoxLayout(self)
            self.pixmap = QPixmap('1.jpg')

            self.lbl = QLabel(self)
            self.angle = -90  # это на сколько градусов надо поднять пушк чтобы он была горизонтальной
            t = QTransform().rotate(self.angle)
            self.lbl.setPixmap(self.pixmap.transformed(t))
            self.lbl.move(200, 10)
            self.hbox.addWidget(self.lbl)
            self.setLayout(self.hbox)
            self.show()
        except Exception as e:
            print(e)

    def next(self):
        t = QTransform().rotate(self.angle - 45)
        self.lbl.setPixmap(self.pixmap.transformed(t))

        self.hbox.addWidget(self.lbl)
        self.setLayout(self.hbox)
        self.pixmap.move(10000, 10)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
