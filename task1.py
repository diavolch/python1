''' Напишите программу, которая принимает на вход цифру, 
обозначающую день недели, и проверяет, 
является ли этот день выходным. '''

num = int(input('Введите число: '))
if num == 6 or num == 7:
    print('День является выходным')
elif num in range (1,6):
    print('День не является выходным')
else:
    print('Число не обозначает день недели')