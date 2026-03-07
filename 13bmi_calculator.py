def get_input(height, weight):
    return height, weight

height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kg: "))

result = get_input(height, weight)
print(result)

def calculate_BMI(weight, height):
    return weight / (height * height)

BMI = calculate_BMI(weight, height)

print(f"{BMI:.2f}")


def get_category(BMI):
    if BMI < 18.5:
        return "Underweight 😟"   
    elif 18.5 <= BMI <= 24.9:
        return "Normal ✅"
    elif 25 <= BMI <= 29.9:
        return "Overweight ⚠️"
    else:
        return "Obese 🚨"
    
category=get_category(BMI)
print(category)

def main():  
    # Function kaam karta hai, answer return karta hai, variable mein save ho jaata hai! ✅ sabhi fun ko ek variable me store karaya hain

    height, weight  = get_input()     
    bmi             = calculate_BMI(weight, height)  
    category        = get_category(bmi)
    print(height,weight)
    print(f"Your BMI  : {BMI:.2f}")
    print(f"Category  : {category}")
    print("this is your calculated bmi!")

    main()