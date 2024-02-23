from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QPainter, QColor, QPolygon
import sys
from random import randint

h = 1200
w = 720


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('ui.ui', self)
        self.setGeometry(0, 0, h, w)
        self.pushButton.clicked.connect(self.draw)
        self.f = 0

    def draw(self):
        self.r = randint(5, 50)
        self.f = 1
        self.update()

    def paintEvent(self, event):
        if self.f:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(255, 255, 0))
            qp.setBrush(QColor(255, 255, 0))
            self.x = randint(self.r + 1, h - (self.r + 1))
            self.y = randint(self.r + 1, w - (self.r + 1))
            qp.drawEllipse(self.x, self.y, self.r, self.r)
            qp.end()
            self.f = 0


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec_())
