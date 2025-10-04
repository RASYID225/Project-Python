class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)
        return f"Grade {grade} added."

    def get_average(self):
        if not self.grades:
            return "Average grade: 0.0"
        avg = sum(self.grades) / len(self.grades)
        # Format sesuai contoh (one decimal place)
        return f"Average grade: {avg:.1f}"

print("# Case 8 Output")
student = Student("Alice")
print(student.add_grade(90))   # Grade 90 added.
print(student.add_grade(80))   # Grade 80 added.
print(student.add_grade(70))   # Grade 70 added.
print(student.get_average())   # Average grade: 80.0