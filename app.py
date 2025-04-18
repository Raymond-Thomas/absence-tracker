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
    reason = request.form.get('reason')
    date = request.form.get('date')
    return render_template('submit.html', name=name, reason=reason, date=date)

if __name__ == '__main__':
    app.run(debug=True)


