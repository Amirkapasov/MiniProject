import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton
from PyQt5.QtGui import QPainter, QPen, QColor, QFont
from PyQt5.QtCore import Qt, QTimer,QUrl
from PyQt5.QtMultimedia import QSound,QMediaPlayer,QMediaContent

time_m = int(input("Enter the time in m: "))

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pomodoro")
        self.setMinimumSize(400, 400)
        # Темный фон
        self.setStyleSheet("background-color: #2b2b2b;")

        # Аудио плеер настройка
        self.player = QMediaPlayer()
        # Расположение звука
        sound_path = "/Users/kapasovamir/PycharmProjects/MiniProject/sound/02599.mp3"
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(sound_path)))

        # Настройки времени
        self.total_seconds = time_m * 60
        self.remaining_seconds = self.total_seconds

        # Таймер срабатывает раз (1000 мс)
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_timer)
        self.timer.start(1000)

        self.StartButton = QPushButton(self)
        self.StartButton.setText("Start")
        self.StartButton.move(75, 250)
        self.StartButton.clicked.connect(self.timer.start)

        self.StopButton = QPushButton(self)
        self.StopButton.setText("Stop")
        self.StopButton.move(220, 250)
        self.StopButton.clicked.connect(self.timer.stop)


    # Функция для анимация таймера
    def update_timer(self):
        if self.remaining_seconds > 0:
            self.remaining_seconds -= 1
            self.update() # Перерисовать окно
        if self.remaining_seconds == 0:
            self.timer.stop()
            self.player.play() # Вывод звука
            self.total_seconds = time_m * 60
            self.remaining_seconds = self.total_seconds

    def paintEvent(self, event):

        # Значение окна берет
        width = self.width()
        height = self.height()

        # Отступ от краев
        side = min(width, height) - 50
        x = (width - side) // 2
        y = (height - side) // 2

        painter = QPainter(self) # Холст
        painter.setRenderHint(QPainter.Antialiasing) # Сглаживание холста

        # Серый фоновый круг
        pen = QPen(QColor("#444444"), 8)
        painter.setPen(pen)
        painter.drawEllipse(x, y, side, side)

        # Красную круг над фоновым кругом
        if self.total_seconds > 0:
            progress = self.remaining_seconds / self.total_seconds
            pen.setColor(QColor("#ff5555"))
            pen.setCapStyle(Qt.RoundCap)
            painter.setPen(pen)

            start_angle = 90 * 16 # Головка линий
            span_angle = int(progress * 360 * 16) # Конец линий
            painter.drawArc(x, y, side, side, start_angle, span_angle)

        # Текст временни (ММ:СС)
        minutes = self.remaining_seconds // 60
        seconds = self.remaining_seconds % 60
        time_text = f"{minutes:02}:{seconds:02}"

        painter.setFont(QFont("Arial", 40, QFont.Bold)) # Значение текста
        painter.setPen(QColor("#FFFFFF"))
        painter.drawText(self.rect(), Qt.AlignCenter, time_text) # Вывод по центру таймер


def main():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()