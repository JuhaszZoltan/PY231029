from module import *
import math

# minden esetben str-t ad vissza
nev:str = input('írd be a neved: ')

print(f'hello, {nev}!')

vezeteknev:str = "Juhasz"
keresztnev:str = "Zoltan"

print(vezeteknev + ' ' + keresztnev)
# "f" betűs prefix str előtt: "formated string"
print(f'{vezeteknev} {keresztnev}')

szam:float = 10/3
print(f'a szám kerekítve: {round(szam)}')

szo1:str = 'alma'
szo2:str = 'a'
szo3:str = 'fa'
szo4:str = 'alatt'

szoveg:str = f'{szo1} {szo2} {szo3} {szo4}'
print(szoveg)

egesz:int = 10
lebegopontos:float = 11.5
karakterlanc:str = 'szoveg'
logikai:bool = True # vagy False

# 10 / 3 -> sima osztás
# 10 // 3 -> egész osztás
# 10 % 3 -> maradékképzés
# +, -, *
# 10 ** 3 -> hatványozás (10^3)
# x += 10 increment operator van
# x++ <- ilyen nincs :(, helyette: x += 1

x:int = 10
gyok:float = 16 ** .5
print(gyok)

# compare operátorok (összehasonlító)
# !=, ==, >= <=, >, <

# logikai operátorok
# and, or, not

# "halmazművelet"
allatok:list[str] = ['cica', 'kutya', 'pingvin']
if 'hörcsög' in allatok: print(f'van höröcsög')
else: print('nincs hörcsög')

# str műveletek:
# 'kutya' + 'ház' -> 'kutyaház'
# 'cica' * 3 -> 'cicacicacica'