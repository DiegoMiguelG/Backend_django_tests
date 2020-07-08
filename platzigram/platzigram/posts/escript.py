from models import User        

if __name__ == "__main__":
    correo = input("Introduzca el correo electronico: ")
    contraseña = input('Introduzca la contraseña: ')
    nombre = input('Introduzca el nombre: ')
    apellido = input('Introduzaca el apellido: ')

    diego = User.obects.create(
            email = correo,
            password = contraseña,
            first_name = nombre,
            last_name = apellido
            )

