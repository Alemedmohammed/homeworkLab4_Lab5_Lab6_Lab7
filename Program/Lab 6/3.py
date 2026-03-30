students = {}
for i in range(3):
    name = input(f"enter student name {i+1}: ")
    try:
        grade = float(input(f"enter grade for {name}: "))
    except ValueError:
        print("invalid grade")
        exit(1)
    students[name] = grade

print("students and their grades:")
for name, grade in students.items():
    print(name, ":", grade)

top_student = max(students, key=students.get)
print("top student:", top_student, "with grade:", students[top_student])



input("")