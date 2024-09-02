# Create a list of dictionary(Data) representing students.
students = [
    {"name": "Alice", "age": 22, "grade": 85},
    {"name": "Bob", "age": 20, "grade": 90},
    {"name": "Charlie", "age": 23, "grade": 78},
    {"name": "David", "age": 21, "grade": 92},
    {"name": "Eve", "age": 22, "grade": 88}
]

# sort students by grade in decending order

sorted_by_grade = sorted(students, key=lambda student: student["grade"], reverse=True)

print("Students sorted by grade:")
for student in sorted_by_grade:
    print(student)
#Filter student with a grade of 80 and above

passing_students = filter(lambda student: student["grade"] >= 80, students)

print("\nStudents with passing grades (80 or above):")
for student in passing_students:
    print(student)
# Extarct the grades and calculate the average

grades = list(map(lambda student: student["grade"], students))
average_grade = sum(grades) / len(grades)

print(f"\nAverage grade of all students: {average_grade:.2f}")
# Extact student names

names = list(map(lambda student: student["name"], students))

print("\nList of student names:")
print(names)
# Sort their names in decending order










# sort () -> will modify the list in place
# sorted () -> will return a new list and not change the original

# print(sorted(people, key = lambda person: person['salary']))
# print(people.sort(key = lambda person: person['salary']))

# sort this list of people by age in ascending order without changing the list
# b. sort by salary in decending order without changing the list
# c. sort by their names in ascending order 