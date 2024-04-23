from flask import Flask, render_template, redirect, url_for, request, session
import sqlite3
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(120)  # Generates a 240-character long hexadecimal string

# SQLite3 database connection
conn = sqlite3.connect('database.db')
cursor = conn.cursor()

@app.after_request
def add_no_cache_headers(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

@app.route('/')
def home():
    return render_template('home.html', title="PMS Tracker")

@app.route('/signup')
def signup():
    return render_template('signup.html', title="Sign Up - PMS Tracker")

@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        username = session['username']
        return render_template('dashboard.html', title="User Dashboard", username=username)
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login form submission
        username = request.form['username']
        password = request.form['password']

        # Perform user authentication (check username and password against database)
        # If authentication successful, set session variable
        # For simplicity, let's assume the authentication is successful
        session['username'] = username
        return redirect(url_for('dashboard'))
    else:
        return render_template('login.html', title="Login - PMS Tracker")

@app.route('/logout')
def logout():
    # Clear the session (log out the user)
    session.pop('username', None)
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True, port=27095, host='0.0.0.0')
