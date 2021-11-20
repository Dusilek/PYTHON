#Kalkulátor s výběrem početní operace
print("Kalkulátor s čtyřmi operacemi")
prvni_cislo=float(input("Zadejte první číslo   "))
druhe_cislo=float(input("Zadejte druhé číslo   "))
print("Co chcete s čísly udělat?   ")
print("1 - sečíst")
print("2 - odečíst")
print("3 - vynásobit")
print("4 - vydělit")
operace=int(input())
if operace==1:
    vysledek=prvni_cislo+druhe_cislo
    print(vysledek)
elif operace==2: #Pozor! Ne if ale ELIF!
    vysledek=prvni_cislo-druhe_cislo
    print(vysledek)
elif operace==3:
    vysledek=prvni_cislo*druhe_cislo
    print(vysledek)
elif operace==4:
    vysledek=prvni_cislo/druhe_cislo
    print(vysledek)
else: #A co když si nevybere nic?
    print("Nevybral jste si žádnou operaci a proto nebudu nic počítat")
input()
