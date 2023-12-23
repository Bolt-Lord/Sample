from quiz_brain import QuizBrain
from data import question_bank_list

quiz = QuizBrain(question_bank_list())
while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
