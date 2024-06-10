from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Used for session management

@app.route('/')
def index():
    session['secret_number'] = random.randint(1, 100)
    session['attempts'] = 0
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    session['attempts'] += 1
    
    if guess == session['secret_number']:
        message = f"Congratulations! You guessed the number in {session['attempts']} attempts."
        return render_template('result.html', message=message)
    elif guess < session['secret_number']:
        message = "Try a higher number."
    else:
        message = "Try a lower number."
    
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
