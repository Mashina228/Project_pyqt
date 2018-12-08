def pokaz_pushki(self, nach):
    self.hbox = QHBoxLayout(self)
    self.pixmap = QPixmap('pushka.')

    self.lbl = QLabel(self)
    self.angle = nach  # это на сколько градусов надо поднять пушк чтобы он была горизонтальной
    t = QTransform().rotate(self.angle)
    self.lbl.setPixmap(self.pixmap.transformed(t))

    self.hbox.addWidget(self.lbl)
    self.setLayout(self.hbox)
    self.show()


def naklon_pushki(self, naklon):
    self.lbl.setPixmap(self.pixmap.transformed(self.angle - naklon))

    self.hbox.addWidget(self.lbl)
    self.setLayout(self.hbox)
    self.show()
