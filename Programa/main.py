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
Qz = []  # Lista donde se almacenarán los cocientes
matrices = [] 
def mcd(a,b):
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
    return a




def bezout_e_inverso_modular(e, n):
    variable = mcd(e, n)
    mcm = variable
    if mcm != 1:
       # print(f"El MCD de {e} y {n} debe ser igual a 1 para calcular el inverso modular.")
        return None
    else:
        for i in range(len(Qz)):
            matriz = np.array([[Qz[i], 1], [1, 0]])
            matrices.append(matriz)  
            print(f"Matriz {i}:\n{matriz}")

        if len(matrices) > 0:
            resultado = matrices[0]
            for i in range(1, len(matrices)):
                resultado = np.dot(resultado, matrices[i])  
            print(f"Resultado final de multiplicar todas las matrices:\n{resultado}")
            exponente = (-1)**(len(Qz))
            x1 = exponente * -(resultado[0, 1])
            y1 = exponente * (resultado[1, 1])

           # print(f"{mcm} = {b1} ({x1}) + {a1} ({y1})") 
    
            resultado_inverso = x1
            while resultado_inverso < 0:
                resultado_inverso += n

            #print(f"El inverso modular de {a1} y {b1} es {resultado_inverso}\nya que {a1} * {resultado_inverso} = 1 mod {b1}")
            return resultado_inverso
        

def generar_llaves(rango_inf,rango_sup):
    #Tomar 2 numeros primos
    p = generar_primo(rango_inf,rango_sup)
    q = generar_primo(rango_inf,rango_sup)

    while p is not None and q is not None and q == p:
        q = generar_primo(rango_inf, rango_sup)

    # Si alguno es None, devolvemos None
    if p is None or q is None:
        return None
    

    #print(f"p = {p}")
    #print(f"q = {q}")
    
    #calcular n
    n = p * q

    #Calcular phi
    phi = (p - 1) * (q - 1)

    # Calcular e 1 < e < λ ( n ) y mcd ( e , λ ( n )) = 1
 

    # Paso 4: Calcular d (inverso modular de e mod phi_n)

    # Paso 5: Verificar que e y d sean distintos

    # Paso 6: Devolver las claves pública y privada



    #CAlcular el inverso 
    
#print(mcd(3628,4756))
#print(generar_primo(90,95))
#bezout(27,14)
#inverso_modular(10,100)
print(bezout_e_inverso_modular(7,40))
#(generar_llaves(10,100))