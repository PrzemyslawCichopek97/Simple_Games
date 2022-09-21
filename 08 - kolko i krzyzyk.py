n = 3
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
            a[i][j] = "="

for row in a:
    print(' '.join([str(elem) for elem in row]))

z = input("grasz x czy o ?")

if z=="x":
    komp="o"
    print("grasz x a komputer gra o")
elif z=="o":
    komp="x"
    print("grasz o, a komputer gra x")
else:
    print("zla odpowiedz ") 

#zaczyna krzyżyk - więc w tym przypadku gracz
i=input("podaj współrzędną 'i' w której chcesz postawić x w formie (i,j)")
j=input("podaj współrzędną 'j' w której chcesz postawić x w formie (i,j)")
a[i][j]=1
for row in a:
    print(' '.join([str(elem) for elem in row]))






#gdyby gracz miał kółko i zaczynał komputer
