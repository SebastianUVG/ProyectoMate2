import numpy as np

#---------Generar primos---------
def criba(n):
    not_primes = set()
    primes = []

    for i in range(2,int(n)):
        if i in not_primes:
            continue
        
        for j in range(i*2,n,i):
            not_primes.add(j)
        primes.append(i)
    return primes


def generar_primo(Rinf,Rsup):
    for n in range(Rinf, Rsup):
        #print(n)
        prime_list = criba(int(n**0.5))
        bandera = True  
        for i in prime_list:
            if n % i == 0:
                bandera = False
        if bandera:
            print(f"El primer número primo encontrado entre {Rinf} y {Rsup} es {n}")
            return  
    print(f"No se encontraron números primos entre {Rinf} y {Rsup}")  


#-----------------------------------------MCD-------------------------------------------------------------
Qz = []  # Lista donde se almacenarán los cocientes
matrices = [] 
def mcd(a,b):
    if b > a:
        a, b = b, a
    a1 = a
    b1 = b
    if b == 0:
        print(f"El mcd de {a1} y {b1} es : {a}")
        return
    while b != 0:
        r = a // b
        x = a % b
        #print(r)
        Qz.append(r)
        print(f"{a} = {r} * {b} + {x}")
        
        #mcd = b
        a = b
        b = x
    print(f"El mcd de {a1} y {b1} es : {a}")
    return a,a1,b1

def bezout(a1,b1):
    variable = mcd(a1,b1)
    mcm = variable[0]
    for i in range(len(Qz)):
        
        matriz = np.array([[Qz[i], 1], [1, 0]])
        matrices.append(matriz)  
        print(f"Matriz {i}:\n{matriz}")

    
    if len(matrices) > 0:
        resultado = matrices[0]
        for i in range(1, len(matrices)):
            resultado = np.dot(resultado, matrices[i])  
            print(resultado)
        print(f"Resultado final de multiplicar todas las matrices:\n{resultado}")
        exponente = (-1)**(len(Qz))
        x1 = exponente * -(resultado[0,1])
        y1 = exponente * (resultado[1,1])
        
        print(f"{mcm} = {b1} ({x1}) + {a1} ({y1})") 
        return mcm,b1,x1


def bezout_e_inverso_modular(a1, b1):
    variable = mcd(a1, b1)
    mcm = variable[0]
    
    if mcm != 1:
        print(f"El MCD de {a1} y {b1} debe ser igual a 1 para calcular el inverso modular.")
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

            print(f"{mcm} = {b1} ({x1}) + {a1} ({y1})") 
    
            resultado_inverso = x1
            while resultado_inverso < 0:
                resultado_inverso += b1

            print(f"El inverso modular de {a1} y {b1} es {resultado_inverso}\nya que {a1} * {resultado_inverso} = 1 mod {b1}")
        




#mcd(18,50)
#generar_primo(90,95)
#bezout(27,14)
#inverso_modular(10,100)
bezout_e_inverso_modular(14,27)