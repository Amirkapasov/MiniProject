# 🍅 Pomodoro Timer (PyQt5)

A sleek, minimalist Pomodoro application built with Python and PyQt5. This tool helps you manage your work sessions with a visual countdown and audio notifications.

## ✨ Features
* **Circular Progress Visualization**: A dynamic red arc that depletes as time runs out.
* **Simple Controls**: Dedicated "Start" and "Stop" buttons to manage your session.
* **Audio Alerts**: Automatically plays a notification sound when the timer reaches zero.
* **Dark Mode**: A clean, modern dark interface designed to reduce eye strain.
* **Custom Duration**: Set your focus time (in minutes) via the console upon launch.

---

## 🚀 Getting Started

### 1. Prerequisites
Ensure you have Python 3.x installed. You will need the **PyQt5** and **PyQt5-QtMultimedia** libraries.

```bash
pip install PyQt5 PyQt5-QtMultimedia
```
### 2. Configuration
The application uses a local path for the notification sound. Update line 22 in the script with the correct path to your audio file:
```bash
sound_path = "your/path/to/sound/file.mp3"
```
### 3. Running the App
1. Run the script:
```bash
python main.py
```
2. Enter the desired focus time in minutes when prompted in the terminal.

3. The GUI window will appear, and you can start your session.

## 🛠 Technical Stack

* **Language:** Python 3
* **Framework:** PyQt5
    * **QPainter:** Used for custom high-quality graphics and anti-aliased drawing.
    * **QTimer:** Handles the precision countdown logic.
    * **QMediaPlayer:** Manages audio playback for session completion.

---

## 📐 How it Works

The application calculates the ratio of remaining time to total time. It then renders a circular arc using the following formula:

$$\text{Span Angle} = \frac{\text{Remaining Seconds}}{\text{Total Seconds}} \times 360^\circ$$

The UI is updated every **1000ms** (1 second) to ensure smooth visual performance and real-time progress tracking.

---

## 📝 Future Roadmap

- [ ] **In-GUI Input:** Implement an input field for time within the window (remove console dependency).
- [ ] **Presets:** Add "Break" and "Long Break" session presets.
- [ ] **Notifications:** Create a system notification pop-up when time is up.
- [ ] **Reset Button:** Add a button to quickly restart the current timer.
