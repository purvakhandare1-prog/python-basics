class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        print(f"the person name is{self.name} and age is {self.age}")
class Student(Person):
    def study(self,hours):
        self.hours=hours
        print(f"student  {self.name}studying for{self.hours}")


class Teacher(Person):
    def teach(self,subject):
        self.subject=subject
        print(f"teacher teach {self.subject}")

a=Person("purva",19)
stu=Student("amruta",22,)
stu.study(4)
t=Teacher("sanket",19)
t.teach("hindi")
