
quieres_helado = input ('Te apetece un helado? (Si/No): ').upper()
esta_tu_tia = input ('Esta tu tia para comprartelo? (Si/No): ').upper()
hay_dinero = input ('Tienes dinero para compralo? (Si/No): ').upper()
esta_el_senor = input ('Esta el señor de los helados? (Si/No): ').upper()


apetece_helado = quieres_helado == 'SI'and esta_el_senor == 'SI'
tienes_como = hay_dinero == 'SI' or esta_tu_tia == 'SI'


if apetece_helado == True and tienes_como == True:
    print('Bien, pues dale, comete un helado')

else:
    print('Ash, que pena, sera para la proxima entonces...')
