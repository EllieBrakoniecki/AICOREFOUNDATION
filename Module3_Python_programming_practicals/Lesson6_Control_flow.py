#%%
# BMI checker

def bmi_checker(weight,height):

    bmi = weight / height ** 2

    if bmi < 18.5:
        print(f"Your BMI is {bmi}. You're in the underweight range")
    elif 18.5 <= bmi < 25:
        print(f"Your BMI is {bmi}. You're in the healthy weight range")
    elif 25 <= bmi < 30:
        print(f"Your BMI is {bmi}. You're in the overweight range.")
    elif 30 <= bmi < 40:
        print(f"Your BMI is {bmi}. You're in the obese range")
    else:
        print('BMI out of range')

a = float(input('Enter your weight in kg'))
b = float(input('Enter your height in m'))

bmi_checker(a,b)
print(bmi_checker(85,1.83))
print(bmi_checker(95.9,1.71))


# %%
# Flight Safety Checker

def flight_safety_checker(altitude, airspeed):
    if (altitude < 100 or altitude > 50000) or (airspeed <= 60 or airspeed >= 500):
        print("unsafe flying")
        return
    print("safe flying")

flight_safety_checker(25000,300)
flight_safety_checker(50001,250)
flight_safety_checker(90,125)
flight_safety_checker(500,45)
flight_safety_checker(1000,600)
flight_safety_checker(65000,700)


# %%
