#pole neboli the list
#food = ["pizza", "hamburger", "apple", "fish"]

#food[1] = "sushi"

#užitečné funkce

#tato funkce přidá na konec pole daný string
#food.append("ice cream")

#food.remove("sushi")

#vymaže poslední element z pole
#food.pop()

#přidá element na místo které mu přiřadím 
#food.insert(2, "cake")

#seřadí pole v tomto případě podle abecedy
#food.sort()

#vymaže všechna data z pole
#food.clear()

#pole vždy vypsat cyklem
#for i in food:
    #print(i,  end=" ")



#procvičování loopů
#phone_number = "123-3344-2311"
#for i in phone_number:
    #if i == "-":
        #continue
    #print(i, end=",")


#for i in range(1,12):
    #if i != 9:
        #pass
        #print(i)

#name = "heloo my name iisb dominik"

#name = name.replace("iisb", "is")
#name = name.replace("heloo", "Hello")
#name = name.__add__(".")
#print(name)

#meal = ["hamburger","pizza","chese"]
#drink = ["soda","pepsi","cocacola"]
#food = [drink, meal]

#meal = ["hamburger","pizza","chese"]
#for i in meal:
#    if i == "pizza":
#        continue
#    print(i)

#tuple = je to něco jako pole, ale nelz eměnitjeho elementy uvnitř a narozdíl od pole se používaji () tyto závorky

student = ("Dominik",17,"male")
#řekne kolik se těchto elementu v poli nází
print(student.count("Dominik"))
#kde se element nachazi
print(student.index("male"))

for i in student:
    print(i)

if "Dominik" in student:
    print("Dominik is here!")

#set => je to něco jako pole, ale je ohraničeno {} a je neindexované. Tzn, že když to pole vypíšu, 
# tak ne nebypíše odle pořadí, ale random a když je tam více stejných elementů, tak je vypíše a 
# pracuje s nimi jako s jedním

set = {"knife","spoon","fork","fork","spoon"}
dishes = {"bowl","plate"}
#set.add("napkin")
#set.remove("fork")
#set.clear()
#=> update je, že spojí sety dohromady
#set.update(dishes)
#dinner_table = set.union(dishes)
#for i in dinner_table:
#    print(i)

#auto = ["honda","ferrari","skoda"]
#moto = ["bagatata","lambarjambar"]
#auto_moto = [auto, moto]
#for i in auto_moto:
#    print(i)

#a = list(range(1,11))
#print(a)

#a = []
#or i in range(60):
 #   a += [0] 
#    print(a)

print("ahoj")