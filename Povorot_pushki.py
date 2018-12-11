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

        oImage = QImage("fon.png")
        sImage = oImage.scaled(QSize(self.width(), self.height()))  # resize Image to widgets size
        palette = QPalette()
        palette.setBrush(10, QBrush(sImage))  # 10 = Windowrole
        self.setPalette(palette)

        self.label = QLabel('название игры', self)  # test, if it's really backgroundimage
        self.label.setGeometry(860, 500, 200, 50)

        self.pushButton = QPushButton('hdsghja', self)
        self.pushButton.setGeometry(860, 540, 100, 80)
        self.pushButton.clicked.connect(self.cleaning_first)
        self.pushButton.clicked.connect(self.hello)

        # Блок настроек
        self.mish_x = 700  # расположение мишени

        self.sdvig_x = 280  # Задаем отступ слева
        self.sdvig_y = 755  # Задаем ширину поля

        self.a = 45  # Изначальный угол броска
        self.v = 113  # Начальная скорость

        self.kol_hp = 3  # Количество жизней
        self.poln_hp = self.kol_hp

        self.label = QLabel(str(self.a), self)
        self.label.setGeometry(860, 500, 200, 50)

        self.hp = QLabel('', self)
        self.hp.setGeometry(880, 200, 200, 50)
        self.run()

    def run(self):
        i, okBtnPressed = QInputDialog.getInt(
            self, "Давайте сыграем", "Сколько вы хотите жизней?", 3, 1, 3, 1
        )
        if okBtnPressed:
            self.kol_hp = int(i)
            self.hp.setText('0' * self.kol_hp)
            self.show()

    def keyPressEvent(self, event):
        if event.key() == 1062:
            if self.a <= 80:
                self.a += 5
                self.label.setText(str(self.a))
                self.flag = False
        if event.key() == 1067:
            if self.a >= 10:
                self.a -= 5
                self.label.setText(str(self.a))
                self.flag = False
        if event.key() == 32:
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

                if k2 == 0:
                    self.vivod(False)
                    break

                if x + self.sdvig_x in range(self.mish_x, self.mish_x + 21) and self.sdvig_y - y in range(
                        self.sdvig_y - 120, self.sdvig_y + 1):
                    self.vivod(True)
                    break
            qp.setPen(Qt.white)
            for i in range(self.sdvig_y + 1, 1081):
                for j in range(0, 1920):
                    qp.drawPoint(j, i)

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

    def cleaning_first(self):
        self.label.setText('')
        self.pushButton.deleteLater()

    def hello(self):
        try:
            self.pic = QLabel(self)
            self.pixmap = QPixmap('pushka3.0.png')
            self.pic.setPixmap(self.pixmap)
            self.pic.move(280, 755)
            self.pic.show()
        except Exception as e:
            print(e)

    def next(self, naklon):
        try:
            t = QTransform().rotate(45 + naklon)
            self.pic.setPixmap(self.pixmap.transformed(t))
            self.hbox.addWidget(self.pic)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
