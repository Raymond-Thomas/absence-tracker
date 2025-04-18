from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Setup database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////home/data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define the LeaveRequest model
class LeaveRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    type = db.Column(db.String(50))
    start = db.Column(db.String(20))
    end = db.Column(db.String(20))

# Create the database table
with app.app_context():
    db.create_all()

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the form submission page (handles both GET and POST)
@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        name = request.form.get('name')
        leave_type = request.form.get('type')
        start = request.form.get('start')
        end = request.form.get('end')

        # Save to database
        new_request = LeaveRequest(name=name, type=leave_type, start=start, end=end)
        db.session.add(new_request)
        db.session.commit()

        return render_template('submit.html', name=name, leave_type=leave_type, start=start, end=end)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
