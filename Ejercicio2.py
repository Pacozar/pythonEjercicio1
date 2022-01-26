agenda = {}


def main():
    print("""Si quieres añadir un nuevo contacto escribe 1
Si quieres buscar un contacto escribe 2
Si quieres salir escribe 3""")
    ask = input()
    if ask == '1':
        add()
    elif ask == '2':
        search()
    elif ask == '3':
        print('Gracias')
    else:
        print('No has introducido una opcion valida')
        main()


def add():
    nombre = input('Nombre contacto: \n')
    while True:
        try:
            telefono = int(input('ingrese telefono de contacto: '))
            break
        except:
            print('El numero no es valido')
    if telefono > 0:
        agenda[nombre] = telefono
        print(agenda)
        main()
    else:
        add()


def search():
    nombre = input('Introduzca nombre de contacto: \n')
    booleano = False
    for i in agenda:
        if nombre in i:
            print(i, agenda[i])
            booleano = True

    if not booleano:
        print(nombre, 'no es un contacto de tu agenda')
    main()


main()
