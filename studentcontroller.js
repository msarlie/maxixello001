const db = require('./database');

// CREATE: Add a new student
exports.createStudent = (req, res) => {
  const { firstName, lastName, email, gradeLevel } = req.body;
  const sql = `INSERT INTO students (firstName, lastName, email, gradeLevel) VALUES (?, ?, ?, ?)`;
  
  db.run(sql, [firstName, lastName, email, gradeLevel], function(err) {
    if (err) return res.status(400).json({ error: err.message });
    res.status(201).json({ id: this.lastID, firstName, lastName, email, gradeLevel });
  });
};

// READ: Get all students
exports.getAllStudents = (req, res) => {
  const sql = `SELECT * FROM students`;
  
  db.all(sql, [], (err, rows) => {
    if (err) return res.status(500).json({ error: err.message });
    res.json(rows);
  });
};

// UPDATE: Update a student's information
exports.updateStudent = (req, res) => {
  const { firstName, lastName, email, gradeLevel } = req.body;
  const sql = `UPDATE students SET firstName = ?, lastName = ?, email = ?, gradeLevel = ? WHERE id = ?`;
  
  db.run(sql, [firstName, lastName, email, gradeLevel, req.params.id], function(err) {
    if (err) return res.status(400).json({ error: err.message });
    if (this.changes === 0) return res.status(404).json({ error: "Student not found" });
    res.json({ message: "Student updated successfully" });
  });
};

// DELETE: Remove a student
exports.deleteStudent = (req, res) => {
  const sql = `DELETE FROM students WHERE id = ?`;
  
  db.run(sql, req.params.id, function(err) {
    if (err) return res.status(500).json({ error: err.message });
    if (this.changes === 0) return res.status(404).json({ error: "Student not found" });
    res.status(204).send();
  });
};