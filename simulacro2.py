import json 
import os

dataAutoshop={}
dataAutoshop['autostore']={}
dataAutoshop["autostore"]["auto"]=[]
with open ('AutoShopping.json') as clientes:
    carros=json.load(clientes)
    for carro in carros['autostore']['auto']:

        carrito={}
        carrito['marca']=carro['marca']
        carrito['linea']= carro['linea']
        carrito['modelo']= carro['modelo']
        carrito['precio']= carro['precio']
        carrito['equipamiento']=carro['equipamiento']
        dataAutoshop['autostore']["auto"].append(carrito)

def msgError(msg):
    print(msg)
    input("Presione cualquier tecla para continuar...")

def validarInput(msg):
    while True:
        try: 
            n=input(msg)
            if n==None or n.strip()=="":
                msgError("Digite algun dato...") 
                continue
            break
        except Exception as e:
            msgError("Ha ocurrido un error ",e)
    return n

def validarEntero(msg):
    while True:
        try:
            n=int(input(msg))
            if n<1:
                msgError('El valor debe ser mayor a 0...')
                continue
            break
        except ValueError:
            msgError('Ingrese el dato de forma numerica...')
    return n

def listarAutos():
    os.system('clear')
    cont=0
    for elem in dataAutoshop["autostore"]["auto"]:
        cont+=1
        print(f"\n{cont}.")
        print(f"> Marca:{elem['marca']}")
        print(f"> Linea:{elem['linea']}")
        print(f"> Modelo:{elem['modelo']}")
        print(f"> Precio:{elem['precio']}")
        if type(elem['equipamiento']) is list:
            print("> Equipamiento: ")
            max=len(elem['equipamiento'])
            for i in range (0,max):
                print(f'{i+1}. {elem["equipamiento"][i]}')
        else:
            print(f"> Equipamiento:{elem['equipamiento']}")

def agregarAuto():
    os.system('clear')
    print("***REGISTRO***\n")
    marca=validarInput(">> Marca: ".capitalize())
    linea=validarInput(">> Linea: ".capitalize())
    modelo=validarInput(">> Modelo: ")
    precio=validarEntero(">> Precio: ")
    print("El equipamiento es: ")
    print("\n1. Full Equipo")
    print("2. Sin equipamiento adicional")
    print("3. Otros.")
    op=validarEntero("\nOpcion -> ")
    
    if op==1:
        dataAutoshop['autostore']['auto'].append({
            "marca":marca,
            "linea":linea,
            "modelo":modelo,
            "precio":precio,
            "equipamientos":"Full Equipo"
        })

    if op==2:
        dataAutoshop['autostore']['auto'].append({
            "marca":marca,
            "linea":linea,
            "modelo":modelo,
            "precio":precio,
            "equipamientos":"Sin equipamiento adicional"
        })

    if op==3:
        equip=validarInput("Ingrese el equipamiento separado por comas (','): ")
        equip=equip.replace(' ','')
        listEquipamiento=equip.split(",")
        dataAutoshop['autostore']['auto'].append({
            "marca":marca,
            "linea":linea,
            "modelo":modelo,
            "precio":precio,
            "equipamientos":listEquipamiento
        })

def mostrarModelo(marca):
    while True:
        try:
            modelo=validarInput("> Modelo:")
            cont=0
            for elem in dataAutoshop["autostore"]["auto"]:
                if elem["marca"]==marca and elem["modelo"]==modelo:
                    cont+=1
                    print(f"> Marca:{elem['marca']}")
                    print(f"> Linea:{elem['linea']}")
                    print(f"> Modelo:{elem['modelo']}")
                    print(f"> Precio:{elem['precio']}")
                    if type(elem['equipamiento']) is list:
                        print("> Equipamiento: ")
                        max=len(elem['equipamiento'])
                        for i in range (0,max):
                            print(f'{i+1}. {elem["equipamiento"][i]}')
                    else:
                        print(f"> Equipamiento:{elem['equipamiento']}")
            if cont==0:
                msgError("> Lo sentimos. Este modelo no se encuentra registrado.")
                x=siNo("> ¿Desea buscar otro modelo? (1=Si/2=No): ")
                if x==1:
                    continue
                break
            break
        except Exception as e:
            msgError("> Kgaste. Ocurrio un error: ", e)


def siNo(msg):
    while True:
        try:
            x=validarEntero(msg)
            if x!=1 and x!=2:
                msgError("> Si o no pendejo")
                continue
            break
        except Exception as e:
            msgError("> Kgaste. Ocurrio un error: ",e)
    return x            

def mostrarTodos(marca):
    for elem in dataAutoshop["autostore"]["auto"]:
        if elem["marca"]==marca:
            print(f"\n> Marca:{elem['marca']}")
            print(f"> Linea:{elem['linea']}")
            print(f"> Modelo:{elem['modelo']}")
            print(f"> Precio:{elem['precio']}")
            if (type(elem['equipamiento']))==type(list):
                print("> Equipamiento: ")
                max=len(elem['equipamiento'])
                for i in range (0,max):
                    print(f'{i+1}. {elem["equipamiento"][i]}')
            else:
                print(f"> Equipamiento:{elem['equipamiento']}")

def mostrarAuto():
    while True:
        try:
            cont=0
            marca=validarInput("> Marca: ")
            marca=marca.capitalize()
            for elem in dataAutoshop["autostore"]["auto"]:
                if elem["marca"]==marca:
                    cont+=1
            if cont==0:
                msgError("> Lo sentimos esta marca no se encuentra registrada...")
                x=siNo("> ¿Desea ver otra marca? (1=Si/2=No): ")
                if x==1:
                    continue
                if x==2:
                    break
            break
        except Exception as e:
            msgError("> Kgaste. Ocurrio un error: ",e)

    if cont>1:
        print("> Se encontraron varios modelos de esta marca.")
        elec=siNo("> ¿Desea ver algun modelo en particular? (1=Si/2=No): ")
        if elec==1:
            mostrarModelo(marca)
        else:
            mostrarTodos(marca)
    else:
        mostrarTodos(marca)
        
def eliminar(): 
    pass 

def menu():
    os.system('clear')
    seguir=True 
    while seguir:
        print("-"*10,"VENTA DE AUTOS","-"*10)
        print(">> MENU:")
        print("1. Mostrar todos los autos.")
        print("2. Agregar auto.")
        print("3. Mostrar un auto.")
        print("4. Actualizar datos de autos.")
        print("5. Eliminar auto.")
        print("6. Salir del programa")
        
        while True:
            try: 
                op=int(input("Opcion -> "))
                if op<1 or op>6:
                    msgError("Digite bien la opcion...")
                    continue
                break
            except ValueError:
                msgError("Ingrese la opcion de forma numerica...")

        if op==1:
            listarAutos()
        if op==2:
            agregarAuto()
        if op==3:
            mostrarAuto()
        if op==4:
           def actualizarDatos():
               pass
            
        if op==5:
            def eliminar():
                pass
            
        if op==6:
            print("Gracias por utilizar el programa... Suerte!")
            seguir=False
menu()