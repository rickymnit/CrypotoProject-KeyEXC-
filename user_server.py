from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_input', methods=['POST'])
def process_input():
    user_input = request.form['user_input']
    # Do something with the user input, e.g., print it
    print("User input:", user_input)
    return "Input received: {}".format(user_input)

if __name__ == '__main__':
    app.run(debug=True)
