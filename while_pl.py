pwd:str = '1234'
probalkozasok:int = 0
while input('írd be a jelszót: ') != pwd: pass
print('siker!')

# -------------------

proba:str = ''
while proba != pwd:
    proba = input('írd be a jelszót: ')
print('siker!')
# -------------------

while True:
    proba = input('írd be a jelszót: ')
    if proba == pwd: break
print('siker!')