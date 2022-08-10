import sys

#realizar un script que imprima una palabra una cantidad de veces pasada por parametro
# imprimir hola 5    


if len(sys.argv) != 3:
    print("error necesito 2 argumentos")
else:
    palabra=sys.argv[1]
    cantidad=int(sys.argv[2])


    for i in range(cantidad):
        print(palabra)
