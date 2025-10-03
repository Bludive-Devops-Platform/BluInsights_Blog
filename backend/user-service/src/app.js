require('dotenv').config();
const express = require('express');
const cors = require('cors');
const authRoutes = require('./routes/authRoutes');

const app = express();
app.use(cors());
app.use(express.json());
app.use('/api', authRoutes);

const PORT = process.env.PORT || 5050;
app.listen(PORT, ()=>console.log(`User Service running on port ${PORT}`));
