# multiplication Table: Ask for a number (e.g., 5) and use a for loop to print its multiplication table from 1 to 10.
user_number = int(input("Enter a number: "))

for i in range(1, 11):
    # This formats it as: "5 x 1 = 5"
    print(f"{user_number} x {i} = {user_number * i}")