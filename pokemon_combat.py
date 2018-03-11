

rival_elegido = input('Contra que pokemon quieres combatir? (Squirtle / Bulbasaur / Charmander)').upper()
print()
print('Combatiras usando un Pikachu')
print()

vida_pika = 100
vida_enemigo = 0

if rival_elegido == 'SQUIRTLE':
    vida_enemigo = 100
    ataque_enemigo = 8

elif rival_elegido == 'BULBASAUR':
    vida_enemigo = 80
    ataque_enemigo = 20

elif rival_elegido == 'CHARMANDER':
    vida_enemigo = 90
    ataque_enemigo = 12

while vida_enemigo > 0 and vida_pika > 0:

    ataque_elegido = input('Que ataque quieres usar contra {}? (Bola Voltio / Chispazo)'.format(rival_elegido)).upper()

    if ataque_elegido == 'BOLA VOLTIO':
        print()
        print('PIKACHU ha usado BOLA VOLTIO')
        print()
        vida_enemigo -= 10
        print('{} a perdido 10 puntos de vida'.format(rival_elegido))

    if ataque_elegido == 'CHISPAZO':
        print()
        print('PIKACHU ha usado CHISPAZO')
        print()
        vida_enemigo -= 15
        print('{} a perdido 15 puntos de vida'.format(rival_elegido))

    print()

    print('{} usó MORDIZCO'.format(rival_elegido))
    vida_pika -= ataque_enemigo
    print()
    print('PIKACHU perdió {} puntos de vida'.format(ataque_enemigo))
    print()
    print('Vida Pikachu {}'.format(vida_pika))
    print()
    print('vida {} {}'.format(rival_elegido, vida_enemigo))
    print()

if vida_enemigo <= 0:
    print("Enhorabuena, PIKACHU ha ganado")
    print()

if vida_pika <= 0:
    print('{} ha ganado el combate'.format(rival_elegido))

print("El combate ha terminado.")