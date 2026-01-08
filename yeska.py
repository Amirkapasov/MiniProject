import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton
from PyQt5.QtCore import QTimer

app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Timer")
window.resize(300, 200)


pause_button = QPushButton("Pause", window)
pause_button.setGeometry(150, 130, 100, 40)
paused = False

reset = QPushButton("Reset", window)
reset.setGeometry(50, 130, 100, 40)

label = QLabel(window)
label.setGeometry(119, 80, 100, 40)
label.setStyleSheet("font-size: 24px;")

Start_time = 10
time_left = Start_time


def update_timer():
    global time_left
    if time_left < 0:
        timer.stop()
        return
    minutes = time_left // 60
    sec = time_left % 60

    label.setText(f"{minutes:02}:{sec:02}")
    time_left -= 1

def tooglePause():
    global paused
    if not paused:
        timer.stop()
        pause_button.setText("Resume")
        paused = True
    else:
        timer.start()
        pause_button.setText("Pause")
        paused = False

def reset_timer():
    global time_left, paused
    timer.stop()
    paused = False
    time_left = Start_time

    minutes = time_left // 60
    sec = time_left % 60
    label.setText(f"{minutes:02}:{sec:02}")

    pause_button.setText("Pause")

timer = QTimer()
timer.setInterval(1000)
timer.timeout.connect(update_timer)
timer.start()
pause_button.clicked.connect(tooglePause)
reset.clicked.connect(reset_timer)

window.show()
sys.exit(app.exec_())
