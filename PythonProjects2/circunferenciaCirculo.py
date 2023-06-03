#Realiza el calculo para saber la circunferencia de un circulo de diametro x
#El diámetro corresponde al doble del radio, es decir, d = 2 × r.

pi = 3.1415
diametro = int(input('Ingrese el valor del diametro del circulo en cm: '))

circunferencia = (diametro) * (pi)
print(f'La circunferencia del circulo de diametro {diametro}cm, es de: {round(circunferencia)}cm')

#Round sirve para redondear un numero