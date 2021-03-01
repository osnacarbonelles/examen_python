# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 13:00:57 2021

@author: Osnaider Carbonell
"""

"""
1. Una fruteria ofrece las manzanas con descuento según la siguiente tabla
De 0 – 2 kilos se aplica un 0% de descuento
De 2 – 5 kilos se aplica un 10% de descuento
De 5 – 10 kilos se aplica un 15% de descuento
De 10 en adelante se aplica un 20% de descuento.
"""
kilos_manzanas = float(input('Digite los kilos de manzanas": '))
precio_manzanas = float(input('Digite el precio del kilo de manzanas: $'))
total = kilos_manzanas * precio_manzanas
if kilos_manzanas < 2:
    descuento = 0
elif kilos_manzanas >= 2 and kilos_manzanas < 5:
    descuento = total * 0.10
    print('Se aplico un 10% de descuento')
elif kilos_manzanas >= 5 and kilos_manzanas < 10:
    descuento = total * 0.15
    print('Se aplico un 15% de descuento')
else:
    descuento = total * 0.20
    print('Se aplico un 20% de descuento')
valor_total = total - descuento
print(f'El total a pagar por {kilos_manzanas} ')
print(f'kilos de manzana es: ${valor_total:,}')


"""
2. Hacer algoritmo que de el valor final por la compra de abanicos. El
descuento lo hace basado a la clave, si la clave es 010 el descuento
es del 20% y si la clave es 020 el descuento es del 40%, si ela clave
es 030 el descuento es 55% y si es 040 el 75%.
"""
precio_abanico = float(input('Digite el precio del abanico: $'))
clave = input('Digite la clave: ')
if clave == '010':
    descuento = precio_abanico * 0.20
    valor_total = precio_abanico - descuento
    print('Se aplico un 20% de descuento')
    print(f'El precio del abanico con descuento es: ${valor_total:,}')
elif clave == '020':
    descuento = precio_abanico * 0.40
    valor_total = precio_abanico - descuento
    print('Se aplico un 40% de descuento')
    print(f'El precio del abanico con descuento es: ${valor_total:,}')
elif clave == '030':
    descuento = precio_abanico * 0.55
    valor_total = precio_abanico - descuento
    print('Se aplico un 55% de descuento')
    print(f'El precio del abanico con descuento es: ${valor_total:,}')
elif clave == '040':
    descuento = precio_abanico * 0.75
    valor_total = precio_abanico - descuento
    print('Se aplico un 75% de descuento')
    print(f'El precio del abanico con descuento es: ${valor_total:,}')
else:
    print('¡Digite una clave correcta!')


"""
3. Un proveedor de estéreos ofrece un descuento del 20% sobre el
precio sin IVA, de algún aparato si este cuesta $4000 o más.
Además, independientemente de esto, ofrece un 10% de descuento
si la marca es NOSY. Determinar cuanto pagará, con IVA incluido, un
cliente cualquiera por la compra de su aparato. IVA es del 30%.
"""
precio = float(input('Digite el precio del aparato: $'))
marca = input('Digite la marca del aparato: ')
if marca == 'NOSY' and precio >= 4000:
    descuento = precio * 0.30
elif precio >= 4000:
    descuento = precio * 0.20
total = precio - descuento
iva = (total * 0.30) / 100
valor_total = total + iva
print(f'El total a pagar es: ${precio:,}')
print(f'El descuento aplicado es: $-{descuento:,}')
print(f'El total a pagar ya con IVA incluido es: ${valor_total:,}')


"""
4. El gobierno Colombiano desea reforestar un bosque que mide un
determinado número de hectáreas. Si la superficie del terreno excede
a 5 hectáreas se sembrarán 80% Pino, 15% Oyamel y 5% Cedro. Si
es menor o igual a 5 hectáreas se sembrarán 45% Pino, 25% Oyamel
y 30% Cedro. Que cantidad de hectáreas le corresponde sembrar al
Gobierno de Pino, Oyamel y Cedro.
"""
numero_hectareas = int(input('Digite el numero de Hectáreas: '))
metros_cuadrados = numero_hectareas * 10000  # 1 Hectárea es igual a 10mil m^2
if numero_hectareas > 5:
    pino = metros_cuadrados * 0.80
    oyamel = metros_cuadrados * 0.15
    cedro = metros_cuadrados * 0.05
else:
    pino = metros_cuadrados * 0.45
    oyamel = metros_cuadrados * 0.25
    cedro = metros_cuadrados * 0.30
print('El numero de Pinos que se pueden sembrar en ')
print(f'{numero_hectareas} Hectáreas es: {pino:,}')
print('El numero de Oyamel que se pueden sembrar en ')
print(f'{numero_hectareas} Hectáreas es: {oyamel:,}')
print('El numero de Cedros que se pueden sembrar en ')
print(f'{numero_hectareas} Hectáreas es: {cedro:,}')


"""
5. Haga una función que lea 3 números diferentes e imprima el mayor
de los 3.
"""
numero1 = int(input('Digite un numero: '))
numero2 = int(input('Digite otro numero: '))
numero3 = int(input('Digite otro numero: '))
if (numero1 > numero2) and (numero1 > numero3):
    print(f'El numero mayor es: {numero1}')
elif (numero2 > numero1) and (numero2 > numero3):
    print(f'El numero mayor es: {numero2}')
else:
    print(f'El numero mayor es: {numero3}')
