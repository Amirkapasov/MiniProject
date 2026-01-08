import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QPen, QColor, QFont
from PyQt5.QtCore import Qt, QTimer


# ⏱ Время таймера (в секундах)
DURATION = 10


class CircularTimer(QWidget):
    def __init__(self):
        super().__init__()

        # Окно
        self.setMinimumSize(500, 500)
        self.setStyleSheet("background-color: #211E1E;")

        # Таймерные данные
        self.duration = DURATION
        self.remaining_time = self.duration
        self.progress = 1.0

        self.interval_ms = 1 * 100  # Интервал обновления (в миллисекундах)
        self.steps = self.duration * 1000 / self.interval_ms

        # QTimer
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_progress)
        self.timer.start(self.interval_ms)

    def update_progress(self):
        if self.progress > 0:
            self.progress -= 1 / self.steps
            self.remaining_time = max(0, int(self.progress * self.duration))
            self.update()
        else:
            self.progress = 0
            self.remaining_time = 0
            self.timer.stop()

    def paintEvent(self, event):
        width = self.width()
        height = self.height()
        side = min(width, height) - 100

        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Перо
        pen = QPen()
        pen.setWidth(6)
        pen.setCapStyle(Qt.RoundCap)

        x = (width - side) // 2
        y = (height - side) // 2

        # Фоновый круг
        pen.setColor(QColor("#3A3A3A"))
        painter.setPen(pen)
        painter.drawEllipse(x, y, side, side)

        # Прогресс
        pen.setColor(QColor("#C40606"))
        painter.setPen(pen)

        start_angle = 90 * 16
        span_angle = int(self.progress * 360 * 16)

        painter.drawArc(x, y, side, side, start_angle, span_angle)

        # ⏱ Текст таймера
        minutes = self.remaining_time // 60
        seconds = self.remaining_time % 60
        msec = seconds//1000
        time_text = f"{minutes:02}:{seconds:02}:{msec:02}"

        font = QFont("Arial", 36, QFont.Bold)
        painter.setFont(font)
        painter.setPen(QColor("#FFFFFF"))

        painter.drawText(self.rect(), Qt.AlignCenter, time_text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CircularTimer()
    window.show()
    sys.exit(app.exec_())