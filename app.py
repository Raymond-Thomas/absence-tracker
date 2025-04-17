from flask import Flask, render_template, request, redirect
from datetime import datetime

app = Flask(__name__)
leave_requests = []

@app.route('/')
def index():
    return render_template('index.html', requests=leave_requests)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        leave_requests.append({
            'name': request.form['name'],
            'type': request.form['type'],
            'start': request.form['start'],
            'end': request.form['end'],
            'status': 'Pending',
            'submitted': datetime.now().strftime("%Y-%m-%d %H:%M")
        })
        return redirect('/')
    return render_template('submit.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
