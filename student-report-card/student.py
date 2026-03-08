class Student:
    def __init__(self,name,roll_no,marks):
        self.name=name
        self.roll_no=roll_no
        self.marks=marks
        print(f"student name is {name}")
        

    def add_marks(self,added_marks):
        self.added_marks=added_marks
      
        self.marks+=self.added_marks
        print(f"your nmarks {self.added_marks}")

    def show_result(self):          # self.marks use karo andar!
     if self.marks >= 40:
        print("PASS")
     else:
        print("FAIL")
        
#test
stu = Student("Priya", 1, 0)
stu.add_marks(75)
stu.show_result()


    
      
    
        

    

    














