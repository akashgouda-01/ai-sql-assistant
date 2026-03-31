# AI-Powered SQL Query Generator (Gemini + Streamlit)

## 🚀 Overview

This project is an AI-powered application that converts natural language questions into SQL queries and executes them on a database.

Users can interact with a database without writing SQL, making data access simple and intuitive.

---

## 🧠 Features

* Natural Language → SQL conversion
* Real-time query execution
* Streamlit-based interactive UI
* Google Gemini API integration
* Dynamic database querying

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Google Gemini API
* SQLite

---

## ⚙️ How It Works

1. User enters a question in natural language
2. Gemini converts it into an SQL query
3. The query is executed on a SQLite database
4. Results are displayed in the UI

---

## 📦 Installation

```bash
git clone https://github.com/akashgouda-01/ai-sql-assistant.git
cd ai-sql-assistant
pip install -r requirements.txt
```

---

## 🗄️ Database Setup

Before running the app, initialize the database:

```bash
python sql.py
```

This will:

* Create the `STUDENT` table
* Insert sample data

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory and add:

```bash
GOOGLE_API_KEY=your_api_key_here
```

---

## 📊 Example

**Input:**

```
Show all students in AI class
```

**Generated SQL:**

```
SELECT * FROM STUDENT WHERE CLASS = "AI";
```

---

## 🚧 Challenges Faced

* Setting up and managing virtual environments
* Handling API errors and model selection
* Cleaning AI-generated SQL queries
* Fixing database errors like missing tables

---

## 🚀 Future Improvements

* Chat-based interface with memory
* Support for multiple tables
* Query validation and error handling
* Deployment on cloud platforms

---

## 👨‍💻 Author

Akash Kumar Gouda
=======
