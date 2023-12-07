#!/usr/bin/env python3

def admin_login (username,password):
    if((username == "admin" or username == "ADMIN") and password == "12345"):
        return "Access granted"
    else:
        return "Access denied"

#access = admin_login("admin","1235")
#print(access)

def hows_the_weather(temperature):
    if temperature < 40:
        response = "brisk"
    elif temperature >= 40 and temperature <= 65:
        response = "a little chilly"
    elif temperature > 85:
        response = "too dang hot"
    else:
        response = "perfect"
  
    return (f"It's {response} out here")
    
today = hows_the_weather(45)
print(today)
