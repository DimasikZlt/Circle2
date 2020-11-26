from random import randint
import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication

from Circle2.UI import Ui_Form


class YellowCircle(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.create_circle)

    def create_circle(self):
        self.repaint()

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        self.draw_circle(qp)
        # Завершаем рисование
        qp.end()

    def draw_circle(self, qp):
        # Задаем кисть
        color = [randint(0, 255), randint(0, 255), randint(0, 255)]
        qp.setBrush(QColor(*color))
        radius = randint(1, 500)
        qp.drawEllipse(20, 20, radius, radius)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircle()
    ex.show()
    sys.exit(app.exec())
