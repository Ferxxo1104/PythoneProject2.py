# EJERCICIO 1
#pedir 2 numeros y decir si uno es multiplo del otro

num1 = int(input('Ingrese el primer número: '))
num2 = int(input('Ingrese el segundo número: '))

if num1 % num2 == 0:
    print(f'El número {num1} es multiplo de {num2} ')
elif num2 % num1 == 0:
    print(f'El número {num2} es multiplo de {num1} ')
else:
    print('los numero no son multiplos entre si')

