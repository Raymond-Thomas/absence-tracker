from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///leave_requests.db'
db = SQLAlchemy(app)

class LeaveRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    type = db.Column(db.String(50))
    start = db.Column(db.String(20))
    end = db.Column(db.String(20))
    status = db.Column(db.String(20), default='Pending')
    submitted = db.Column(db.DateTime, default=datetime.utcnow)

@app.route('/')
def index():
    requests = LeaveRequest.query.all()
    return render_template('index.html', requests=requests)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        new_request = LeaveRequest(
            name=request.form['name'],
            type=request.form['type'],
            start=request.form['start'],
            end=request.form['end']
        )
        db.session.add(new_request)
        db.session.commit()
        return redirect('/')
    return render_template('submit.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
