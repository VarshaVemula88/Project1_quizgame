questions = ("Which keyword is used for function in python?: ",
                       "Which character is used for single line comments in python?: ",
                       "Which is the correct extension of python file?: ",
                       "What is the maximum length of python identifier?: ",
                       "In which year python 3.0 was developed?: ")

options = (("A. fun", "B. function", "C. def", "D. define"),
                   ("A. /*", "B. !", "C. //", "D. #"),
                   ("A. .py", "B. .python", "C. .pl", "D. .p"),
                   ("A. no fixed length ", "B. 32", "C. 16", "D. 18"),
                   ("A. 2000", "B. 2008", "C. 2010", "D. 2005"))

answers = ("C", "D", "A", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("----------------------")
print("       RESULTS        ")
print("----------------------")

print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")