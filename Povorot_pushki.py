import sys
from PyQt5.QtWidgets import QApplication, QWidget, \
    QPushButton, QLabel, QLineEdit, QLCDNumber, QHBoxLayout, QMainWindow
from PyQt5.Qt import QSize
from PyQt5.QtWidgets import QInputDialog
from PyQt5.QtGui import QPixmap, QTransform, QImage, QPalette, QBrush, QPainter, QColor
import math
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QRect
from PyQt5 import uic


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle('The Pushka Game')
        self.flag_pushki = False
        self.flag_pole = False

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

        # переменная для восстановления жизней
        self.poln_hp = self.kol_hp

        self.label_nachal = QLabel('', self)
        self.label_nachal.setGeometry(680, 300, 200, 100)

        self.hp = QLabel('', self)
        self.hp.setGeometry(1205, 0, 200, 200)

        self.start()

        self.show()

    # стартовое окно перед начала игры
    def start(self):
        self.label_nachal.setText('Это игра "пушка"')

        self.pushButton = QPushButton('Играть', self)
        self.pushButton.setGeometry(660, 400, 150, 80)
        self.pushButton.clicked.connect(self.dialog_nachalo)

    # считывание нажаний для подъема и опускания пушки

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_W or event.key() == 1062:  # поднять пушку
            if self.a <= 80:
                self.povorot_pushki(-5)
                self.a += 5
                self.flag = False
        if event.key() == Qt.Key_S or event.key() == 1067:  # опустить пушку
            if self.a >= 10:
                self.povorot_pushki(5)
                self.a -= 5
                self.flag = False
        if event.key() == Qt.Key_Space or event.key() == 32:  # выстрелить
            self.kon = True
            self.flag = True

    # отрисовка полета

    def paintEvent(self, e):
        self.qp = QPainter()
        self.qp.begin(self)
        self.drawPoints(self.qp)
        self.drawMishen(self.qp)
        self.qp.end()

    def drawMishen(self, qp):  # Отрисовка мишени
        if self.flag_pole:
            qp.setPen(Qt.black)
            qp.setBrush(QColor(139, 69, 19))
            qp.drawRect(self.mish_x, self.sdvig_y - 120, 20, 120)

    # Отрисовка траектории и поля

    def drawPoints(self, qp):

        if self.flag:

            qp.setPen(Qt.red)
            for i in range(round(self.v ** 2 * math.sin(
                    math.radians(self.a * 2)) / 9.8) + 1):

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

                if i == round(self.v ** 2 * math.sin(
                        math.radians(self.a * 2)) / 9.8):
                    if self.kon:
                        self.vivod(False)
        if self.flag_pole:

            qp.setPen(Qt.green)

            # Отрисовка пола
            for i in range(1920):
                qp.drawPoint(i, self.sdvig_y)

            qp.setPen(Qt.white)
            for i in range(self.sdvig_y + 1, 1081):
                for j in range(0, 1920):
                    qp.drawPoint(j, i)

    # вывод результата победы или проигрыша

    def vivod(self, ishod):
        if ishod:
            self.kol_hp = self.poln_hp
            self.hp.setText('You win')
            self.wining = QLabel(self)
            pix = QPixmap('youwon1.png')
            self.wining.setPixmap(pix)
            self.wining.move(0, 0)
            self.wining.show()
            #
            self.pushButton2 = QPushButton('Закрыть', self)
            self.pushButton2.setGeometry(960, 200, 100, 100)
            self.pushButton2.clicked.connect(self.run)
            self.pushButton2.show()
        else:
            if self.kol_hp >= 2:
                self.kol_hp -= 1
                self.hp.setText('Жизни: {}'.format('0' * self.kol_hp))
            else:
                self.kol_hp = self.poln_hp
                self.hp.setText('You lose')
                self.wining = QLabel(self)
                pix = QPixmap('game.png')
                self.wining.setPixmap(pix)
                self.wining.move(0, 0)
                self.wining.show()
                #
                self.pushButton2 = QPushButton('Закрыть', self)
                self.pushButton2.setGeometry(960, 200, 100, 100)
                self.pushButton2.clicked.connect(self.run)
                self.pushButton2.show()
        self.kon = False

    # закрытие окна конец программы

    def run(self):
        QMainWindow.close(self)

    # очистка первого окна для стрельбы

    def cleaning_first(self):
        self.label_nachal.setText('')
        self.label_nachal.resize(1, 1)
        self.pushButton.deleteLater()

    def cleaning_second(self):  # Фунция для будущего продолжения проекта
        self.pushButton2.deleteLater()
        self.hp.setText('')
        t = QTransform().rotate(-45)
        self.pic.setPixmap(self.pixmap.transformed(t))
        self.pic.move()

    def dialog_nachalo(self):
        i, okBtn = QInputDialog.getInt(self,
                                       'Количество жизней', 'Сколыько жизней?', 3, 1, 5, 1)
        if okBtn:
            self.kol_hp = int(i)
            self.flag_pole = True
            self.cleaning_first()
            self.hp.setText('Жизни: {}'.format('0' * self.kol_hp))
            self.hello()
            self.hp.show()

    def hello(self):

        self.podskaz = QLabel('', self)
        self.podskaz.setGeometry(1200, 200, 200, 100)
        self.podskaz.setText('W - Поднять пушку,\nS - Опустить пушку,\nSpace - Выстрел ')
        self.podskaz.show()

        self.angel = -45
        self.pic = QLabel(self)
        self.pixmap = QPixmap('pushka (4).png')
        t = QTransform().rotate(self.angel)
        self.pic.setPixmap(self.pixmap.transformed(t))
        self.vse = {-45: (5, self.sdvig_y - 187), -5: (5, self.sdvig_y - 133), -10: (6, self.sdvig_y - 139),
                    -15: (6, self.sdvig_y - 148), -30: (4, self.sdvig_y - 167), -35: (5, self.sdvig_y - 173),
                    -20: (5, self.sdvig_y - 155), -25: (5, self.sdvig_y - 160), -40: (5, self.sdvig_y - 182),
                    -50: (6, self.sdvig_y - 191), -55: (7, self.sdvig_y - 200), -60: (8, self.sdvig_y - 205),
                    -65: (11, self.sdvig_y - 210), -70: (14, self.sdvig_y - 214), -75: (18, self.sdvig_y - 217),
                    -80: (20, self.sdvig_y - 220), -85: (24, self.sdvig_y - 223)}
        self.pic.move(5, self.sdvig_y - 186)
        self.pic.show()

    def povorot_pushki(self, naklon):
        try:
            self.angel += naklon
            t = QTransform().rotate(self.angel)
            self.pic.setPixmap(self.pixmap.transformed(t))
            self.pic.move(self.vse[self.angel][0], self.vse[self.angel][1])
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
