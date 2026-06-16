const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database('./school.db');

// Create the students table if it does not exist
db.serialize(() => {
  db.run(`
    CREATE TABLE IF NOT EXISTS students (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      firstName TEXT NOT NULL,
      lastName TEXT NOT NULL,
      email TEXT UNIQUE NOT NULL,
      gradeLevel TEXT NOT NULL
    )
  `);
});

module.exports = db;