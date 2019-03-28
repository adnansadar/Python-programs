name = (raw_input("Enter your name: "))
height = (input("Enter your height(in m): "))
weight = (input("Enter your weight(in kg): "))
bmi = weight/(height**2)
print(bmi)
if bmi > 25:
    print(name)
    print("is overweight")
else:
    print(name)
    print("is not overweight")
