def main():
    print (calculate_bmi(weight=57, height=1.73))


def calculate_bmi(height, weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    bmi =weight/height/height

    print("Bmi = " + str(bmi))

    if bmi < 18.5:
     print("The User is Under Weight")
     return -1
    elif bmi > 25.0:
     print("The User is Over Weight")
     return 1
    else:
     print("The User is Normal Weight")
     return 0

if __name__ == "__main__":
 main()