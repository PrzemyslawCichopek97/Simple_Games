#losowanie liczb od 0 do 100 i potem odgadywanie liczb
#losuje liczbę od 0 do 100

from random import randint
liczba = randint(0,100)
guess = -1
ilosc_podejsc = 0

while guess!=liczba:

    guess = int(input("zgadnij liczbe: "))
    ilosc_podejsc+=1

    if guess == liczba:
        print("brawo, zgadłeś liczbę! Twoja liczba podejść to: " + str(ilosc_podejsc))
    elif guess > liczba:
        print("podana liczba jest zbyt duża ")
    else:
        print("podana liczba jest zbyt mała ")

 