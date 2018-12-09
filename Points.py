import sys, random
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt
import math


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
        qp.setPen(Qt.red)
        a = 45
        v = 52

        for i in range(280):
            k = int(i * math.tan(math.radians(a)) - (9.8 * i ** 2) / (2 * v ** 2 * math.cos(math.radians(a)) ** 2))
            x = i
            if k < 0:
                break
            if k < int((i + 1) * math.tan(math.radians(a)) - (9.8 * (i + 1) ** 2) / (
                    2 * v ** 2 * math.cos(math.radians(a)) ** 2)):
                for j in range(k, int((i + 1) * math.tan(math.radians(a)) - (9.8 * (i + 1) ** 2) / (
                        2 * v ** 2 * math.cos(math.radians(a)) ** 2))):
                    qp.drawPoint(x, 170 - j)
            else:
                for j in range(int((i + 1) * math.tan(math.radians(a)) - (9.8 * (i + 1) ** 2) / (
                        2 * v ** 2 * math.cos(math.radians(a)) ** 2)), k):
                    qp.drawPoint(x, 170 - j)
            y = k
            qp.drawPoint(x, 170 - y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
