class QuizeBrain:
    def __init__(self, question_list):
        self.score=0
        self.question_number=0
        self.question_list=question_list
    
    def still_has_questions(self):
        return len(self.question_list) > self.question_number


    def next_question(self):
        obj = self.question_list[self.question_number]
        self.question_number+=1
        ans = input(f"Q.{self.question_number} : {obj.question} (True/False)")
        self.check_answer(ans, obj.answer)

    def check_answer(self, ans, answer):
        if ans.lower() == answer.lower():
            print("You got it!")
            self.score+=1
        else:
            print("That's wrong ")
        print(f"the correct answer was: {answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")

