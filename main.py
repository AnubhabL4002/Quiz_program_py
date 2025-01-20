from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    new_question = Question(question["text"], question["answer"])
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
try:
    while quiz.still_has_questions():
        quiz.next_question()
    print(f"\n*******📄 Your Final Score: {quiz.score}/{len(question_bank)} ✔️*******")
except KeyboardInterrupt:
    print("\nProgram stopped by user.")