height=float(input("enter your height in cm:"))
weight=float(input("enter your weight in kg:"))
BMI=weight/(height/100)**2
if(BMI<=14.5):
    print("you are light weight")
elif(BMI<=24.9):
    print("your weight is healthy")
else:
    print("you are over weight")