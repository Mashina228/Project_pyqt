from PyQt5 import Qt
import pyqtgraph as pg
import math


class Window(Qt.QWidget):

    def __init__(self):
        super().__init__()

        layout = Qt.QVBoxLayout(self)

        self.view = view = pg.PlotWidget()
        self.curve = view.plot(name="Line")

        self.btn = Qt.QPushButton("Random plot")
        self.btn.clicked.connect(self.random_plot)

        layout.addWidget(Qt.QLabel("Some text"))
        layout.addWidget(self.view)
        layout.addWidget(self.btn)

    def random_plot(self):
        a = 45
        v = 10
        random_array = []
        for i in range(20):
            if i * math.tan(math.radians(a)) - (9.8 * i ** 2) / (2 * v ** 2 * math.cos(math.radians(a)) ** 2) < 0:
                break
            random_array.append(
                i * math.tan(math.radians(a)) - (9.8 * i ** 2) / (2 * v ** 2 * math.cos(math.radians(a)) ** 2))
        self.curve.setData(random_array)


if __name__ == "__main__":
    app = Qt.QApplication([])
    w = Window()
    w.show()
    app.exec()
