'''Напишите программу для проверки истинности утверждения 
¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.'''

x = bool(input('Введите x: '))
y = bool(input('Введите y: '))
z = bool(input('Введите z: '))

left = not (x or y or z)
right = (not x) and (not y) and (not z)
if left == right:
    print(True)
else:
    print(False)