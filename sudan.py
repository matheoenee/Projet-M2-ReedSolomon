import numpy as np

# EXEMPLE 1.95 DU COURS SUR LES CODES
# RS[10,2,9] sur GF(11)
n = 10
k = 2
d = 9

x = [pow(2,i) % 11 for i in range(n)] # on prends 2 car élément primitif modulo 11
r = [7,6,5,3,8,7,9,0,2,5] # mot reçu
print("x = ",x)
print("r = ",r)

def Sudan(r,tau,l):
    
    deg_Q = [n - tau - 1 - j*(k-1) for j in range(l+1)]
    print("deg_Q = ",deg_Q)

    A = [] # matrice des coefficients
    B = [0 for i in range(n)] # matrice des termes constants

    # on définit les n équations
    for i in range(n):
        print(f"[{i}]")
        E = [] # coefficients de l'équation
        for j in range(len(deg_Q)):
            print(f"[+] Q{j} , pow(r) = {j} et pow(x) max = {deg_Q[j]}")
            deg = 0
            while deg <= deg_Q[j]:
                coeff = (pow(r[i],j)*pow(x[i],deg))% 11
                E.append(coeff)
                deg += 1
        A.append(E)
    print("A = ",A)
    print("B = ",B)

    # AX = B où X représente les coefficients des polynômes (a0,a1,...,a4,b0,...,b3,d0,...,d2) dans l'exemple sur GF(11) du cours
    # Comment retrouver X ? Méthode du pivot de Gauss? Que se passe-t-il si plus d'inconnues que d'équations?

Sudan(r,5,2)


