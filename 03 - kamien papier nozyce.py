from random import randint

score_computer = 0
score_user=0

while score_computer < 3:
    wybor_computer = randint(0,3)
    wybor_user=int(input("co wybierasz? 1.kamień, 2.popier, czy 3.nozyce? "))

    if wybor_computer==1:
        print("komputer wybrał: ", int(wybor_computer))
        if  wybor_user==2:
            score_user = score_user + 1
            print("dostałeś punkt")
        elif wybor_user==3:
            score_computer=score_computer+1
            print("komputer dostał punkt")
        else:
            print("remis")
        

    if wybor_computer==2:
        print("komputer wybrał: ", int(wybor_computer))
        if  wybor_user==3:
            score_user = score_user + 1
            print("dostałeś punkt")
        elif wybor_user==1:
            score_computer=score_computer+1
            print("komputer dostał punkt")
        else:
            print("remis")

    
    if wybor_computer==3:
        print("komputer wybrał: ", int(wybor_computer))
        if  wybor_user==1:
            score_user = score_user + 1
            print("dostałeś punkt")
        elif wybor_user==2:
            score_computer=score_computer+1
            print("komputer dostał punkt")
        else:
            print("remis")

    print ("aktualny wynik to komputer: ", str(score_computer), "gracz: ", str(score_user) )
