🖱️ Virtual Mouse Using Hand Gestures

Control your computer's mouse using hand gestures and a webcam — no physical mouse required!

This Python project uses computer vision and hand tracking to translate hand movements into mouse actions such as cursor movement, clicking, and scrolling.

✨ Features

- 🖐️ Hand gesture recognition using a webcam
- 🖱️ Mouse cursor control using hand movements
- 👆 Left-click using a pinch gesture
- 🤏 Right-click using a finger gesture
- 📜 Scroll using raised fingers
- ⚡ Real-time gesture processing
- 🐍 Built with Python

🛠️ Technologies Used

- Python — Core programming language
- OpenCV — Webcam and image processing
- MediaPipe — Hand landmark detection
- PyAutoGUI — Mouse automation

📁 Project Structure

virtual-mouse/
│
├── main.py
├── gesture_controller.py
├── requirements.txt
├── README.md
└── .gitignore

Your actual project structure may differ depending on your implementation.

⚙️ Requirements

- Python 3.10 or another version compatible with your installed dependencies
- A working webcam
- Windows, macOS, or Linux desktop
- Internet access for installing dependencies

🚀 Installation

1. Clone the repository

git clone YOUR_GITHUB_REPOSITORY_URL
cd virtual-mouse

Replace "YOUR_GITHUB_REPOSITORY_URL" with your repository's actual URL.

2. Create a virtual environment

Windows:

python -m venv venv
venv\Scripts\activate

3. Install dependencies

pip install -r requirements.txt

If you don't have a "requirements.txt" file yet, install the required packages:

pip install opencv-python mediapipe pyautogui

Make sure these packages are compatible with your Python version.

4. Run the application

python main.py

Allow webcam access if prompted.

🖐️ Gesture Controls

