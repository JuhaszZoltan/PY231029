# konvertálás: int('string')
erdemjegy:int = int(input('írd be a jegyet: '))

if erdemjegy == 1: print('elégtelen')
elif erdemjegy == 2: print('elégséges')
elif erdemjegy == 3: print('közepes')
elif erdemjegy == 4: print('jó')
elif erdemjegy == 5: print('jeles')
else: print('valami nem stimmel :(')

# ---------------------

a:int = int(input('3szög "a" oldala: '))
b:int = int(input('3szög "b" oldala: '))
c:int = int(input('3szög "c" oldala: '))

if a+b>c and b+c>a and a+c>b:
    print('van ilyen 3szög')
    kerulet:int = a+b+c
    s = kerulet/2
    terulet:float = (s*(s-a)*(s-b)*(s-c))**.5
    print(f'kerület: {kerulet}')
    print(f'terület: {round(terulet)}')
else:
    print('nem létezhet ilyen 3szög!')

x:int = int(input('x:= '))
y:int = int(input('y:= '))
if x == y:
    print(f'{x} és {y} értéke egyenlő')
else:
    if x > y:
        print(f'{x} nagyobb')
    else:
        print(f'{y} nagyobb')
