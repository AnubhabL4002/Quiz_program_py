class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False)")
        correct_answer = self.question_list[self.question_number-1].answer
        self.is_correct(user_answer, correct_answer)

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def is_correct(self, user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score+=1
            print(f"Correct!\nScore: {self.score}/{self.question_number}")
        else:
            print(f"Wrong!\nScore: {self.score}/{self.question_number}\nThe correct answer was: {correct_answer}")
        print("\n")