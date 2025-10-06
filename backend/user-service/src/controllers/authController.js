require('dotenv').config(); // Load environment variables from .env
const db = require('../models/userModel');
const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');

// Use secret from environment or fallback
const JWT_SECRET = process.env.JWT_SECRET || 'dev-secret';

const register = (req, res) => {
  const { username, password } = req.body;
  if (!username || !password) {
    return res.status(400).json({ message: "Missing fields" });
  }

  bcrypt.hash(password, 10, (err, hash) => {
    if (err) {
      return res.status(500).json({ message: err.message });
    }

    db.run(
      'INSERT INTO users(username, password) VALUES(?, ?)',
      [username, hash],
      function (err) {
        if (err) {
          return res.status(400).json({ message: "Username already exists" });
        }
        res.json({
          message: "User registered successfully",
          userId: this.lastID,
        });
      }
    );
  });
};

const login = (req, res) => {
  const { username, password } = req.body;

  db.get('SELECT * FROM users WHERE username = ?', [username], (err, user) => {
    if (err) return res.status(500).json({ message: err.message });
    if (!user) return res.status(400).json({ message: "User not found" });

    bcrypt.compare(password, user.password, (err, result) => {
      if (err) return res.status(500).json({ message: err.message });
      if (!result) return res.status(400).json({ message: "Invalid credentials" });

      const token = jwt.sign(
        { userId: user.id, username: user.username },
        JWT_SECRET,
        { expiresIn: '1h' }
      );

      res.json({ token });
    });
  });
};

const profile = (req, res) => {
  const authHeader = req.headers.authorization;
  if (!authHeader) return res.status(401).json({ message: "Unauthorized" });

  const token = authHeader.split(' ')[1];

  jwt.verify(token, JWT_SECRET, (err, decoded) => {
    if (err) return res.status(401).json({ message: "Invalid token" });

    db.get('SELECT id, username FROM users WHERE id = ?', [decoded.userId], (err, user) => {
      if (err) return res.status(500).json({ message: err.message });
      res.json({ user });
    });
  });
};

module.exports = { register, login, profile };
 
