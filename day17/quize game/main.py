from question_model import Question
from data import question_data
from quiz_brain import QuizeBrain

question_bank = []

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quize = QuizeBrain(question_bank)


while quize.still_has_questions():
    quize.next_question()
print("You have completed your Quize successfully")

print(f"Your final score is: {quize.score}/{quize.question_number}")