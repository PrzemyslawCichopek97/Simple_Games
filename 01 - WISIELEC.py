#Tworzymy grę w wisielca
#ilość żyć
no_of_tries = 5

#słowo które chcemy odgadnąć
word = "kamil"

#tworzymy listę składającą się z liter które podał użytkownik
used_letters=[]

#słowa które użytkownik ma odgadnąć
user_word = []

#definiuje fukcje 
def find_indexes(word.letter):
    indexes = []

    

    return indexes


#Dodajemy podkreślniki jako brakujące litery
for letter in word:
    user_word.append("_")



#while true - pętla która wykonuje się w nieskończoność
while True:
    letter = input("podaj litere: ")
    used_letters.append(letter)

    #pokaż która w wyrazie jest litera którą podałeś (numeracja od zera)
    print(word.index(letter))

    print("użyte litery: ", used_letters)

