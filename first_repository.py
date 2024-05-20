"""
EX1:
a. Defineste o lista cu 3 elemente.
b. Este lista o structura de date ordonata? De ce da/nu?
c. Acceseaza al doilea element din lista si afiseaza-l.
d. Afiseaza lungimea listei.
"""
print("ex 1 - rezolvare")

produse = ['pahar', 'crema de maini', 'pix']
al_doilea_element = produse[1]
print(al_doilea_element)
print('lungimea listei este', len(produse))

"""
EX2:
Se da setul: my_set = {1, 2, 3, 4}.
a. Adauga nr 5 in set.
b. Adauga nr 6 in set.
c. Adauga nr 1 in set. Ce observi?
d. Sterge un element din set folosind metoda remove().
e. Sterge un element din set folosind metoda pop().
"""
print("ex 2 - rezolvare")
my_set = {1, 2, 3, 4}
my_set.add(5)
my_set.add(6)
my_set.add(1)
my_set.remove(5)
my_set.pop()

print(my_set)