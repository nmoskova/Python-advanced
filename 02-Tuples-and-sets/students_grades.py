number_students = int(input())
students_grades = {}

for _ in range(number_students):
    name, grade_string = input().split()
    grade = float(grade_string)

    if name not in students_grades:
        students_grades[name] = []
    students_grades[name].append(grade)

for student, grades in students_grades.items():
    grades_string = [str(f'{x:.2f}') for x in grades]
    avg_grade = sum(grades) / len(grades)
    print(f"{student} -> {' '.join(grades_string)} (avg: {avg_grade:.2f})")