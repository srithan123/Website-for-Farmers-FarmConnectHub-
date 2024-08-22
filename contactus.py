from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

#create a database and table to store details of the users
conn = sqlite3.connect('farmers.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS customer_feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT NOT NULL,
        state TEXT NOT NULL,
        subject TEXT NOT NULL
    )
''')
conn.commit()
conn.close()

@app.route('/')
def index():
    """
    #Display available slots
    conn = sqlite3.connect('farmers.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM customers_feedback')
    slots = cursor.fetchall()
    conn.close()
    """
    return render_template('contactus.html')


@app.route('/book' , methods=['POST'])
def book():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        phone=request.form['phone']
        email=request.form['email']
        state = request.form['state']
        subject = request.form['subject']

        #insert booked slot into the database
        conn = sqlite3.connect('farmers.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO customer_feedback (first_name, last_name, phone, email, state, subject) VALUES (?, ?, ?, ?, ?, ?)',
                       (first_name, last_name, phone, email, state, subject))
        conn.commit()
        conn.close()

        return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(debug=True)