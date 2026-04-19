# 🎓 College Enquiry Chatbot

An intelligent **AI-powered chatbot web application** designed to handle college-related queries such as courses, admissions, fees, timings, and more.

Built using **Flask + PyTorch + NLP**, this system provides automated responses and includes full **user authentication + admin management**.

---

## 🚀 Features

* 🔐 User Authentication (Login & Register)
* 🤖 AI Chatbot (Neural Network-based)
* 🏫 College Information Pages (Courses, Campus, Library, etc.)
* 🗂️ MySQL Database Integration
* 👨‍💼 Admin Panel for Data Management
* 📩 Contact & Admission Forms
* 🧠 NLP-based Query Understanding

---

## 🧠 How Chatbot Works

* Uses **Natural Language Processing (NLP)**
* Trained on `intents.json`
* Converts user input → Bag of Words
* Predicts intent using **PyTorch Neural Network**
* Returns the most relevant response

---

## 🛠️ Tech Stack

**Backend**

* Python
* Flask

**Frontend**

* HTML, CSS, JavaScript
* Bootstrap

**Database**

* MySQL (PyMySQL)

**AI / ML**

* PyTorch
* NLTK
* NumPy

---

## 📦 Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/yourusername/college_enquiry_chatbot.git
cd college_enquiry_chatbot

---

### 2️⃣ Create Virtual Environment

python -m venv venv

Activate (Windows PowerShell):
venv\Scripts\activate

---

### 3️⃣ Install Dependencies

pip install -r requirements.txt

If needed:
pip install torch nltk numpy flask pymysql

Download NLTK data:
python -c "import nltk; nltk.download('punkt')"

---

### 4️⃣ Setup MySQL Database

Create database:
CREATE DATABASE re;

Create tables:

* acc → user accounts
* adii → admissions
* cc → contacts
* rsp → research
* blo → blood donation

Update DB credentials in `main.py` if needed.

---

### 5️⃣ Run the Application

python main.py

Open in browser:
http://127.0.0.1:5000/

---

## 💬 Chatbot Example Queries

* What courses are available?
* What is the fee structure?
* How many seats are there?
* Where is the college located?

---

## 📁 Project Structure

college_enquiry_chatbot/
│
├── main.py              # Flask app
├── chat.py              # Chatbot logic
├── model.py             # Neural network
├── train.py             # Training script
├── nltk_utils.py        # NLP utilities
├── intents.json         # Training data
├── data.pth             # Trained model
│
├── templates/           # HTML pages
├── static/              # CSS, JS, images
│
├── requirements.txt
└── README.md

---

## ⚠️ Important Notes

* ❌ Do NOT upload `venv/` folder
* Ensure MySQL server is running

---

## 🔧 Troubleshooting

**Torch/NLTK Issues**
pip install torch nltk

**Database Error**
Check MySQL credentials and database

---

## 🌟 Future Improvements

* 🌐 Deploy online (Render / Railway)
* 📱 Mobile responsive UI
* 🎤 Voice-based chatbot
* 🤖 Advanced NLP models

---

## 👨‍💻 Author

Shelva Ganesan M P |
MCA Student |
Web Developer | AI Enthusiast

---

## ⭐ If you like this project

Give it a ⭐ on GitHub!
