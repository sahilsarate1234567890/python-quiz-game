import os
from flask import Flask, render_template, request
from questions import questions

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for i, q in enumerate(questions):
        user_answer = request.form.get(f'q{i}')
        if user_answer == q['answer']:
            score += 1
    return render_template('result.html', score=score, total=len(questions))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)