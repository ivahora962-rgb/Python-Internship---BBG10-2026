height_cm = "175"
weight_kg = "68.5"

height_cm = int(height_cm) / 100
weight_kg = float(weight_kg)
bmi = weight_kg / (height_cm * height_cm)
print("BMI:",bmi)