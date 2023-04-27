print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
def display_main_menu():
 print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
def get_user_input():
  print("get_user_input")
  values = input("Enter a list of strings separated by commas: ")
  temperatures = values.split(",")
  temp_list = [float(x) for x in temperatures]
  return temp_list
def calc_average(list):
 print("calc_average")
 sum = 0
 count = 0
 for num in list:
     sum += num
     count += 1
 if count == 0:
     return 0
 else:
     return sum / count
def find_min_max(list):
   print("find_min_max")
   if not list:
       return None, None
   min_val = list[0]
   max_val = list[0]
   for num in list:
       if num < min_val:
           min_val = num
       if num > max_val:
           max_val = num
   return min_val, max_val
def sort_temperature():
    print("sort_temperature")

def calc_median_temperature():
 print("calc_median_temperature")


display_main_menu()
temp_list = get_user_input()
average = calc_average(temp_list)
min_val, max_val = find_min_max(temp_list)


print(temp_list)
print("The average temp is " + str(average))
print("The minimum temperature is:", min_val)
print("The maximum temperature is:", max_val)

