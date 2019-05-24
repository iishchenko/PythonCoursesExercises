class Student:
     def __init__(self):
         self.studentName = ""
         self.GPA = 0.0
         self.creditHours = 0
         self.enrolled = True
         self.classes = []

newStudent = Student() 

newStudent.studentName = "George P. Burdell"

print(newStudent.studentName)

newStudent.enrolled = True

newStudent.classes = ["CS1301", "PHYS3001", "ISYE3029"]
