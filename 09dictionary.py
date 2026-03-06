# Dictionary Practice: Create a student_grades dictionary. Write a script that asks the user for a name, then tells them that student's grade.
student_grades=[
   { "name":"amruta bedre",
    "grade":"A",},
   { "name":"plasi jagtap",
    "grade":"b"}]


user_name=(input("enter your name:").lower())
for student in student_grades:
    if user_name==student["name"]: 
      print(student["grade"])



     


