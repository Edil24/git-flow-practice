class Student:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age


class Subject:
    def __init__(self, name, teacher_name):
        self._name = name
        self._teacher_name = teacher_name

    @property
    def name(self):
        return self._name

    @property
    def teacher_name(self):
        return self._teacher_name


class Diary:
    def __init__(self, student):
        self._student = student
        self._subjects = []

    def add_subject(self, subject):
        self._subjects.append(subject)

    @property
    def student(self):
        return self._student

    @property
    def subjects(self):
        return self._subjects


# Создание объектов и демонстрация их работы
student_alex = Student(name="Alex", age=16)
math_subject = Subject(name="Math", teacher_name="Mr. Johnson")
history_subject = Subject(name="History", teacher_name="Mrs. Smith")

alex_diary = Diary(student_alex)
alex_diary.add_subject(math_subject)
alex_diary.add_subject(history_subject)

print(alex_diary.student.name)  # Alex
print(alex_diary.subjects[0].name)  # Math
print(alex_diary.subjects[0].teacher_name)  # Mr. Johnson
