print( "Hello world!" )
first_name = "Dominik"
last_name = "Moszis"
full_name = first_name +" "+last_name
print("Jmenuji se "+full_name)
x = "2"
print("10 = 5 * "+x)
#tento kód pod tím vypisuje datový typ proměnné, což je vtomto případě STRING
print(type(first_name))

#integer se píše bez uvozovek
age = 17
age += 1
print("My age is: "+str(age))
print(type(age))

#desetinná čísla neboli float se píšou bez uvozovek a s tečkou mezi
height = 185.2
print("Moje výška je: "+str(height)+" cm")
print(type(height))

#boolean je datatype který umí je true a false
#hodí se u IF, ELSE atd.
human = False
print("Are you a human: "+str(human))
print(type(human))

#muliple assigment
name, age, attractive = "Dominik", 17, True
print (" ")
print(name)
print(age)
print(attractive)

spongebob = patrick = sue = 30

print(patrick)
print(spongebob)
print(sue)

name, first_surname, age = "Dominik", "Mojzis", 17
print("Dobrý den, jmenuji se "+name+" "+first_surname+" a je mi "+str(age)+" let.")
print(type(age))

#string methods
name = "Dominik"

#tato metoda stringu vypíše počet znaků ve stringu
print(len(name))

#tato metoda stringu vypíše kde se nachází daný znak v tomto případě i
#vypíše to v jakém pořadí je
print(name.find("i"))

#první písmen velké
print(name.capitalize())

#vše velké
print(name.upper())

#vše malé
print(name.lower())

#zjistí jestli ve stringu jsou písmena => false, nebo čísla => true
print(name.isdigit())

#jestli je string pouze z abecedy (mezery se počítají také!!)
print(name.isalpha())

#zjistí kolik znaků, na teré se zeptám je ve stringu
print(name.count("i"))

#vymění v tomto případě i za jiný string v tomto případě a
print(name.replace("i","a"))

#vypíše to tolikrát kolikrát to vynásobím
print(name*10)


#input
#name = input("What is your name: ")
#age = input("How old are you: ")
#age = int(age) + 1
#print("Hello "+name+"!")
#print("You are "+str(age)+" years old.")

import math
import time

x = math.pi
print(round(x))

#zaokrounhlení nahoru
print(math.ceil(x))

#zaokrounhlení dolu
print(math.floor(x))

#absolutní hodnota
print(abs(x))

#dá dané číslo na druhou, nebo na kolikátou napíšu jako druhé číslo za proměnnou
print(pow(x, 2))

#nějaké číslo na druhou se rovná proměnná a vypíše to to číslo ve floatu
print(math.sqrt(x))

#minimum a maximum z pole či více proměnných
x = (1, 3, 2)
print(max(x))
y = 1
c = 3
z = 2
print(min(y, c, z))

name = "Dominik Mojzis"
firsr_name = name[:7]
second_name = name[8:]
print(firsr_name)
print(second_name)
funky_name = name[::2]
print(funky_name)
reversed_name = name[::-1]
print(reversed_name)

website = "https://google.com"
website1 = "https://wikipedia.com"
slice = slice(8,-4)
print(website[slice])
print(website1[slice])

#age = input("What is your age: ")
#age = int(age)

#if (age == 100):
#    print ("You are a centenarian.")
#elif (age >= 18):
#    print("You are an adult.")
#else:
#    print("You are a child.")

#temp = input("What is the tempreture outside: ")
#temp = int(temp)

#if temp >= 0 and temp <= 30:
#    print("The tempreture is good today.")
#    print("Go outside!")
#elif temp < 0 or temp > 30:
#    print("The tempreture is bad today.")
#    print("Stay inside.")

#not je negace jako v php
#temp = input("Jaké je to teplo venku: ")
#temp = int(temp)

#if not(temp >= 0 and temp <= 30):
#    print("Venku je ošklivě.")
#elif not(temp < 0 or temp > 30):
#    print("Dneska je venku hezké počasí.")


#nekonečný cyklus 
#while 1==1:
#    print("Help! I'm stuck in a loop.")

#name = None
#while not name:
    #name = input("Enter your name: ")

#print("Hello "+name+"!")

#for i in range(10+1):
    #print(i)

#for i in "Dominik":
    #print(i)

#import time

#for seconds in range(10,0,-1):
    #print(seconds)
    #time.sleep(1)

#print("Happy new year!")

#row = int(input("How namy rows: "))
#column = int(input("How namy columns: "))
#symbol = input("What type of symbol: ")

#for i in range(row):
    #for j in range(column):
        #print(symbol, end="")
    #print()


#break
#while True:
    #name = input("What is your name: ")
    #if name != "":
        #break

#continue
phone_number = "123-456-7890"
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")