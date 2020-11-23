import sys

from PyQt5 import uic

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randrange


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.btn.clicked.connect(self.start)
        self.draw_flag = False

    def start(self):
        self.draw_flag = True
        self.repaint()
        self.draw_flag = False

    def paintEvent(self, event):
        if self.draw_flag:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()

    def draw(self, qp):
        circles = []
        qp.setBrush(QColor(255, 255, 0))
        for i in range(5):
            d = randrange(100)
            circles.append((randrange(self.frameGeometry().width()), randrange(self.frameGeometry().height()), d, d))
        for i in circles:
            qp.drawEllipse(*i)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
