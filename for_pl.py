ures_lista:list[int] = []
#                   0   1   2  3  4   5
szamok:list[int] = [7, 10, 11, 6, 4, 21] # -> 6

for szam in szamok:
    print(f'- {szam}')

lista_hossza:int = len(szamok)
print(f'lista hossza: {lista_hossza}')

# range: egész számokat állít elő, [start, stop) "step"enként
# range(0, 10, 1) -> [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
# range(3, 11, 2) -> [ 3, 5, 7, 9 ]

# range(10) == range(0, 10, 1)
# range(2, 10) == range(2, 10, 1)

# lista indexeinek bejárása:
for i in range(len(szamok)):
    print(f'{szamok[i]}', end=' ')

print('\n')
print(szamok)