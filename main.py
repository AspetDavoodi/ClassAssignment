class Student:

    def __init__(self,Name, ID):
        self.Name = Name
        self.ID = ID
        self. courses = []


    def addcourse(self,CourseID):
        self.courses.append(CourseID)

    def addAssignment(self,Course, Name, Deadline):
        pass

    def grade(self,Course,Name,Deadline,grade):
        pass

    def getCourseGrade(self):
        pass

    def  getAssignmentGrade(self):
        pass




    def getgrade(self,Course, Assignment):


class Course:

    def __init__(self, Name):
        self.Name = Name
        self.Assignments = []

    def addAssignment(self, Assignment):
        pass

    pass

class Assignment:
    pass



def main():

    A = Student("Aspet", "A09180176")




main()
