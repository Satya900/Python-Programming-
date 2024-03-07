class Person :
    pass

per_obj = Person()
print(per_obj)
class Student :
    def __init__(self, email_id, subject, hobby):
        self.email_id = email_id
        self.subject = subject
        self.hobby = hobby

stud1 = Student(123,"Python","Cricket")

print(stud1.hobby)