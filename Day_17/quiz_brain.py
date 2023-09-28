class QuizBrain:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        question = self.question_list[self.question_number]
        self.question_number += 1
        response = input(f'Q{self.question_number}.{question.text} (True/False): ')
        self.check_answer(response, question.answer)

    def check_answer(self, response, answer):
        if answer.lower() == response.lower():
            self.score += 1
            print("You got it right")
        else:
            print("Wrong")
        print(f"The correct answer is {answer}")
        print(f'Your score is: {self.score}/{self.question_number}\n')
