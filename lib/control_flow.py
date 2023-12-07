#!/usr/bin/env python3

def admin_login (username,password):
    if((username == "admin" or username == "ADMIN") and password == "12345"):
        return "Access granted"
    else:
        return "Access denied"

#access = admin_login("admin","1235")
#print(access)

def hows_the_weather(temperature):
   responce = (
       "brisk" if temperature < 40 else
       "a little chilly" if temperature >= 40 and temperature <= 65 else
       "too dang hot" if temperature > 85 else
       "perfect"
   )
   return f"It's {responce} out here!"
    
today = hows_the_weather(45)
print(today)



