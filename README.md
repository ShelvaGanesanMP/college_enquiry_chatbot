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

## Screenshot
<img width="1060" height="526" alt="image" src="https://github.com/user-attachments/assets/df936e4f-ed5a-46d5-a4e4-cc7bf5ee4cf1" />
<img width="1046" height="493" alt="image" src="https://github.com/user-attachments/assets/fe47f5b2-d4bb-405c-9d94-b06abb1e7456" />
<img width="1046" height="444" alt="image" src="https://github.com/user-attachments/assets/6662f390-b9fc-4ac3-8143-ad73a8227e85" />
<img width="1046" height="360" alt="image" src="https://github.com/user-attachments/assets/c8e0f93c-7592-4da4-8c4e-5c64593832a8" />
<img width="1046" height="378" alt="image" src="https://github.com/user-attachments/assets/b6872119-b780-4d1b-96c3-336d5d38ab9e" />
<img width="1046" height="406" alt="image" src="https://github.com/user-attachments/assets/8ed833de-d8e0-49af-8442-b2e9f9ae1d74" />
<img width="1044" height="316" alt="image" src="https://github.com/user-attachments/assets/ab5d08db-2635-4554-b726-8693fa267f2d" />
<img width="1046" height="511" alt="image" src="https://github.com/user-attachments/assets/afb4563e-1220-459d-ac69-1304507129b5" />
<img width="1059" height="525" alt="image" src="https://github.com/user-attachments/assets/81725f59-8abd-4c7e-a989-98561168e88d" />
<img width="1085" height="524" alt="image" src="https://github.com/user-attachments/assets/82024ef5-a315-48cb-81cd-3124e7c3f361" />
<img width="1055" height="520" alt="image" src="https://github.com/user-attachments/assets/d7ff1c0d-3003-48ba-8b0c-7f594b677d31" />











