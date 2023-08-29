#pole neboli the list
food = ["pizza", "hamburger", "apple", "fish"]

food[1] = "sushi"

#užitečné funkce

#tato funkce přidá na konec pole daný string
food.append("ice cream")

food.remove("sushi")

#vymaže poslední element z pole
food.pop()

#přidá element na místo které mu přiřadím 
food.insert(2, "cake")

#seřadí pole v tomto případě podle abecedy
food.sort()

#vymaže všechna data z pole
#food.clear()

#pole vždy vypsat cyklem
for i in food:
    print(i)