students = [
    {"name": "Alice", "age": 22, "grade": 85},
    {"name": "Bob", "age": 20, "grade": 90},
    {"name": "Charlie", "age": 23, "grade": 78},
    {"name": "David", "age": 21, "grade": 92},
    {"name": "Eve", "age": 22, "grade": 88}
]
sorted_by_grade = sorted(students, key=lambda student: student["grade"], reverse=True)

print("Students sorted by grade:")
for student in sorted_by_grade:
    print(student)

passing_students = filter(lambda student: student["grade"] >= 80, students)

print("\nStudents with passing grades (80 or above):")
for student in passing_students:
    print(student)

grades = list(map(lambda student: student["grade"], students))
average_grade = sum(grades) / len(grades)

print(f"\nAverage grade of all students: {average_grade:.2f}")

names = list(map(lambda student: student["name"], students))

print("\nList of student names:")
print(names)











