#Spojování více podmínek
cislo=int(input("Zadejte číslo v rozmezí mezi 10 a 20 nebo číslo mezi 30 a 40   "))
if ((cislo>=10)and(cislo<=20))or((cislo>=30)and(cislo<=40)):
    print("Zadal jste správné číslo")
else:
    print("Zadal jste špatné číslo. Zkuste to znovu")
input()
