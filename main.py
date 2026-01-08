import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt, QTimer

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # заголовок окна
        self.setWindowTitle("Pomadaro")
        self.setMinimumSize(400, 400)

        self.progress = 1.0

        # Анимация Таймера
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateTimer)
        self.timer.start(10)

    def updateTimer(self):
        if self.progress > 0:
            self.progress -= 0.000006666
            self.update()
        else:
            self.timer.stop()

    def paintEvent(self, event):
        width = self.width()
        height = self.height()
        side = min(width, height) - 50
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        pen = QPen()
        pen.setWidth(5)
        pen.setCapStyle(Qt.RoundCap)

        pen.setColor(QColor("#e0e0e0"))
        painter.setPen(pen)
        painter.drawEllipse((width - side) // 2, (height - side) // 2, side, side)

        pen.setColor(QColor("#ff5555"))
        painter.setPen(pen)

        start_angle = 90*16
        span_angle = int(self.progress * 360 * 16)

        painter.drawArc((width - side) // 2, (height - side) // 2, side, side,
                        start_angle, span_angle)

if __name__ == "__main__":
    # объект приложения
    app = QApplication(sys.argv)

    # экземпляр нашего класса
    window = MyWindow()

    # Показываем окно
    window.show()

    # Запускаем цикл обработки событий
    sys.exit(app.exec_())