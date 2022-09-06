class student:
    def __init__(self,stu_id,stu_name):
        self.studentid=stu_id
        self.studentname=stu_name

    def details(self):
        return self.studentid + " " + self.studentname

stud = student("123","naveen")
sdetails = stud.details()

setattr(stud,"student_class","10")        #Add a new attribute student_class
print(getattr(stud,"student_class"))
delattr(stud,"studentname")                # remove the student_name attribute
print(hasattr(stud,"student_name"))
setattr(stud,"__studpt","IT")              #Add a new attribute “__studentdept” to Student class
print(hasattr(stud,"__studpt"))
print(getattr(stud,"__studpt"))
