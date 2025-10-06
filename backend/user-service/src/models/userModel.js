require('dotenv').config();
const sqlite3 = require('sqlite3').verbose();

// Load from environment or fallback
const dbPath = process.env.DB_PATH || './users.db';
const db = new sqlite3.Database(dbPath);

// Create table if not exists
db.run(`CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)`);

module.exports = db;
 
