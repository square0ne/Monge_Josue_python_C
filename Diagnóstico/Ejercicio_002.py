nombre = input('¿Cuál es tu nombre (s)? ')
primerApellido = input('¿Cuál es tu primer apellido? ')
segundoApellido = input('¿Cuál es tu segundo apellido? ')
nacimiento = input('¿En qué año naciste? ')
cumpleanos = input('¿En qué mes y día naciste? ').split(' ')
cumpleanos.reverse()
cumpleanos = '-'.join(cumpleanos)

print('A. Este es tu nombre completo en mayúsculas: %s'%(nombre + ' ' + primerApellido + ' ' + segundoApellido).upper())

print('B. Este es tu nombre completo en minúsculas: %s'%(nombre + ' ' + primerApellido + ' ' + segundoApellido).lower())

print('C. Esta es tu fecha de nacimiento: “%s”.'%(cumpleanos + '-' + nacimiento))

print('D. Esta es tu edad: %i'%(2023 - int(nacimiento)))

print('E. Tu nombre completo tiene %i vocales'%[(x in 'AEIOUaeiou') for x in (nombre.replace(' ', '') + primerApellido + segundoApellido)].count(True))

print('F. Tu nombre completo tiene %i letras'%len(nombre.replace(' ', '') + primerApellido + segundoApellido))

print('G. ¿Tu edad es un caracter de tipo número?: %s'%str(type((2023 - int(nacimiento))) == type(1)))

print('H. ¿Tu nombre completo es un caracter de tipo alfanumérico?: %s'%str(type((nombre + ' ' + primerApellido + ' ' + segundoApellido)) == type('a')))

print('I. Tu edad en diez años será: %i'%(2023 - int(nacimiento) + 10))

print('J. La media de tu edad actual y tu edad en 20 años es: %i'%(2023 - int(nacimiento) + 10))
                        