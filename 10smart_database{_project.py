
import random


student_list = []

# Loop chalate hain 40 baar
for i in range(1, 41):
    # Har student ke liye ek dictionary
    student = {
        "id": i,
        "name": f"Student {i}",
        "grade": random.choice(["A", "B", "C", "D"]) # Random grade select karega
    }
    # List mein add kar dete hain
    student_list.append(student)

# Check karne ke liye pehle 5 students print karte hain
for s in student_list[:40]:
    print(s)

print(f"\nTotal Students in list: {len(student_list)}")
