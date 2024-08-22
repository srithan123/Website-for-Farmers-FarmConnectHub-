# Import necessary modules
from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from datetime import datetime, timedelta
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)

# Create a database and table to store slots
conn = sqlite3.connect('farmers.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS slots (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        address TEXT NOT NULL,
        email TEXT NOT NULL,
        service TEXT NOT NULL,
        date TEXT NOT NULL,
        time TEXT NOT NULL
    )
''')
conn.commit()
conn.close()

# Initialize scheduler for reminders
scheduler = BackgroundScheduler()
scheduler.start()


def send_reminder(email, date, time):
    # Here, you would implement code to send a reminder (e.g., email or notification)
    print(f"Reminder: Your slot on {date} at {time} is coming up! Sent to {email}")


@app.route('/')
def index():
    # Display available slots
    conn = sqlite3.connect('farmers.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM slots')
    slots = cursor.fetchall()
    conn.close()
    return render_template('slot.html', slots=slots)


@app.route('/book', methods=['POST'])
def book():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['phone']
        address = request.form['address']
        email = request.form['email']
        service = request.form['service']
        date = request.form['date']
        time = request.form['time']

        # Insert booked slot into the database
        conn = sqlite3.connect('farmers.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO slots (name, phone, address, email, service, date, time) VALUES (?, ?, ?, ?, ?, ?, ?)',
                       (name, phone, address, email, service, date, time))
        conn.commit()
        conn.close()

        # Schedule a reminder for the booked slot
        reminder_time = datetime.strptime(f"{date} {time}", "%Y-%m-%d %H:%M") - timedelta(hours=1)
        scheduler.add_job(send_reminder, 'date', run_date=reminder_time,
                          args=[email, date, time])

        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
