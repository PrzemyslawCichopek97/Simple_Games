#1. losujemy 5 liczb 0-100 i sprawdzamy która z nich jest najmniejsza

from random import randint
lista_list=[]
liczba=0

for liczba in range(0,5):
    los = randint(0,100)
    lista_list.append(los)
print("liczby: ",lista_list)

najmniejsza=lista_list[1]
najwieksza=lista_list[1]

for liczba in lista_list:
    if najmniejsza>liczba:
        najmniejsza=liczba
    if najwieksza<liczba:
        najwieksza=liczba
print("najwieksza liczba to ",najwieksza,"najmniejsza liczba to ", najmniejsza)




