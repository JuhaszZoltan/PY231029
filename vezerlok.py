# elagazas
# if <condition>: <programrész, ami akkor fut le, ha a condition True

# if <condition>: -||-
# else: <ami akkor fut le, ha a condition False

# if <condition 01>:
#   prg 01
# elif <condition 02>:
#   prg 02
# else:
#   prg 03

# pythonban a ternary: 
# [on_true] if [expression] else [on_false] 
#pl:
x:int = 11
print('az x az 10' if x == 10 else 'az x nem 10')
szuletett:int = 2004
elmult18:str = 'igen' if 2023-szuletett>=18 else 'nem'
# ez a 'rendes' programozási nyelveken így néz ki:
# <expression> ? <on true> : <on false>

# ciklusok

# for, while

# for <variable> in <collection>:
#   a <variable> felveszi rendre a <collection> minden elemének értékét

# while <condition>:
#   ismétli addig, amíg a <condition> True