class Student:
   
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
    
    def rate_lecturer(self, lecturer , course, grade):
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
        return f'Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнbе задание: {avg_grade}\nКурсы в процессе изучения: {courses_in_progress}\nЗавершённые курсы: {finished_courses}'
        
    def _calculate_avg_grade(self):
        if not self.grades:
            return 0
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return round(sum(all_grades) / len(all_grades), 1)
        


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []
    
    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'
    




class Lecturer(Mentor):
    def __init__( self, name, surname):
        super().__init__( name, surname)
        self.grades = {}

    def __str__(self):
        avg_grade = self._calculate_avg_grade()
        return f'{super().__str__()}\nСредняя оценка за лекции: {avg_grade}'
    
    def _calculate_avg_grade(self):
        if not self.grades:
            return 0
        all_grades = [grade for grades in self.grades.values() for grade in grades]
        return round(sum(all_grades) / len(all_grades), 1)

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
           return 'Ошибка'


student = Student('Ruoy', 'Eman', 'your_gender')
lecturer = Lecturer("Some", "Buddy")
reviewer = Reviewer("Some", "Buddy")

student.courses_in_progress = ["Python", "Git"]
student.finished_courses = ["Основы программировиния нв Python"]
lecturer.courses_attached = ["Python"]
reviewer.courses_attached = ["Python"]


reviewer.rate_hw(student, "Python", 9)
reviewer.rate_hw(student, "Python", 10)
student.rate_lecturer(lecturer, "Python", 9)
student.rate_lecturer(lecturer, "Python", 10)

print("Проверяющий")
print(reviewer)
print("\nЛектор")
print(lecturer)
print("\nСтудент")
print(student)