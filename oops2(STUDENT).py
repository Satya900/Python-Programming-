class Student:
    def __init__(self, email_id, subject, hobby):
        self.email_id = email_id
        self.subject = subject
        self.hobby = hobby

stud1 = Student(123, "Python", "Cricket")
stud2 = Student(145,"C++","Dancing")
print("Student 1 loves {}".format(stud1.hobby))
print("Student 1 favourite subject is {}".format(stud1.subject))