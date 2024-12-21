
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
app.secret_key = "your_secret_key"

def get_db_connection():
    conn = sqlite3.connect('MainDB.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def vendor_management():
    conn = get_db_connection()
    vendors = conn.execute('SELECT * FROM vendors').fetchall()
    conn.close()
    return render_template('vendor_management.html', vendors=vendors)

@app.route('/reject/<int:vendor_id>')
def reject_vendor(vendor_id):
    conn = get_db_connection()
    conn.execute('DELETE FROM vendors WHERE id = ?', (vendor_id,))
    conn.commit()
    conn.close()
    return redirect(url_for('vendor_management'))


@app.route('/approve/<int:vendor_id>')
def approve_vendor(vendor_id):
    conn = get_db_connection()
    conn.execute('UPDATE vendors SET status = ? WHERE id = ?', ('approved', vendor_id))
    conn.commit()
    conn.close()
    return redirect(url_for('vendor_management'))

if __name__ == '__main__':
    app.run(debug=True)
