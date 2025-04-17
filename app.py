from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    # Redirect root URL straight to the login page
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        user = request.form['username']
        pwd  = request.form['password']
        conn = get_db_connection()
        row = conn.execute(
            'SELECT * FROM users WHERE username = ? AND password = ?',
            (user, pwd)
        ).fetchone()
        conn.close()
        if row:
            return render_template('success.html')

        else:
            error = 'Invalid username or password'
    return render_template('login.html', error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if request.method == 'POST':
        uname = request.form['username']
        email = request.form['email']
        pwd   = request.form['password']
        pwd2  = request.form['confirm_password']

        if pwd != pwd2:
            error = 'Passwords do not match'
        else:
            conn = get_db_connection()
            existing = conn.execute(
                'SELECT * FROM users WHERE username = ? OR email = ?',
                (uname, email)
            ).fetchone()
            if existing:
                error = 'Username or email already taken'
                conn.close()
            else:
                conn.execute(
                    'INSERT INTO users (username, email, password) VALUES (?, ?, ?)',
                    (uname, email, pwd)
                )
                conn.commit()
                conn.close()
                return redirect(url_for('login'))

    return render_template('register.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)
