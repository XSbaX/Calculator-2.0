from math import *

liste_outil = ['Trouver la forme canonique: 1', 'Trouver le tableau de variation: 2']


print("Bonjour, je suis Calculator 2.0")
print("Veuillez sélectionner un outil: ")
print(liste_outil)

choice_variable = int(input("Quelle est votre choix: "))

if choice_variable == 1:
    a = 0
    b = 0
    c = 0

    delta = 0
    alpha = 0
    beta = 0

    signe_b = 0
    signe_c = 0
    signe_alpha = 0
    signe_beta = 0

    x0 = 0
    x1 = 0
    x2 = 0

    print("Merci pour ton choix")
    print("Pour trouver la forme canonique de ton expression du 2nd degrès")
    print("Il me faut tes différentes valeurs")

    a = float(input("Quelle est la valeur de 'a': "))
    b = float(input("Quelle est la valeur de 'b': "))
    c = float(input("Quelle est la valeur de 'c': "))


    if b >= 0:
        signe_b = ("+")
    else:
        signe_b = ("")
    
    if c >= 0:
        signe_c = ("+")
    else:
        signe_c = ("")



    print("Ici, pour '", a, ("x^2"), signe_b, b, ("x"), signe_c, c)

    delta = b**2 - 4 * a * c
    alpha = -1*b / 2*a
    beta = delta / 4*a

    if alpha >= 0:
        signe_alpha = ("+")
    else:
        signe_alpha = ("")

    if beta >= 0:
        signe_beta = ("+")
    else:
        signe_beta = ("")

    

    print("Alors on a:", a, "(x", signe_alpha, alpha, ")^2", signe_beta, beta)


    if delta < 0:
        print("Il y'a 0 solutions")
        print("delta =", delta)

    if delta == 0:
        print("Il y'a 1 seule solution")
        print("delta =", delta)

        x0 = -b / 2*a

        

    if delta > 0:
        print("Il y'a 2 solutions")
        print("delta =", delta)

        x1 = (-1*b - sqrt(delta)) / (2*a)
        x2 = (-1*b + sqrt(delta)) / (2*a)

        print("x1 =", x1)
        print("x2 =", x2)




elif choice_variable == 2:
    print("Merci pour ton choix")

