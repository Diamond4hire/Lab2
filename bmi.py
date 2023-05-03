
def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmitest =weight/height/height

    print("Bmi = " + str(bmitest))

    if bmitest < 18.5:
     print("The User is Under Weight")
     return -1
    elif bmitest > 25.0:
     print("The User is Over Weight")
     return 1
    else:
     print("The User is Normal Weight")
     return 0

result = (calculate_bmi(weight=57, height=1.73))
print (result)