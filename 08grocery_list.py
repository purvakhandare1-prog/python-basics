# Grocery List: Create a list of 5 items. Use a loop to print them out with a bullet point (e.g., * Apple).
list=["apple","mango","pineapple","banana","lemons"]
for names in list:
    print(f"*{names}")
print(f"* {names.capitalize()}")