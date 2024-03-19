#!/usr/bin/python3
def print_list_integer(my_list=[]):
 
   for i in my_list:
      print('{}'.format(i))

my_list = range(5)
print_list_integer(my_list)