class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @staticmethod
    def go_to_school():
        return "I'm going to school"

anna = Student("Anna", "Oxford")
print(anna.marks)
anna.marks.append(56)
anna.marks.append(99)
print(anna.marks)
print(anna.average())

rolf = Student("Rolf", "Harvard")
print(rolf.go_to_school())
print(Student.go_to_school())
