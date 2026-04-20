def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    weight = float(input("Vazn (kg): "))
    height = float(input("Bo'y (m): "))
    bmi = calculate_bmi(weight, height)
    category = get_bmi_category(bmi)
    print(f"BMI: {bmi:.2f}")
    print(f"Kategoriya: {category}")

if __name__ == "__main__":
    main()
