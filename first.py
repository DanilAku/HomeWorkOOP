class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'
    
    def __str__(self):
        avg_grade = self._calculate_avg_grade()
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses) if self.finished_courses else "Нет завершённых курсов."
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашние задания: {avg_grade}\nКурсы в процессе изучения: {courses_in_progress}\nЗавершённые курсы: {finished_courses}'
    
    def _calculate_avg_grade(self):
        if not self.grades:
            return 0
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return round(sum(all_grades) / len(all_grades), 1)
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_avg_grade() == other._calculate_avg_grade()
    
    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_avg_grade() < other._calculate_avg_grade()
    
    def __le__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self._calculate_avg_grade() <= other._calculate_avg_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
    
    def __str__(self):
        avg_grade = self._calculate_avg_grade()
        return f'{super().__str__()}\nСредняя оценка за лекции: {avg_grade}'
    
    def _calculate_avg_grade(self):
        if not self.grades:
            return 0
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return round(sum(all_grades) / len(all_grades), 1)
    
    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_avg_grade() == other._calculate_avg_grade()
    
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_avg_grade() < other._calculate_avg_grade()
    
    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self._calculate_avg_grade() <= other._calculate_avg_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'


def calculate_avg_hw_grade(students, course_name):
    total_sum = 0
    total_count = 0
    for student in students:
        if course_name in student.grades:
            grades = student.grades[course_name]
            total_sum += sum(grades)
            total_count += len(grades)
    return round(total_sum / total_count, 1) if total_count > 0 else 0


def calculate_avg_lecture_grade(lecturers, course_name):
    total_sum = 0
    total_count = 0
    for lecturer in lecturers:
        if course_name in lecturer.grades:
            grades = lecturer.grades[course_name]
            total_sum += sum(grades)
            total_count += len(grades)
    return round(total_sum / total_count, 1) if total_count > 0 else 0


# Создание участников
student1 = Student('Алиса', 'Бекетова', 'female')
student2 = Student('Пётр', 'Фестрангов', 'male')

lecturer1 = Lecturer('Владимир', 'Длинноусов')
lecturer2 = Lecturer('Жоан', 'Маду')

reviewer = Reviewer('Франческо', 'Воскоплавов')

# Настройка курсов
student1.courses_in_progress = ['Python']
student2.courses_in_progress = ['Python']
lecturer1.courses_attached = ['Python']
lecturer2.courses_attached = ['Python']
reviewer.courses_attached = ['Python']

# Выставленные оценки
student1.rate_lecturer(lecturer1, 'Python', 9)
student1.rate_lecturer(lecturer1, 'Python', 8)
student2.rate_lecturer(lecturer2, 'Python', 10)
student2.rate_lecturer(lecturer2, 'Python', 9)

reviewer.rate_hw(student1, 'Python', 7)
reviewer.rate_hw(student1, 'Python', 8)
reviewer.rate_hw(student2, 'Python', 9)
reviewer.rate_hw(student2, 'Python', 10)

# Выводим информацию
print("Проверяющий")
print(reviewer)
print("\nЛектор 1")
print(lecturer1)
print("\nЛектор 2")
print(lecturer2)
print("\nСтудент 1")
print(student1)
print("\nСтудент 2")
print(student2)

# Считаем средние оценки
students_list = [student1, student2]
lecturers_list = [lecturer1, lecturer2]

print("\nСредняя оценка за домашние задания по Python:", 
      calculate_avg_hw_grade(students_list, 'Python'))
print("Средняя оценка за лекции по Python:", 
      calculate_avg_lecture_grade(lecturers_list, 'Python'))

# Сравнение студентов
print("\nСравнение студентов:")
print("student1 < student2:", student1 < student2)
print("student1 == student2:", student1 == student2)

# Сравнение лекторов
print("\nСравнение лекторов:")
print("lecturer1 > lecturer2:", lecturer1 > lecturer2)
print("lecturer1 == lecturer2:", lecturer1 == lecturer2)