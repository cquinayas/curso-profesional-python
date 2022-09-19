def decorador(func):
    def envoltura():#wrapper
        print("Esto se añade a mi funcion original")
        func()
    return envoltura
@decorador #Syntantic sugar
def saludo():
    print("Hola")
#saludo = decorador(saludo)

saludo()

#Example
def upper_convert(func):
    def wrapper(texto):
        return func(texto).upper()
    return wrapper
@upper_convert
def message(nombre):
    return f'{nombre}, Did you get  a message'

print(message('Cesar'))

