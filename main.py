from questions import QUESTIONS
import random

score = 0
random.shuffle(QUESTIONS)  # Shuffle the questions to add variety each time
quiz_questions = random.sample(QUESTIONS, 10)
print("Welcome to the quiz! Let's get started.\n")

for i in range(len(quiz_questions)):
    question = quiz_questions[i]
    print(f"Question: {question['question']}")
    print("Options:")
    for option in question['options']:
        print(option)
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == question['answer']:
        print("Correct! Well done.\n")
        score += 1
    else:
        print("Incorrect. Better luck next time.\n")

print(f"Your score is: {score}/{len(quiz_questions)}")
                


