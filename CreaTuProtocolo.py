import os

a=0
print('''

***Bienvenido a la maquina creadora de protocolos***

''')
def menu():
    print('''
._._._._._._._._._._._._
    Opciones
    1)Crear protocolo
    2)Agregar linea
    3)Eliminar
    4)Mostrar
._._._._._._._._._._._._
''')
menu()
elige=input("Desea elegir una opción? s/n ")
if (elige == "N" or elige == "s" or elige == "S" or elige == "n"):

    print("Numero de opción")
    while (elige == "s" or elige == "S"):
        opcion=int(input("Cual elige? "))
        
        if opcion == 1:
            print("___________________")
            name=input("Cuál es el nombre de su protocolo? ")
            protocolo = open(name + ".txt", 'w')
            protocolo.write(name+ '''\n \n''')
            
            esc=input("Desea escribir las líneas? s/n ")
            while (esc == "s" or esc=="S"):
                a=a+1

                print("____________")
                linea=input("Escriba la "+str(a)+"° línea: ")
                protocolo.write(str(a) +"-"+ linea + '''\n''')
                
                sub=input("Quiere que tenga subinstrucción? s/n")
                
                if (sub == "s" or sub=="S"):
                    
                    subinstruccion=input("Escribala: ")
                    protocolo.write("    "+str(a)+".1-"+subinstruccion+'''\n''')
                    
                esc=input("Desea escribir la siguiente instrucion? s/n ")
            print("Terminamos gracias")
            protocolo.close()
            
        elif  opcion == 2:
            print("-----------------")
            
            name=input("Escriba el nombre del protocolo que quiere agregar la línea: ")
            protocolo = open(name + ".txt",'a')
            
            esc=input("Desea agregar una línea? s/n ")
            while (esc == "s" or esc=="S"):

                print("-------------")
                linea=input("Escriba la línea: ")
                protocolo.write("-"+ linea + '''\n''')
                
                sub=input("Quiere que tenga subinstrucción? s/n")
                
                if (sub == "s" or sub=="S"):
                    
                    subinstruccion=input("Escribala: ")
                    protocolo.write(".   -"+subinstruccion+'''\n''')
                    
                esc=input("Desea escribir la otra instrucion? s/n ")
            print("terminamos el cambio en el protocolo "+name)
            protocolo.close()
            
            
        elif  opcion == 3:
            print("-----------------")
            name=input("Escriba el nombre del protocolo que quiere borrar: ")
            os.remove(name + ".txt")
            print("SE HA BORRADO EL PROTOCOLO")
            
        elif  opcion == 4:
            print("-----------------")
            name=input("Escriba el nombre del protocolo que quiere ver: ")
            protocolo = open(name + ".txt")
            print(protocolo.read())
            protocolo.close()
                   
        elige=input("Desea elegir una opción? s/n ")
        if (elige=="s" or elige=="S"):
            continue
        else:
            break
    print("Hasta luego :)")
    
else:
    print("Gracias por su visita <3")
