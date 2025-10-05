weight = float(input("Enter your weight in kg: "))
height = float(input("Enter you height in m: "))

a = weight
b = height

def bmi_calculate(a,b):
    bmi = (a/(b*b))
    print('Bmi is', bmi)

bmi_calculate(a,b)
