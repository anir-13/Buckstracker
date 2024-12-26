
# Buckstracker

Buckstracker is a Python-based financial management application with a Tkinter GUI for effortless management of income and expenses. It integrates with an SQL database to handle operations such as adding, updating, and deleting records.

---

## Features
- **User Authentication:** Secure login system to access the application.
- **Income Management:** Add, update, and delete income records with descriptions and dates.
- **Expense Management:** Track and manage expenditures with ease.
- **User-Friendly GUI:** Intuitive Tkinter interface to perform all operations without SQL knowledge.

---

## Technologies Used
- **Programming Language:** Python
- **GUI Library:** Tkinter
- **Database:** SQLite (or any SQL database of your choice)

---

## Prerequisites
Before running the application, ensure the following:
- **Python** installed (v3.8 or later recommended)
- Necessary Python libraries:
  - Tkinter (default in Python)
  - `sqlite3` or `MySQL` connector (depending on database choice)

---
## Project Structure
The project follows this structure:


### Explanation of Key Files and Directories:
- **`buckstracker.py`:** The main application file and entry point of the project.
- **`gui/`:** Contains individual scripts for each GUI component (login, income, and expense management).
- **`database/`:** Manages database connections and setup scripts.
- **`README.md`:** The documentation for the project, including setup and usage instructions.
- **`requirements.txt`:** List of required Python libraries for the project.
- **`LICENSE`:** Contains the project's licensing terms.
- **`.gitignore`:** Specifies files and directories that should not be tracked by Git.


## Project structure
Buckstracker/
├── buckstracker.py       # Main application file
├── gui/
│   ├── login.py          # Login form
│   ├── income.py         # Income management form
│   ├── expenditure.py    # Expense management form
├── database/
│   ├── setup.sql         # SQL scripts to create tables
│   ├── connection.py     # Database connection utility
├── README.md             # Project documentation
├── requirements.txt      # Dependencies list (if any)
└── LICENSE               # License file

## Author
- **Anirudh Ramachandran:** 
   - **LinkedIn Profile:** https://www.linkedin.com/in/anirudh-ramachandran-17b44a214/
   - **GitHub Profile:** https://github.com/anir-13
   - **Email:** anirudhraam13@gmail.com


