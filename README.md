# 🖐️ Gesture AI Drawing App

An AI-powered **Hand Gesture Drawing Application** built using **Flask, OpenCV, MediaPipe, and OpenAI**.
This system allows users to **draw, write, and control a digital canvas using hand gestures through a webcam**.

The application detects hand movements and translates them into **drawing actions such as writing, selecting colors, erasing, and clearing the canvas**.

---

# 🚀 Features

* ✏️ **Air Drawing** – Draw or write in the air using finger gestures
* 🎨 **Color Selection** – Change drawing color using specific gestures
* 🧽 **Erase Mode** – Remove drawings with hand gesture
* 🖐️ **Real-Time Hand Tracking** – Detect fingers using MediaPipe
* 📷 **Webcam Integration** – Control drawing without mouse or keyboard
* 🤖 **AI Text Processing** – Convert handwriting into readable text using OpenAI
* 💾 **Save Drawings** – Store drawings for later use

---

# 🧠 Technologies Used

## Backend

* Python
* Flask

## Computer Vision

* OpenCV
* MediaPipe

## AI Integration

* OpenAI API

## Frontend

* HTML
* CSS
* JavaScript
* Canvas API

---

# 📂 Project Structure

```
gesture-ai-drawing-app
│
├── app.py
├── config.py
├── requirements.txt
├── README.md
│
├── models
│   └── gesture_model.py
│
├── utils
│   ├── hand_tracking.py
│   ├── gesture_detection.py
│   ├── drawing_utils.py
│   └── ai_processing.py
│
├── static
│   ├── css
│   │   └── style.css
│   ├── js
│   │   └── script.js
│   ├── images
│   │   └── icons.png
│   └── canvas
│       └── drawings
│
├── templates
│   ├── index.html
│   └── layout.html
│
├── api
│   ├── routes.py
│   └── ai_routes.py
│
├── camera
│   └── camera_stream.py
│
└── data
    └── saved_drawings.json
```

---

# ⚙️ Installation

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/gesture-ai-drawing-app.git
```

```
cd gesture-ai-drawing-app
```

---

### 2️⃣ Create Virtual Environment

```
python -m venv venv
```

Activate environment:

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

# ▶️ Running the Application

Start the Flask server:

```
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

# 🖐️ Hand Gesture Controls

| Gesture          | Action       |
| ---------------- | ------------ |
| Index Finger Up  | Draw         |
| Two Fingers Up   | Move Cursor  |
| Three Fingers Up | Change Color |
| Closed Fist      | Erase        |
| Open Palm        | Clear Canvas |

---

# 🤖 OpenAI Integration

OpenAI is used for:

* Handwriting recognition
* Text correction
* AI interpretation of drawn shapes

Set your API key inside **config.py**

Example:

```
OPENAI_API_KEY = "your_openai_api_key"
```

---

# 📊 Application Workflow

```
Webcam
   ↓
Hand Detection (MediaPipe)
   ↓
Gesture Recognition
   ↓
Canvas Drawing
   ↓
AI Processing (OpenAI)
   ↓
Output Text / Drawing
```

---

# 🔮 Future Improvements

* 🧠 AI shape recognition
* 👥 Multi-user collaborative whiteboard
* 📱 Mobile support
* ☁️ Cloud storage for drawings
* 🗣 Voice command support

---

# 👨‍💻 Author

**Sanket Khapake**

Aspiring **Data Scientist & Full Stack Developer**
Skilled in **Python, MERN Stack, Machine Learning, and Data Analytics**

---

# ⭐ Support

If you like this project:

⭐ Star the repository
🍴 Fork the project
🛠 Contribute improvements

---

# 📜 License

This project is open-source and available under the **MIT License**.
