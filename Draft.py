import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt5.QtGui import QPainter, QPen, QColor
from PyQt5.QtCore import Qt, QTimer


class CircularTimer(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(200, 200)
        self.progress = 1.0  # 1.0 = полный круг, 0.0 = пустой

        # Таймер для анимации
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(10)  # Обновление каждые 100 мс для плавности

    def update_progress(self):
        # Уменьшаем прогресс (здесь для примера скорость высокая)
        if self.progress > 0:
            self.progress -= 0.0000641026
            self.update()  # Вызывает paintEvent
        else:
            self.timer.stop()

    def paintEvent(self, event):
        width = self.width()
        height = self.height()
        side = min(width, height) - 50
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Сглаживание

        # Настройки пера (цвета и толщины)
        pen = QPen()
        pen.setWidth(10)
        pen.setCapStyle(Qt.RoundCap)  # Закругленные края линии

        # 1. Рисуем фоновый (серый) круг
        pen.setColor(QColor("#e0e0e0"))
        painter.setPen(pen)
        painter.drawEllipse((width - side) // 2, (height - side) // 2, side, side)

        # 2. Рисуем "истекающий" красный круг
        pen.setColor(QColor("#ff5555"))
        painter.setPen(pen)

        # Угол в PyQt измеряется в 1/16 градуса.
        # 360 градусов = 5760 (16 * 360)
        start_angle = 90 * 16  # Начинаем сверху (12 часов)
        span_angle = int(self.progress * 360 * 16)

        painter.drawArc((width - side) // 2, (height - side) // 2, side, side,
                        start_angle, span_angle)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircularTimer()
    window.show()
    sys.exit(app.exec_())