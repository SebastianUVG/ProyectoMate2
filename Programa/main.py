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
 # Lista donde se almacenarán los cocientes

def mcd(a,b):
    Qz = [] 
    if b > a:
        a, b = b, a
    if b == 0:
        #print(f"El mcd de {a1} y {b1} es : {a}")
        return a
    while b != 0:
        r = a // b
        x = a % b
        #print(r)
        Qz.append(r)
        #print(f"{a} = {r} * {b} + {x}")
        #mcd = b
        a = b
        b = x
    #print(f"El mcd de {a1} y {b1} es : {a}")
    #print(Qz)
    return a,Qz





def bezout_e_inverso_modular(e, n):
    mcm,Qz = mcd(e, n)
    if mcm != 1:
       # print(f"El MCD de {e} y {n} debe ser igual a 1 para calcular el inverso modular.")
        return None
    else:
        matrices = [] 
        for i in range(len(Qz)):
            matriz = np.array([[Qz[i], 1], [1, 0]])
            matrices.append(matriz)  
            #print(f"Matriz {i}:\n{matriz}")

        if len(matrices) > 0:
            resultado = matrices[0]
            for i in range(1, len(matrices)):
                resultado = np.dot(resultado, matrices[i])  
            #print(f"Resultado final de multiplicar todas las matrices:\n{resultado}")
            exponente = (-1)**(len(Qz))
            x1 = exponente * -(resultado[0, 1])
            y1 = exponente * (resultado[1, 1])

           # print(f"{mcm} = {b1} ({x1}) + {a1} ({y1})") 
    
            resultado_inverso = x1
            while resultado_inverso < 0:
                resultado_inverso += n

            #print(f"El inverso modular de {e} y {n} es {resultado_inverso}\nya que {e} * {resultado_inverso} = 1 mod {n}")
            return resultado_inverso
        
llave_publica = None
llave_privada = None


def generar_llaves(rango_inf,rango_sup):
    while True:
    #Tomar 2 numeros primos
        global llave_publica, llave_privada
        p = generar_primo(rango_inf,rango_sup)
        q = generar_primo(rango_inf,rango_sup)

        # p = 5939
        # q = 9277

        while p is not None and q is not None and q == p:
            q = generar_primo(rango_inf, rango_sup)

        # Si alguno es None, devolvemos None
        if p is None or q is None:
            return None
        

        #print(f"p = {p}")
        #print(f"q = {q}")
        
        #calcular n modulo
        n = p * q

        #Calcular phi
        phi = (p - 1) * (q - 1)
        #print(phi)

        # Calcular e 1 < e < λ ( n ) y mcd ( e , λ ( n )) = 1
        
        e = random.randint(2, phi)
        while mcd(e, phi)[0] != 1:
            e = random.randint(2, phi)

        #e =   30612487
        #phi = 55080888

        #Calcular d
        d = bezout_e_inverso_modular(e, phi)
        if d is None:
            continue

        # Verificar que e y d sean diferentes
        if e != d:
            llave_publica = (e, n)
            llave_privada = (d, n)
            return llave_publica, llave_privada
        #print(d)
        return None
    

def encriptar(caracter, publica):
    # C = m^e modulo n

    if caracter < publica[0] and caracter > 0:
        C = (caracter**publica[0]) % publica[1]
        return C
    else:
        return None


 #c=me modulo n, donde m es el texto en claro, c es el texto cifrado y (e, n) es la clave pública del destinatario.

def descencriptar(c, private):
    pass

#print(mcd(11,3))
#print(mcd(3,11))
#print(generar_primo(90,95))
#bezout(27,14)
#inverso_modular(10,100)
#print(bezout_e_inverso_modular(30612487,55080888))
#print(bezout_e_inverso_modular(3,11))

#print(generar_llaves(1000,10000))

#print(generar_primo(90,96))




while True:
    opcion = int(input("1. Generar llaves\n2. Encriptar\n3. Desencriptar\n4. Salir\nOpcion: "))
    if opcion == 1:
        rango_inf = int(input("Ingrese el rango inferior: "))
        rango_sup = int(input("Ingrese el rango superior: "))

        if generar_llaves(rango_inf, rango_sup) is not None:
            print("Llaves generadas:")
            print("Llave publica:", llave_publica)
            print("Llave privada:", llave_privada)
        else:
            print("No se pudieron generar las llaves.")



    elif opcion == 2:
        print("\n")
        print("La llave publica es:", llave_publica)
        texto = int(input("Ingrese el texto a encriptar: "))
        print(f"Ingrese la llave publica: {llave_publica[0]}")
        encriptado = encriptar(texto, llave_publica)

        if encriptado is not None:
            print("Texto encriptado:", encriptado)
        else:
            print("No se pudo encriptar el texto.")