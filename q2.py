#Student Marks Dictionary
students = {
    "Rahul": 75,
    "Amit": 45,
    "Riya": 85,
    "Priya": 35,
    "Rohan": 60
}

for name, marks in students.items():
    print(name, marks)

print("Students scoring 50 or above:")

for name, marks in students.items():
    if marks >= 50:
        print(name)

print("Highest mark:", max(students.values()))