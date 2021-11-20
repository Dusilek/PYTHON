#Odmocnina z čísla s úplným větvením
cislo=int(input("Zadejte číslo, ze kterého chcete spočítat odmocninu"))
if cislo>0:
    print("Zadali jste číslo větší než 0 a já ho tak mohu odmocnit")
    odmocnina=cislo**(1/2)#Náhrada za funkci z matematické knihovny
    print("Odmocnina z cisla",cislo,"je",odmocnina)
if cislo<0:
    print("Zadali jste číslo menší než 0 a to odmocňovat nemůžeme")
print("Děkujeme Vám za zadání")
input()
