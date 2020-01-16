def printBMI(p_weight, p_height):
    bmi = p_weight / (p_height * p_height)
    print("bmi: %.4f"%(bmi))

    if bmi < 18:
        print("You are underweight.")
    elif bmi < 25:
        print("Your weight is ideal.")
    elif bmi < 30:
        print("You are overweight.")
    else:
        print("You are obese.")


for i in range(4):
    weight = input("Enter your weight (kg):")
    height = input("Enter your height (m):")

    try:
        weight = float(weight)
        height = float(height)
        printBMI(p_height=height, p_weight=weight)
    except ValueError:
        print("Please enter only numbers")


