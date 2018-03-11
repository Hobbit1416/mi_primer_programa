print()

print('El usuario debera adivinar un numero entre el 1 al 50')

print()
numero_a_adivinar = input('Introduce el numero que debera adivinar el usuario: ')
print()


print('Que el usuario no vea el numero, no queremos que gane facilmente')
print()

numero_usuario = input('Adivina el numero: ')

print()

if numero_a_adivinar != numero_usuario:
    while numero_a_adivinar != numero_usuario:
        numero_usuario = input('Ese no es, intenta de nuevo: ')

print()

print('Bien, ganaste, has vencido al sistema')
