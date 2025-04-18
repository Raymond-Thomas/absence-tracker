from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route for the submission page
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    leave_type = request.form.get('type')
    start = request.form.get('start')
    end = request.form.get('end')
    return render_template('submit.html', name=name, leave_type=leave_type, start=start, end=end)


if __name__ == '__main__':
    app.run(debug=True)


