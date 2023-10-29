allatok:list[str] = ['kutya', 'cica', 'hörcsög', 'pingvin']
keresett:str = input('keresett állat: ')

# i:int = 0
# while i < len(allatok) and allatok[i] != keresett:
#     i += 1
# if i < len(allatok):
#     print(f'benne van, indexe: {i}')
# else:
#     print('nincs benne')

i:int = 0
while i < len(allatok):
    if keresett == allatok[i]:
        print(f'benne van, indexe: {i}')
        break
    i += 1
else: print('nincs benne')

# ciklushoz tartozó else ág akkor fut le,
# ha a ciklusban nem futott le soha break utasítás

for i in range(len(allatok)):
    if keresett == allatok[i]:
        print(f'megvan, indexe: {i}')
        break
else: print('nincs meg')