
def calculateBMI ( weight,feet,inches):
    metricWeight = weight * 0.45
    totalInches = (feet * 12) + inches
    metricHeight = totalInches * 0.025
    heightSquared = metricHeight ** 2
    return round(metricWeight/heightSquared,1)

def outputBMICategory(bmi):
    if bmi < 18.5:
        category = "Underweight"
    if bmi >= 18.5 and bmi <= 24.9:
        category = "Normal weight"
    if bmi >= 25 and bmi <= 29.9:
        category = "Overweight"
    if bmi >= 30:
        category = "Obese"
    print("Category:", category)
    return category




