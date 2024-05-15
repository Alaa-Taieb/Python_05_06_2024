class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"My name is {self.name} and I am {self.age} years old."
    
class Student(Person):

    def __init__(self, name, age, grade_level):
        super().__init__(name , age)
        self.grade_level = grade_level
        self.grades = []

    def add_grade(self , grade):
        self.grades.append(grade)

    def calculate_grade_average(self):
        if self.grades:
            return sum(self.grades) / len(self.grades)
        return "None"
        

    def introduce(self):
        message = super().introduce()
        message = f"{message} I am a student of the {self.grade_level}th grade."
        message += "\n"
        message += "List of grades: \n"
        for grade in self.grades:
            message += f"{grade} \n"
        return message

class Teacher(Person):
    def __init__(self, name ,age , subject_taught):
        super().__init__(name , age)
        self.subject_taught = subject_taught

    def introduce(self):
        message = super().introduce()
        message = f"{message} I am teaching {self.subject_taught}"
        return message

student_1 = Student("John" , 30 , 5)
student_2 = Student("Jane" , 18 , 6)
# print(student_1.introduce())
# student_1.add_grade(18)
# student_1.add_grade(19)
# student_1.add_grade(17)
# print(student_1.introduce())
# print(f"The average grade is: {student_1.calculate_grade_average()}")

teacher_1 = Teacher("Mike" , 45 , "English")
# print(teacher_1.introduce())

class Police(Person):
    def __init__(self, name , age):
        super().__init__(name , age)
    
police_1 = Police("Jennifer" , 35)
class_1 = []
class_1.append(student_1)
class_1.append(student_2)
class_1.append(teacher_1)
class_1.append(police_1)


for person in class_1:
    print(person.introduce())
