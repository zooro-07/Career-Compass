import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

from logic.chatbot import chatbot_response

import os
from flask import Flask, render_template, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from logic.quiz_questions import quiz_questions
from logic.career_data import match_careers

app = Flask(__name__)
app.secret_key = os.urandom(24)

users = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
        if uname in users and check_password_hash(users[uname], pwd):
            session['user'] = uname
            return redirect(url_for('quiz'))
        flash('Invalid credentials', 'danger')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        uname = request.form['username']
        pwd = request.form['password']
        if uname in users:
            flash('Username already exists', 'danger')
        else:
            users[uname] = generate_password_hash(pwd)
            flash('Registration successful', 'success')
            return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if 'user' not in session:
        return redirect(url_for('login'))
    if request.method == 'POST':
        answers = request.form.getlist('interest')
        results = match_careers(answers)
        return render_template('result.html', results=results)
    return render_template('quiz.html', questions=quiz_questions)

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/chatbot', methods=['POST'])
def chat():
    user_msg = request.form['message']
    reply = chatbot_response(user_msg)
    return reply
@app.route('/quizbot', methods=['GET', 'POST'])
def quizbot():
    if 'quiz_step' not in session:
        session['quiz_step'] = 0
        session['answers'] = []

    step = session['quiz_step']
    if step >= len(quiz_questions):
        from logic.career_data import match_careers
        result = match_careers(session['answers'])
        session.pop('quiz_step')
        session.pop('answers')
        return render_template('result.html', results=result)

    current_q = quiz_questions[step]

    if request.method == 'POST':
        user_response = request.form['answer']
        if user_response.lower() == 'yes':
            session['answers'].append(current_q['v'])
        session['quiz_step'] += 1
        return redirect(url_for('quizbot'))
    if __name__ == "__main__":
      app.run()
 

      return render_template('quizbot.html', question=current_q['q'])

