#Kalkulátor s kontrolou jmenovatele
prvni_cislo=float(input("Zadejte první číslo   "))
druhe_cislo=float(input("Zadejte druhé číslo   "))
if druhe_cislo==0:
    print("Ve jmenovateli je číslo 0 a nulou nesmíme dělit")
else:
    deleni=prvni_cislo/druhe_cislo
    print(deleni)
input()
