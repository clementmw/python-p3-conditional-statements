#!/usr/bin/env python3

def admin_login (username,password):
    if((username == "admin" or username == "ADMIN") and password == "12345"):
        return "Access granted"
    else:
        return "Access denied"

#access = admin_login("admin","1235")
#print(access)

#howistheweather
def hows_the_weather(temperature):
   responce = (
       "brisk" if temperature < 40 else
       "a little chilly" if temperature >= 40 and temperature <= 65 else
       "too dang hot" if temperature > 85 else
       "perfect"
   )
   return f"It's {responce} out there!"
    
today = hows_the_weather(45)
print(today)

#fizzbuzz
def fizzbuzz(num):
    if num % 3 == 0 and num % 5 == 0 :
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num 
    
print(fizzbuzz(5))

def calculator (operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print ("Invalid operation!")
        return None
        
    
print(calculator("+", 3, 5))

