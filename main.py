class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    grades = {}


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


student_1 = Student('Влада', 'Коинова', 'ж')
student_1.courses_in_progress += ['Python', 'GIT', 'Figma']

lecturer_1 = Lecturer('Сергей', 'Иванов')
lecturer_1.courses_attached += ['Python']

reviewer_1 = Reviewer('Полина', 'Кошкина')
reviewer_1.courses_attached += ['GIT']

student_1.rate_lecturer(lecturer_1, 'Python', 9)

reviewer_1.rate_hw(student_1, 'GIT', 10)

print(lecturer_1.grades)
print(student_1.grades)



