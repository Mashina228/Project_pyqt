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
        qp.setBrush(QColor(139, 69, 19))
        qp.drawRect(self.mish_x, self.sdvig_y - 120, 20, 120)

    def drawPoints(self, qp):  # Отрисовка пола и траектории
        qp.setPen(Qt.green)

        for i in range(1920):  # Отрисовка пола
            qp.drawPoint(i, self.sdvig_y)

        qp.setPen(Qt.red)
        for i in range(round(self.v ** 2 * math.sin(
                math.radians(self.a * 2)) / 9.8) + 1):  # Отрисовка траектории, тут сложно, если что я объясню
            k1 = int(i * math.tan(math.radians(self.a)) - (9.8 * i ** 2) / (
                    2 * self.v ** 2 * math.cos(math.radians(self.a)) ** 2))
            k2 = int((i + 1) * math.tan(math.radians(self.a)) - (9.8 * (i + 1) ** 2) / (
                    2 * self.v ** 2 * math.cos(math.radians(self.a)) ** 2))
            x = i
            if k2 < 0:
                self.vivod('gamer over')

            if k1 < 0:
                break

            if k1 < k2:
                for j in range(k1, k2):
                    qp.drawPoint(x + self.sdvig_x, self.sdvig_y - j)
            else:
                for j in range(k2, k1):
                    qp.drawPoint(x + self.sdvig_x, self.sdvig_y - j)
            y = k1
            qp.drawPoint(x + self.sdvig_x, self.sdvig_y - y)
            if x + self.sdvig_x in range(self.mish_x, self.mish_x + 21) and self.sdvig_y - y in range(
                    self.sdvig_y - 120, self.sdvig_y + 1):
                self.vivod('win')
                break
        qp.setPen(Qt.white)
        for i in range(self.sdvig_y + 1, 1081):
            for j in range(0, 1920):
                qp.drawPoint(j, i)

    def vivod(self, ishod):
        print(ishod)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
