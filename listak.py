ures = []
nem_ures = ['csiga', 32, 11.5, True]

homogen:list[int] = [10, 11, 12, 13, 14, 15]

# új elemet ad hozzá a lista végéhez
homogen.append(30)

# az <object>-et az <index>edik indexre szúrja be
homogen.insert(20, 2)

# rendezi az elemeket (a listán belül)
homogen.sort()

# megfordítja az elemek sorrendjét
homogen.reverse()

# "kivesz" egy elemet a listából (alapértelmezetten az utolsót)
elem:int = homogen.pop()

print('-----------')
print(homogen)
# tól-ig indexelés, (Zárt, NYílt)
print(homogen[1:3]) # -> 1, 2 indexű elem
print(homogen[:5]) # -> 0tól 4ig
print(homogen[1:]) # -> egyes indexű elemtől a végéig
print(homogen[-2]) # -> a lista végéről az első elem
print(homogen[3:-2]) # -> 3mas indexűtöl az utolsó előttiig
print('-----------')

print(homogen)

# ÉRTÉK típus
x:int = 10
y:int = x
x += 2

# REFERENCIA típus
t:list[int] = [2]
f:list[int] = t
f[0] += 10
print(t)
# helyette tehát REF type-oknál "másolni" kell
f = t.copy() # vagy másolás tétele...