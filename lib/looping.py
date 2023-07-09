#!/usr/bin/env python3

def happy_new_year():
    item = 10

    while item >= 1 :
        print(item) 
    item -= 1

print("Happy New Year!")

def square_integers(int_list):
    for item in int_list:
       result = item*2
       print(result)
    # code goes here!
    pass

def fizzbuzz():
  item = 100
  while item>0:
    print(item)
    if ((item%3 ==0) and (item%5 ==0)):
      print("FizzBuzz")
    elif item%3 == 0:
      print("Fizz")
    elif item%5 == 0:
      print("Buzz")
    item -= 1 
      

    # code goes here!
    pass
