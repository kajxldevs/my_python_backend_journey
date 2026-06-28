def CalculateBMI(Weight, Height, WeightUnit="kg", HeightUnit="cm"):
    
    
    if WeightUnit == "lbs":
        Weight = Weight*0.453  # 1 lb = 0.453 kg

    
    if HeightUnit == "cm":
        Height = Height/100 # cm to meters = division by 100
    elif HeightUnit == "feet":
        Height = Height*30.48/100  # 1 foot = 30.48 cm, then dividing by 100

    
    BMI = Weight/ Height**2  # weight / height squared

    
    if BMI < 18.5:
        Category = "Underweight"
    elif BMI < 24.9:
        Category = "Normal"
    elif BMI < 29.9:
        Category = "Overweight"
    else:
        Category = "Obese"

    return BMI,Category

