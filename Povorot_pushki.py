import sys
from PyQt5.QtWidgets import QApplication, QWidget, \
    QPushButton, QLabel, QLineEdit, QLCDNumber, QHBoxLayout, QInputDialog, QMainWindow
from PyQt5.Qt import QSize
from PyQt5.QtGui import QPixmap, QTransform, QImage, QPalette, QBrush, QPainter, QColor
import math
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QRect
from PyQt5 import uic


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle('Traektoria')

        # oImage = QImage("fon.png")
        # sImage = oImage.scaled(QSize(self.width(), self.height()))  # resize Image to widgets size
        # palette = QPalette()
        # palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        # self.setPalette(palette)

        self.pushButton = QPushButton('hdsghja', self)
        self.pushButton.setGeometry(860, 540, 100, 80)
        self.pushButton.clicked.connect(self.cleaning_first)
        self.pushButton.clicked.connect(self.hello)

        # Блок настроек
        self.flag = False
        self.kon = True

        # Блок настроек
        self.mish_x = 700  # расположение мишени

        self.sdvig_x = 80  # Задаем отступ слева
        self.sdvig_y = 725  # Задаем ширину поля

        self.a = 45  # Изначальный угол броска
        self.v = 113  # Начальная скорость

        self.kol_hp = 3  # Количество жизней
        self.poln_hp = self.kol_hp

        self.label = QLabel(str(self.a), self)
        self.label.setGeometry(860, 500, 200, 50)

        self.hp = QLabel('0' * self.kol_hp, self)
        self.hp.setGeometry(880, 500, 200, 50)

        self.show()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W or event.key() == 1062:
            if self.a <= 80:
                self.povorot_pushki(-5)
                self.a += 5
                self.label.setText(str(self.a))
                self.flag = False
        if event.key() == Qt.Key_S or event.key() == 1067:
            if self.a >= 10:
                self.povorot_pushki(5)
                self.a -= 5
                self.label.setText(str(self.a))
                self.flag = False
        if event.key() == Qt.Key_Space or event.key() == 32:
            self.kon = True
            self.flag = True

    def paintEvent(self, e):
        self.qp = QPainter()
        self.qp.begin(self)
        self.drawPoints(self.qp)
        self.drawMishen(self.qp)
        self.qp.end()

    def drawMishen(self, qp):  # Отрисовка мишени
        qp.setPen(Qt.black)
        qp.setBrush(QColor(139, 69, 19))
        qp.drawRect(self.mish_x, self.sdvig_y - 120, 20, 120)

    def drawPoints(self, qp):  # Отрисовка пола и траектории
        qp.setPen(Qt.green)

        for i in range(1920):  # Отрисовка пола
            qp.drawPoint(i, self.sdvig_y)

        qp.setPen(Qt.white)
        for i in range(self.sdvig_y + 1, 1081):
            for j in range(0, 1920):
                qp.drawPoint(j, i)

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

                if x + self.sdvig_x in range(self.mish_x, self.mish_x + 21) and self.sdvig_y - y in range(
                        self.sdvig_y - 120, self.sdvig_y + 1):
                    if self.kon:
                        self.vivod(True)
                    break

                if k2 < 0:
                    if self.kon:
                        self.vivod(False)

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
        self.kon = False

    def cleaning_first(self):
        self.pushButton.deleteLater()

    def hello(self):
        self.angel = -45
        self.pic = QLabel(self)
        self.pixmap = QPixmap('pushka (3).png')
        t = QTransform().rotate(self.angel)
        self.pic.setPixmap(self.pixmap.transformed(t))
        self.pic.move(10, self.sdvig_y - 140)
        self.pic.show()

    def povorot_pushki(self, naklon):
        self.angel += naklon
        t = QTransform().rotate(self.angel)
        self.pic.setPixmap(self.pixmap.transformed(t))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
