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
def sort_temperature(list):
    print("sort_temperature")
    sorted_list = sorted(list)
    return sorted_list
def calc_median_temperature(list):
 print("calc_median_temperature")
 sorted_list = sorted(list)
 n = len(sorted_list)
 if n % 2 == 0:
     mid1 = sorted_list[n // 2 - 1]
     mid2 = sorted_list[n // 2]
     median = (mid1 + mid2) / 2
 else:
     median = sorted_list[n // 2]
 return median

display_main_menu()
temp_list = get_user_input()
average = calc_average(temp_list)
min_val, max_val = find_min_max(temp_list)
sorted_list = sort_temperature(temp_list)
median = calc_median_temperature(temp_list)

print(temp_list)
print("The average temp is " + str(average))
print("The minimum temperature is:", min_val)
print("The maximum temperature is:", max_val)
print("The sorted Temperature in order is:", sorted_list)
print("The median Temperature is:", median)
