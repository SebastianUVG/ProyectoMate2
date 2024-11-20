import numpy as np
import random
#---------Generar primos---------
import random

def criba(n):
    
    not_primes = set()
    primes = []
    for i in range(2, n+1):
        if i not in not_primes:
            primes.append(i)
            for j in range(i * i, n + 1, i):  
                not_primes.add(j)
    
    return primes



def generar_primo(Rinf, Rsup):
    
    if Rinf < 0 or Rsup == Rinf or Rsup < 0 or Rsup < Rinf:
        return None
    else:
        primos_encontrados = []
        for n in range(Rinf, Rsup+1):
            prime_list = criba(int(n**0.5))  
            es_primo = True  
            for i in prime_list:
                if n % i == 0:
                    es_primo = False
                    break
            if es_primo:
                primos_encontrados.append(n)  

        #
        if primos_encontrados:
            if len(primos_encontrados) > 1:
                return random.choice(primos_encontrados)
            else:
                return None
        return None  


#-----------------------------------------MCD-------------------------------------------------------------

def mcd(a,b):
    Qz = [] 
    if b > a:
        a, b = b, a
    if b == 0:
       
        return a
    while b != 0:
        r = a // b
        x = a % b
     
        Qz.append(r)
     
        a = b
        b = x
   
    return a,Qz





def bezout_e_inverso_modular(e, n):
    mcm,Qz = mcd(e, n)
    if mcm != 1:
       
        return None
    else:
        matrices = [] 
        for i in range(len(Qz)):
            matriz = np.array([[Qz[i], 1], [1, 0]])
            matrices.append(matriz)  
    

        if len(matrices) > 0:
            resultado = matrices[0]
            for i in range(1, len(matrices)):
                resultado = np.dot(resultado, matrices[i])  
      
            exponente = (-1)**(len(Qz))
            x1 = exponente * -(resultado[0, 1])
            y1 = exponente * (resultado[1, 1])

    
    
            resultado_inverso = x1
            while resultado_inverso < 0:
                resultado_inverso += n

            return resultado_inverso
        

def generar_llaves(rango_inf, rango_sup):
    # Tomar 2 números primos
    p = generar_primo(rango_inf, rango_sup)
    q = generar_primo(rango_inf, rango_sup)


    while p is not None and q is not None and q == p:
        q = generar_primo(rango_inf, rango_sup)

    # Si alguno es None, devolvemos None
    if p is None or q is None:
        return None
    
    # Calcular n módulo
    n = p * q

    # Calcular phi
    phi = (p - 1) * (q - 1)
    if phi <= 0:
        return None

    # Calcular e tal que 1 < e < phi y mcd(e, phi) = 1
    if phi == 2:
        return None
    e = random.randint(2, phi)
    while mcd(e, phi)[0] != 1:
        e = random.randint(2, phi)
    
    # Calcular d
    d = bezout_e_inverso_modular(e, phi)
    if d is None:
        return None

    # Verificar que e y d sean diferentes
    while e == d:
        e = random.randint(2, phi)
        while mcd(e, phi)[0] != 1:
            e = random.randint(2, phi)
        d = bezout_e_inverso_modular(e, phi)
        if d is None:
            return None

    # Asignar las llaves pública y privada
    llave_publica = (e, n)
    llave_privada = (d, n)

    return llave_publica, llave_privada



def encriptar(caracter, publica):
    caracter = int(caracter)
    publica = (int(publica[0]), int(publica[1]))
    
    if 0 < caracter < publica[1]:
        C = pow(caracter, publica[0], publica[1])  # Exponenciación modular
        return C
    else:
        return None


def descencriptar(m, private):
    m = int(m)
    private = (int(private[0]), int(private[1]))
    
    if 0 < m < private[1]:
        M = pow(m, private[0], private[1])  # Exponenciación modular
        return M
    else:
        return None


llaves = None
while True:
    
    opcion = int(input("1. Generar llaves\n2. Encriptar\n3. Desencriptar\n4. Salir\nOpcion: "))
    if opcion == 1:
        rango_inf = int(input("Ingrese el rango inferior: "))
        rango_sup = int(input("Ingrese el rango superior: "))
        llaves = generar_llaves(rango_inf, rango_sup)
        
        if llaves is not None:
            llave_publica = llaves[0]
            llave_privada = llaves[1]
            print("Llaves generadas:")
            print("Llave publica:", llave_publica)
            print("Llave privada:", llave_privada)
        else:
            print("No se pudieron generar las llaves.")



    elif opcion == 2:
        if llaves is None:
            print("Tiene que generar las llaves antes de acceder a la encriptacion.")
        else:
            print("\n")
            print("La llave publica es:", llave_publica)
            texto = int(input("Ingrese el texto a encriptar: "))
            print(f"Ingrese la llave publica: {llave_publica[0]}")
            encriptado = encriptar(texto, llave_publica)

            if encriptado is not None:
                print("Texto encriptado:", encriptado)
            else:
                print("No se pudo encriptar el texto.")

    elif opcion == 3:
        if llaves is None:
            print("Tiene que generar las llaves antes de acceder a la desencriptacion.")
        else:
            print("\n")
            print("La llave privada es:", llave_privada)
            texto = int(input("Ingrese el texto a desencriptar: "))
            print(f"Ingrese la llave privada: {llave_privada[0]}")
            desencriptado = descencriptar(texto, llave_privada)
            if desencriptado is not None:
                print("Texto descencriptado:", desencriptado)
            else:
                print("No se pudo desencriptar el texto.")

    elif opcion== 4:
        print("Saliendo...")
        break