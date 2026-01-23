# 📚 Mini Library Manager

A simple Python-based library management system built as part of **Lara Tech Internship – Agentic AI Bootcamp (Week 2)**.  
This project allows users to manage books locally using JSON, fetch book details from an external API, and generate CSV reports automatically.

---

## 🚀 Features

- Store books persistently in JSON format  
- Add new books  
- List all stored books  
- Search books by title or author  
- Fetch book details using an external API  
- Generate CSV report automatically  

---

## 🛠️ Tech Stack

- Python 3
- requests
- json
- csv
- pathlib

---

## 📂 Project Structure

```
mini-library-manager/
├── src/
│   ├── mini_library_manager.py
│   ├── books_report.csv
│   └── data/
│       └── books.json
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```
git clone https://github.com/Ishashetty07/mini-library-manager.git
cd mini-library-manager
```

### 2️⃣ (Optional) Create Virtual Environment
```
python -m venv .venv
```

**Windows**
```
.venv\Scripts\activate
```

**Mac / Linux**
```
source .venv/bin/activate
```

### 3️⃣ Install Dependencies
```
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```
python src/mini_library_manager.py
```

---

## 📖 Menu Options

```
1. Add Book
2. List Books
3. Search Books
4. Fetch Books from API
5. Generate CSV Report
6. Exit
```

---

## 🌐 API Used

**Open Library Search API**  
https://openlibrary.org/search.json

Used to fetch:
- Book title
- Author(s)
- First publish year

---

## 📄 Data Storage

- Books stored at:  
  `src/data/books.json`

- CSV report generated at:  
  `src/books_report.csv`

---

## 🎯 Learning Outcomes

- JSON & CSV file handling
- REST API integration
- CLI-based Python application
- Path handling using pathlib
- Modular and clean code structure

---

## 👤 Author

**Isha Shetty**  
Lara Tech Internship – Agentic AI Bootcamp  
Week 2 Assignment

---

## ✅ Project Status

✔️ Completed  
✔️ Tested  
✔️ Ready for GitHub Submission
