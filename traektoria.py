import math
import sys, random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 280, 170)
        self.setWindowTitle('Points')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self, qp):
        a = 45
        v = 10

        qp.setPen(Qt.black)
        size = self.size()

        for i in range(20):
            x = i
            y = i * math.tan(math.radians(a)) - (9.8 * i ** 2) / (2 * v ** 2 * math.cos(math.radians(a)) ** 2)
            qp.drawPoint(280 - x * 10, 170 - y * 10)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
