print("What is your name human?")
name =input()
print("How old are you (in years?")
age =int(input())
print("How tall are you (in meters)?")
height = float(input())
print("How much do you weight?")
weight =float(input())
bmi = weight/(height**2)
print(name,"you are",age,"years old and your BMI is",bmi)
print(f"{name} you are {age} years old and your BMI is {bmi}")
print("{} your are {} years old and your BMi is {}".format(name, age, bmi))