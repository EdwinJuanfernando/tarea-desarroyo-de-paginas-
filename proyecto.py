def suma_hasta(n):
    if n <=0:
        return 0 
    return n + suma_hasta(n - 1)
resultado =suma_hasta(4)
print(resultado)
#______________________________________
#def cuenta_ascendente(n, actual=1):
#    if actual > n:
#        return
#    print(actual)
#    cuenta_ascendente(n, actual + 1)
#cuenta_ascendente(4)    
#__________________________
#def cuenta_regresiva(n):
#    if n < 0:
#         print("¡despeque!")
#    else:
#        print(n)
#        cuenta_regresiva(n-1)
#cuenta_regresiva(5)            
#_________________________
#def suma_lista(lista):
#    return sum(lista)
#resultado = suma_lista([1,2,3])
#print(resultado)
#resultado = suma_lista([4,5,6])    
#print(resultado)
#resultado = suma_lista([5,8,16])
#print(resultado)
#__________________________
#def es_par_o_impar(n):
#    if n % 2 == 0:
#        print(f"{n}es par")
#    else:
#        print(f"{n}es impar")        

#es_par_o_impar  (2)
#es_par_o_impar  (3)
#es_par_o_impar  (4)
#es_par_o_impar  (7)

#______________________
#def conteo(n):
#    if n<0:
#     print('Despliegue')
#    else:
#        print(n)
#        conteo(n-1)
#conteo(4)        