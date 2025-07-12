@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    feedback = []

    for i, q in enumerate(questions):
        user_answer = request.form.get(f'q{i}')
        correct = user_answer == q['answer']
        if correct:
            score += 1
        feedback.append({
            "question": q['question'],
            "user_answer": user_answer,
            "correct_answer": q['answer'],
            "is_correct": correct
        })

    message = random.choice([
        "Well done, Code Wizard! 🧙‍♂️",
        "Python Ninja mode activated! 🐍",
        "You’re climbing the debug mountain! ⛰️",
        "Keep coding, quiz master! 🔥"
    ])

    return render_template("result.html", score=score, total=len(questions), message=message, feedback=feedback)