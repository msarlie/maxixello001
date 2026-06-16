# Student Registration System (SRS)

A lightweight, terminal-based CRUD (Create, Read, Update, Delete) application built using Python. This system allows administrative users to manage student enrollment data efficiently with permanent storage using a local JSON database.

---

## 🚀 Core Features

*   **Create (Register Student):** Adds new students to the system with an enforcement layer checking for unique IDs and blocking blank entries.
*   **Read (View All / Search):** Displays all registered student records in a clean, tabular column layout or searches for an individual profile instantaneously via their Student ID.
*   **Update (Edit Profile):** Modifies names or registered courses of current profiles while seamlessly preserving untouched records when fields are left blank.
*   **Delete (Remove Record):** Permanently wipes out a student record from the active directory using their unique ID.
*   **Data Persistence:** Automatically stores and reads data from a local JSON document database so information is never lost when exiting the system.

---

## 🛠️ Tech Stack & Architecture

*   **Language:** Python 3.11+
*   **Database / Storage:** JSON (JavaScript Object Notation) file-based serialization (`students.json`).
*   **Architecture:** Command-Line Interface (CLI) utilizing a structural control loop.

---

## 📦 System File Structure

```text
student registration system/
│
├── main.py            # Main application source code containing runtime logic
├── students.json      # Permanent database storage file (generates automatically)
└── README.md          # Technical documentation and installation instructions
```

---

## 💻 How to Run the Application

### Prerequisites
Ensure that Python 3 is installed on your operating system.

### Running the App
1. Open your system terminal or command prompt inside the project directory.
2. Run the application using the following execution command:
   ```bash
   python main.py
   ```
3. Use the numeric keypad values (`1` through `6`) to seamlessly navigate and execute administrative tasks within the application menu framework.
4.