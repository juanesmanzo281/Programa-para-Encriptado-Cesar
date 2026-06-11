alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

def encrypt(texto_original,espacio):
    """Devuelve un texto (string) encriptado en "codigo cesar", utilizando la lista [alfabeto] como iteracion para el encriptado. 
    Se ingresa un numero (Int) para realizar el encriptado"""
    encriptado = ""
    tamaño_alfabeto = len(alfabeto)
    for i in texto_original:
        if i in alfabeto:
            move = (alfabeto.index(i)+espacio) % tamaño_alfabeto
            encriptado += alfabeto[move]
        else:
            encriptado += i 
        
    return encriptado

def decrypt(encryptado,espacio):
    """Devuelve un texto (string) desentriptado en "codigo cesar", en base a otro texto (string ingresado). 
    Siempre recordar ingresar el numero de referencia que se usó en el encriptado para realizar el desencriptado"""
    desencriptado = ""
    tamaño_alfabeto = len(alfabeto)
    for i in encryptado:
        if i in alfabeto:
            move = (alfabeto.index(i)-espacio) % tamaño_alfabeto
            desencriptado += alfabeto[move]
        else:
            desencriptado += i

    return desencriptado