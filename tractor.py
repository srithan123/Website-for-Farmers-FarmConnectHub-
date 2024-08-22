from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Function to create SQLite3 table if not exists
def create_table():
    conn = sqlite3.connect('farmers.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS tractors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    brand TEXT,
                    location TEXT,
                    year INTEGER,
                    horsepower INTEGER
                )''')
    conn.commit()
    conn.close()

# Route to render HTML form for tractor registration
@app.route('/')
def tractor_form():
    return render_template('tractor_form.html')

# Route to handle form submission and insert data into SQLite3
@app.route('/register', methods=['POST'])
def register_tractor():
    brand = request.form['brand']
    location = request.form['location']
    year = request.form['year']
    horsepower = request.form['horsepower']

    conn = sqlite3.connect('farmers.db')
    c = conn.cursor()
    c.execute("INSERT INTO tractors (brand, location, year, horsepower) VALUES (?, ?, ?, ?)", (brand, location, year, horsepower))
    conn.commit()
    conn.close()

    return redirect(url_for('tractor_form'))

if __name__ == '__main__':
    create_table()  # Create the table if not exists
    app.run(debug=True)
