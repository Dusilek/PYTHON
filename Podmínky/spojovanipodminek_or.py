#Spojování více podmínek
cislo=int(input("Zadejte číslo v rozmezí mezi 10 a 20 nebo číslo mezi 30 a 40   "))
if ((10<=cislo<=20)or(30<=cislo<=40)):
    print("Zadal jste správné číslo")
else:
    print("Zadal jste špatné číslo. Zkuste to znovu")
input()
