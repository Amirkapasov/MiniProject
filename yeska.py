import sys,time
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton, QWidget
from PyQt5.QtGui import QPainter, QPen, QColor, QFont
from PyQt5.QtCore import Qt, QTimer,QUrl
from PyQt5.QtMultimedia import QSound,QMediaPlayer,QMediaContent
START_TIME = int(input("Start time: "))

class CircularTimer(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Timer")
        self.setMinimumSize(400, 400)

        self.total_duration = START_TIME
        self.start_time = time.perf_counter()
        self.running = True

        self.timer = QTimer(self)
        self.timer.setInterval(16)
        self.timer.timeout.connect(self.update)
        self.timer.start()

        self.paused = False
        self.pause_start = 0.0

        self.pause_button = QPushButton("Pause", self)
        self.pause_button.resize(100,40)
        self.pause_button.clicked.connect(self.pause)

        self.reset_button = QPushButton("Reset",self)
        self.reset_button.resize(100,40)
        self.reset_button.clicked.connect(self.reset_timer)

        self.pos_buttons()
    def remaining_time(self):
        elapsed = time.perf_counter() - self.start_time
        remaining = self.total_duration - elapsed
        return max(0.0, remaining)

    def pos_buttons(self):
        width = self.width()
        height = self.height()

        center_x = width // 2
        center_y = height // 2

        buttons_y = center_y + 50

        self.pause_button.move(center_x - 110, buttons_y)
        self.reset_button.move(center_x + 10, buttons_y)



    def pause(self):
        if not self.paused:
            self.paused = True
            self.pause_start = time.perf_counter()
            self.timer.stop()
            self.pause_button.setText("Resume")
        else:
            pause_duration = time.perf_counter() - self.pause_start
            self.start_time += pause_duration
            self.paused = False
            self.timer.start()
            self.pause_button.setText("Pause")


    def reset_timer(self):
        self.start_time = time.perf_counter()
        self.paused = False
        self.pause_button.setText("Pause")
        self.timer.start()
        self.update()

    def resizeEvent(self, event):
        self.pos_buttons()
        super().resizeEvent(event)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 🎨 ФОН ОКНА
        painter.fillRect(self.rect(), QColor("#1e1e1e"))

        # 📐 Размеры и центрирование круга
        width = self.width()
        height = self.height()

        side = min(width, height) - 50
        x = (width - side) // 2
        y = (height - side) // 2

        remaining = self.remaining_time()

        # ⚫ ФОНОВЫЙ КРУГ (прошедшее время)
        background_pen = QPen(QColor("#444444"), 8)
        background_pen.setCapStyle(Qt.RoundCap)
        painter.setPen(background_pen)
        painter.drawEllipse(x, y, side, side)

        # 🔴 АКТИВНАЯ ДУГА (оставшееся время)
        if self.total_duration > 0:
            progress = remaining / self.total_duration

            active_pen = QPen(QColor("#ff5555"), 8)
            active_pen.setCapStyle(Qt.RoundCap)
            painter.setPen(active_pen)

            start_angle = 90 * 16
            span_angle = int(-progress * 360 * 16)  # минус → по часовой стрелке
            painter.drawArc(x, y, side, side, start_angle, span_angle)

        # ⏱ ТЕКСТ ВРЕМЕНИ
        minutes = int(remaining) // 60
        seconds = int(remaining) % 60
        time_text = f"{minutes:02}:{seconds:02}"

        painter.setFont(QFont("Arial", 40, QFont.Bold))
        painter.setPen(QColor("#ffffff"))
        painter.drawText(self.rect(), Qt.AlignCenter, time_text)

        if remaining <= 0:
            self.timer.stop()


app = QApplication(sys.argv)
window = CircularTimer()
window.show()
sys.exit(app.exec_())


# def tooglePause():
#     global paused
#     if not paused:
#         timer.stop()
#         pause_button.setText("Resume")
#         paused = True
#     else:
#         timer.start()
#         pause_button.setText("Pause")
#         paused = False
#
#
# def reset_timer():
#     global time_left, paused
#     timer.stop()
#     paused = False
#     time_left = Start_time
#
#     minutes = time_left // 60
#     sec = time_left % 60
#     label.setText(f"{minutes:02}:{sec:02}")
#
#     pause_button.setText("Pause")
#

