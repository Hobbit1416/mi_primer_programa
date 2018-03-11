
print('Bienvenido a el programa de calculadora')
operacion = input('Que operación matemática desea realizar? (Suma/Resta/Multiplicacion/Division)').upper()

print()

print("Operacion a realizar {}".format(operacion))

primer_numero = int(input('Introduzca el primer numero: '))
segundo_numero = int(input('Introduzca el segundo numero: '))

print()
resultado = 0

if operacion == 'SUMA':
    resultado = primer_numero + segundo_numero
    print('Resultado = {}'.format(resultado))

elif operacion == 'RESTA':
    resultado = primer_numero - segundo_numero
    print('Resultado = {}'.format(resultado))

elif operacion == 'MULTIPLICACION':
    resultado = primer_numero * segundo_numero
    print('Resultado = {}'.format(resultado))

elif operacion == 'DIVISION':
    if segundo_numero == 0:
        print()
        print('ERROR... Imposible dividir entre 0, introduzca un valor valido')
    else:
        resultado = primer_numero / segundo_numero
        print('Resultado = {}'.format(resultado))