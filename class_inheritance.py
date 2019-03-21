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

    @classmethod
    def friend(cls, origin, friend_name, *args):
        return cls(friend_name, origin.school, *args)

anna = Student("Anna", "Oxford")
rolf = Student("Rolf", "Harvard")

print(anna.go_to_school())
print(rolf.go_to_school())
print(Student.go_to_school())


###
class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        super().__init__(name, school)
        self.salary = salary

rolf = WorkingStudent("Rolf", "Harvard", 20.00)
sue = WorkingStudent.friend(rolf, "Sue", 15.00)
print(sue.salary)  # This works!
