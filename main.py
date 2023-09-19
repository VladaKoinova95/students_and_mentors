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

    def _average_grade(self):
        average_grades = [sum(el)/len(el) for el in self.grades.values()]
        return sum(average_grades)/len(average_grades)

    def __str__(self):
        res = (
            f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {self._average_grade()}\n'
            f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\nЗавершенные курсы: {", ".join(self.finished_courses)}'
        )
        return res

    def __lt__(self, other):
        if not isinstance(other, Student):
            print("Объект не является студентом!")
            return
        return self._average_grade() < other._average_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self,name,surname):
        super().__init__(name,surname)
        self.grades = {}

    def _average_grade(self):
        average_grades = [sum(el)/len(el) for el in self.grades.values()]
        return sum(average_grades)/len(average_grades)

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекции: {self._average_grade()}'
        return res

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print("Объект не является лектором!")
            return
        return self._average_grade() < other._average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        res = f'Имя: {self.name}\nФамилия: {self.surname}'
        return res


student_1 = Student('Влада', 'Коинова', 'ж')
student_1.courses_in_progress += ['Python', 'GIT', 'Figma']

lecturer_1 = Lecturer('Сергей', 'Иванов')
lecturer_1.courses_attached += ['Python']

reviewer_1 = Reviewer('Полина', 'Кошкина')
reviewer_1.courses_attached += ['GIT']

student_1.rate_lecturer(lecturer_1, 'Python', 9)
reviewer_1.rate_hw(student_1, 'GIT', 10)