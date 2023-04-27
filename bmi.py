def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi =weight/height/height

    print("Bmi = " + str(bmi))

    if bmi < 18.5:
     print("The User is Under Weight")
    elif bmi > 25.0:
     print("The User is Over Weight")
    else:
     print("The User is Normal Weight")

calculate_bmi(weight=57, height=1.73)