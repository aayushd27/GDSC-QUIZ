import random

class Question:
    def __init__(self, question, options, correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer

    def display_question(self):
        print(self.question)
        for i, option in enumerate(self.options, start=1):
            print(f"{i}. {option}")

class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0
        self.current_question_index = 0
        self.answersheet = {}  # Store user's answers for review

    def add_question(self, question):
        self.questions.append(question)

    def next_question(self):
        if self.current_question_index < len(self.questions):
            self.questions[self.current_question_index].display_question()
            self.current_question_index += 1
        else:
            print("End of the quiz.")
            self.display_score()  # Display the user's score before showing the answer sheet

    def check_answer(self, user_answer):
        current_question = self.questions[self.current_question_index - 1]
        if user_answer == current_question.correct_answer:
            self.score += 2
            print("Correct! Your score is now:", self.score)
        elif user_answer == "D":
            print("You chose 'None of the Above'. The correct answer is:", current_question.correct_answer)
            print("Your score remains unchanged.")
        else:
            self.score -= 1
            print("Incorrect! Your score is now:", self.score)
        self.answersheet[current_question.question] = (current_question.correct_answer, user_answer)

    def remaining_questions(self):
        return len(self.questions) - self.current_question_index

    def display_score(self):
        print("Your final score is:", self.score)

    def display_answersheet(self):
        print("\nAnswer Sheet:")
        for i, question in enumerate(self.questions, start=1):
            correct_answer, user_answer = self.answersheet[question.question]
            print(f"{i}. Question: {question.question}")
            print(f"   Correct Answer: {correct_answer}")
            print(f"   Your Answer: {user_answer}\n")

question1 = Question("Which city is the main campus of BITS Pilani located in?", ["A. Hyderabad", "B. Pilani", "C. Goa", "D. None of the Above"], "B")
question2 = Question("Which year was BITS Pilani founded?", ["A. 1956", "B. 1964", "C. 1972", "D. None of the Above"], "A")
question3 = Question("Which branch of engineering is BITS Pilani's Hyderabad campus known for?", ["A. Computer Science", "B. Electrical Engineering", "C. Mechanical Engineering", "D. None of the Above"], "A")
question4 = Question("What is the official mascot of BITS Pilani?", ["A. Panther", "B. Falcon", "C. Camel", "D. None of the Above"], "C")
question5 = Question("In which state is BITS Pilani's Goa campus located?", ["A. Maharashtra", "B. Goa", "C. Karnataka", "D. None of the Above"], "B")

# Create a quiz and add questions
quiz = Quiz()
quiz.add_question(question1)
quiz.add_question(question2)
quiz.add_question(question3)
quiz.add_question(question4)
quiz.add_question(question5)

# Display the marking scheme
print("Marking Scheme:")
print("Correct Answer: +2 points")
print("Incorrect Answer or 'None of the Above' (D): -1 point")
print("-----------------------------------------------------------")

# Start the quiz
while quiz.remaining_questions() > 0:
    quiz.next_question()
    user_answer = input("Enter your answer (A, B, C, D for 'None of the Above'): ").upper()
    quiz.check_answer(user_answer)

# Display the score and prompt to see the answer sheet
quiz.display_score()
view_answersheet = input("Would you like to view the answer sheet? (Y/N): ").lower()
if view_answersheet == "y":
    quiz.display_answersheet()
