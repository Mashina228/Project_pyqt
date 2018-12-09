import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import math


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle('Traektoria')

        # Блок настроек
        self.mish_x = 700

        self.sdvig_x = 50
        self.sdvig_y = 725

        self.a = 45
        self.v = 113

        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawPoints(qp)
        self.drawMishen(qp)
        qp.end()

    def drawMishen(self, qp):  # Отрисовка мишени
        qp.setPen(Qt.black)
        qp.setBrush(QColor(66, 47, 43))
        qp.drawRect(self.mish_x, self.sdvig_y - 120, 20, 120)

    def drawPoints(self, qp):  # Отрисовка пола и траектории
        qp.setPen(Qt.green)

        for i in range(1920):  # Отрисовка пола
            qp.drawPoint(i, self.sdvig_y)

        qp.setPen(Qt.red)
        for i in range(1920):  # Отрисовка траектории, тут сложно, если что я объясню
            k = int(i * math.tan(math.radians(self.a)) - (9.8 * i ** 2) / (
                    2 * self.v ** 2 * math.cos(math.radians(self.a)) ** 2))
            x = i
            if k < 0:
                break
            if k < int((i + 1) * math.tan(math.radians(self.a)) - (9.8 * (i + 1) ** 2) / (
                    2 * self.v ** 2 * math.cos(math.radians(self.a)) ** 2)):
                for j in range(k, int((i + 1) * math.tan(math.radians(self.a)) - (9.8 * (i + 1) ** 2) / (
                        2 * self.v ** 2 * math.cos(math.radians(self.a)) ** 2))):
                    qp.drawPoint(x + self.sdvig_x, self.sdvig_y - j)
            else:
                for j in range(int((i + 1) * math.tan(math.radians(self.a)) - (9.8 * (i + 1) ** 2) / (
                        2 * self.v ** 2 * math.cos(math.radians(self.a)) ** 2)), k):
                    qp.drawPoint(x + self.sdvig_x, self.sdvig_y - j)
            y = k
            qp.drawPoint(x + self.sdvig_x, self.sdvig_y - y)

            print(x + self.sdvig_x, self.sdvig_y - y)

            if x + self.sdvig_x in range(self.mish_x, self.mish_x + 21) and self.sdvig_y - y in range(
                    self.sdvig_y - 120, self.sdvig_y):
                print('Win')
                break


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
