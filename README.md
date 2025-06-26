# 🧠 AI Chat Log Summarizer

This is a Python-based tool that reads `.txt` chat logs between a **User** and an **AI**, parses the conversation, and generates a simple summary that includes:

- Total number of messages
- Number of messages from User vs. AI
- Top 5 most relevant keywords using TF-IDF

> Built for the **Junior Python Developer (AI-focused)** assessment at Qtec Solution Limited.

---

## 📁 Project Overview

AI_ChatLog_Summarizer/
├── sampleChatLog/
│ ├── chat.txt
│ ├── chat2.txt
│ └── chat3.txt
├── main.py
├── requirements.txt
└── setup.py

---
### Text files is shown below
![Alt Text](screenshots\chat.txt.png)
![Alt Text](screenshots\chat2.txt.png)
![Alt Text](screenshots\chat3.txt.png)

---

## 🚀 Features

- ✅ Parses chat logs by speaker (`User:` and `AI:`)
- ✅ Extracts keyword topics using TF-IDF (with `sklearn`)
- ✅ Shows stats like message count
- ✅ Processes **all `.txt` files in a folder**
- ✅ Clean automation via `setup.py`

---

## ⚙️ Setup Instructions

### 1️. Create Python Environment
We use **conda** with Python 3.10:

```bash
conda create -p venv python=3.10 -y
conda activate ./venv
```

---

### 2️. Auto-generate Project Structure
Run the following Python script to create folder and file structure automatically:
```bash
python setup.py

```
This will create:

-sampleChatLog/ with 3 demo chat files
-main.py
-requirements.txt

---

### 3. Install Required Packages

```bash
pip install -r requirements.txt

```
---

### 4. Running the Summarizer
```bash
python main.py
```

---

### 🧪 Sample Output
```yaml

📄 Summary for: chat.txt
- Total messages: 4
- User messages: 2, AI messages: 2
- Most common keywords: machine, learning, systems, data, field

📄 Summary for: chat2.txt
- Total messages: 6
- User messages: 3, AI messages: 3
- Most common keywords: nlp, language, processing, translate, python

📄 Summary for: chat3.txt
- Total messages: 6
- User messages: 3, AI messages: 3
- Most common keywords: flask, database, django, feature, support

![Terminal Output](screenshots\Summary.png)



```
---
 
### 📦 Dependencies
Python 3.10
nltk
scikit-learn 

---

### 📌 Notes
-TF-IDF automatically excludes common stop words.
-The script supports analyzing multiple chat files from a folder.
-We can customize sampleChatLog/ with our own .txt logs.

---

### 📌 Author
Mohammad Wasif Ahad Linkedin: https://www.linkedin.com/in/wasifahad/ Github: https://github.com/wasif23ahad