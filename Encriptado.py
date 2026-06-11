import funciones_y_alfabeto

print("BIENVENIDO AL ENCRIPTADOR/DESENCRIPTADOR DE PYTHON")

def encriptado_cesar():

    fin = False 

    while fin != True:
        
        while True:

            direction = input("Ingresa 'encode' para codificar, o 'decode' para desencriptar: ").lower().strip()

            if direction not in ["encode","decode"]:
                print(f"Lo siento, ''{direction}'' no esta dentro de las opciones")

            else:
                break

        text = input("Ingresa tu mensaje(solo letras): ").lower().strip()

        while True:          

            if direction == "encode":
                espacio = int(input("Ingresa el número de cifrado: "))
                print(f"Aqui esta esta tu texto codificado: {funciones_y_alfabeto.encrypt(text, espacio)}")
                break
                

            elif direction == "decode":
                espacio = int(input("Ingresa el número de descifrado: "))
                print(f"Aqui esta tu texto tu texto desencriptado: {funciones_y_alfabeto.decrypt(text,espacio)}")
                break

        while True:

            program = input("Digita 'si' si deseas seguir usando el programa, sino, digita 'no': ").lower().strip()

            if program == "si":
                print("Buena respuesta, sigamos trabajando")
                fin = False
                break

            elif program == "no":
                print("Entendido, vuelve pronto")
                fin = True
                break
                    
            else:
                print("Por favor solo ingrese 'si' o 'no'")


encriptado_cesar()
                