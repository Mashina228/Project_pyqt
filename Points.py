import sys
from PyQt5.QtWidgets import QWidget, QApplication, QInputDialog, QLabel
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt
import math
import time


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle('Traektoria')

        self.flag = False

        # Блок настроек
        self.mish_x = 700  # расположение мишени

        self.sdvig_x = 50  # Задаем отступ слева
        self.sdvig_y = 725  # Задаем ширину поля

        self.a = 45  # Изначальный угол броска
        self.v = 113  # Начальная скорость

        self.kol_hp = 3  # Количество жизней
        self.poln_hp = self.kol_hp

        self.label = QLabel(str(self.a), self)
        self.label.setGeometry(860, 500, 200, 50)

        self.hp = QLabel('', self)
        self.hp.setGeometry(880, 500, 200, 50)

        self.run()

        self.show()

    def run(self):
        i, okBtnPressed = QInputDialog.getInt(
            self, "Давайте сыграем", "Сколько вы хотите жизней?", 3, 1, 3, 1
        )
        if okBtnPressed:
            self.kol_hp = int(i)
        self.hp.setText('0' * self.kol_hp)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W:
            if self.a <= 80:
                self.a += 5
                self.label.setText(str(self.a))
        if event.key() == Qt.Key_S:
            if self.a >= 10:
                self.a -= 5
                self.label.setText(str(self.a))
        if event.key() == Qt.Key_Space:
            self.flag = True

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

        if self.flag:
            qp.setPen(Qt.red)
            for i in range(round(self.v ** 2 * math.sin(
                    math.radians(self.a * 2)) / 9.8) + 1):  # Отрисовка траектории, тут сложно, если что я объясню
                k1 = int(i * math.tan(math.radians(self.a)) - (9.8 * i ** 2) / (
                        2 * self.v ** 2 * math.cos(math.radians(self.a)) ** 2))
                k2 = int((i + 1) * math.tan(math.radians(self.a)) - (9.8 * (i + 1) ** 2) / (
                        2 * self.v ** 2 * math.cos(math.radians(self.a)) ** 2))
                x = i

                if k1 < k2:
                    for j in range(k1, k2):
                        qp.drawPoint(x + self.sdvig_x, self.sdvig_y - j)
                else:
                    for j in range(k2, k1):
                        qp.drawPoint(x + self.sdvig_x, self.sdvig_y - j)
                y = k1
                qp.drawPoint(x + self.sdvig_x, self.sdvig_y - y)

                print(k1, k2)

                if k2 == 0:
                    self.vivod(False)
                    break

                if x + self.sdvig_x in range(self.mish_x, self.mish_x + 21) and self.sdvig_y - y in range(
                        self.sdvig_y - 120, self.sdvig_y + 1):
                    break
                    self.vivod(True)
            qp.setPen(Qt.white)
            for i in range(self.sdvig_y + 1, 1081):
                for j in range(0, 1920):
                    qp.drawPoint(j, i)
            self.show()

    def vivod(self, ishod):
        if ishod:
            self.kol_hp = self.poln_hp
            self.hp.setText('You win')
        else:
            if self.kol_hp >= 2:
                self.kol_hp -= 1
                self.hp.setText('0' * self.kol_hp)
            else:
                self.kol_hp = self.poln_hp
                self.hp.setText('You lose')
        current_sec = time.localtime(time.time())[5]
        next_current_sec = current_sec
        while next_current_sec - current_sec != 5:
            next_current_sec = time.localtime(time.time())[5]
            print(current_sec, next_current_sec)
            self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
