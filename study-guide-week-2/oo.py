# Create your classes here

class Student:
    """Create a student instance"""

    def __init__(self, first_name, last_name, address):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address

class Question:
    """Create a question instance"""

    def __init__(self, question, correct_answer):
        self.question = question
        self.correct_answer = correct_answer

    def ask_and_evaluate(self):
        return self.correct_answer == input(f'{self.question} > ')

class Exam:
    """Create an exam instance"""

    def __init__(self, name):
        self.questions = []
        self.name = name

    def add_question(self, question):
        self.questions.append(question)

    def administer(self):
        correct = 0
        for question in self.questions:
            if question.ask_and_evaluate():
                correct += 1
        return correct / len(self.questions)

class StudentExam():

    def __init__(self, student, exam):
        self.student = student
        self.exam = exam
        self.score = None

    def take_test(self):
        self.score = self.exam.administer()
        print(f'{self.score:0.2f}')

def example():

    exam = Exam('Exam 1')
    exam.add_question(Question('What is 2 + 2', '4'))
    exam.add_question(Question('What is 1 + 1?', '2'))
    test_student = Student('First', 'Last', 'address')
    student_exam = StudentExam(test_student, exam)

    return student_exam.take_test()

example()