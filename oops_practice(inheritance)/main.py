class Student:
  def __init__(self,name):
    self.name=name
    print(f"the name of student{self.name}")

  def check_marks(self,points):
   self.points=points
   print(f"the points of student are {self.points}")  # ✅)

  def grade(self):
  
   if self.points >= 40:
        print(f"✅ Pass! Marks: {self.points}")
   else:
        print(f"❌ Fail! Marks: {self.points}")

if __name__ == "__main__":  
 a=Student("amruta")
 a.check_marks(48)
 a.grade()
