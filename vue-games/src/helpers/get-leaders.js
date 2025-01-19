const { Pool } = require('pg');

// Configure the PostgreSQL connection
const pool = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: 'play2learn',
  password: 'Yag3hebi',
  port: 5432,
});

// Function to get data from the table
const getData = async () => {
  try {
    const res = await pool.query('SELECT s.user_id, s.score, s.max_number, u.first_name, u.last_name \
        FROM games_ascore AS s \
        JOIN users_customuser AS u ON s.user_id=u.id \
        ORDER BY s.score DESC LIMIT 3');
    console.log(res.rows); // Output the rows
  } catch (err) {
    console.error('Error executing query', err.stack);
  }
};

// Call the function
getData();