from flask import Flask, render_template, request

app = Flask(__name__)

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
        return render_template('submit.html', name=name, leave_type=leave_type, start=start, end=end)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


