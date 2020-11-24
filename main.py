import sys

from PyQt5 import uic

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randrange
from UI import Ui_MainWindow

class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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

        for i in range(5):
            d = randrange(100)
            circles.append((randrange(self.frameGeometry().width()), randrange(self.frameGeometry().height()), d, d))
        for i in circles:
            qp.setBrush(QColor(randrange(255), randrange(255), randrange(255)))
            qp.drawEllipse(*i)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
