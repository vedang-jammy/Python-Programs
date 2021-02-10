# oop example program
class Students:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False

    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)


s1 = Students("JAck", 20, 90)
s2 = Students("Oggy", 21, 85)
s3 = Students("bob", 19, 70)

course = Course("science", 5)
course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
print(course.get_average_grade())
