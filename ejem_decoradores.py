import random

def piedra_papel_tijera(func):
    def wrapper(*kargs,**kwargs):
        list_jugadas = ["piedra", "papel", "tijera"]
        jugada = random.choice(list_jugadas)
        print(f"La PC muestra {jugada}")
        func(*kargs,**kwargs)
        if jugada =="piedra"and mano =="papel"\
            or jugada =="papel"and mano =="tijera"\
            or jugada == "tijera" and mano == "piedra":
            print("Ganaste")
        elif jugada == mano:
            print("Empate")
        else:
            print("Perdiste")
    return wrapper

mano= "papel"
@piedra_papel_tijera
def mi_turno(mano):
    print(f"Yo muestro {mano}")   

if __name__ == "__main__":
    mi_turno(mano)    
