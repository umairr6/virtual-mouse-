#🖱️ Virtual Mouse Using Hand Gestures

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

Gesture| Action
Move your hand/index finger| Move the mouse cursor
Touch thumb and index finger| Left-click
Touch index and middle fingers| Right-click
Raise index and middle fingers| Scroll

Gesture behavior depends on the gesture detection logic implemented in your source code.

🧠 How It Works

1. The webcam captures live video.
2. OpenCV processes the video frames.
3. MediaPipe detects hand landmarks and finger positions.
4. The program interprets those landmarks as gestures.
5. PyAutoGUI performs the corresponding mouse actions.

🔧 Troubleshooting

Webcam not opening

- Close other applications that may be using the webcam.
- Check camera permissions and your camera index in "main.py".

Module not found

- Activate your virtual environment.
- Install the missing dependency using "pip".

Mouse clicks happen repeatedly

- Adjust the gesture detection threshold or action delay.
- Add a gesture-release requirement before allowing another click.

Cursor movement is inaccurate

- Adjust coordinate mapping and smoothing settings in "main.py".

Application does not start

- Check the Python version and dependency compatibility.
- Read the error message in the VS Code terminal.

🔒 Safety Note

This application can control your real mouse. Test it carefully, keep your hands away from unintended click gestures, and provide a reliable way to stop the program.

🔮 Future Improvements

- Add drag-and-drop functionality.
- Add volume and brightness controls.
- Add customizable gestures.
- Improve cursor smoothing and tracking accuracy.
- Add a graphical user interface.
- Support more hand gestures and accessibility features.

🤝 Contributing

Contributions, suggestions, and bug reports are welcome!

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

📄 License

This project can be distributed under the MIT License. Add a "LICENSE" file to the repository if you choose to use that license.

---

Built with Python and computer vision.
