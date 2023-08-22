import os 
""" Elabore un programa Python para gestionar el CRUD del archivo de datos PetShopping.json con las siguientes funcionalidades:

    
Mostrar en pantalla todas las mascotas a la venta visualizando: Tipo, Raza, Precio y Servicios

    
Crear Nueva mascota con la posibilidad de múltiples ítems de Servicio

    
Mostrar los datos de Mascotas por Tipo elegido visualizando: Raza, Precio y Servicios

    
Actualizar los datos de una mascota consultada por índice (Mostrar el listado total y elegir por     índice)

    
Eliminar una mascota de la tienda (Mostrar el listado total y elegir por índice) """

import json 

dataPetShop={}
dataPetShop['pets']=[]
with open ('PetShopping.json') as clientes:
    mascotas=json.load(clientes)
    for elem in mascotas['pets']:

        puichico={}
        puichico['tipo']=elem['tipo']
        puichico['raza']= elem['raza']
        puichico['talla']= elem['talla']
        puichico['precio']= elem['precio']
        puichico['servicios']=elem['servicios']
        dataPetShop['pets'].append(puichico)



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

def listarMascotas():
    os.system('clear')
    cont=0
    for elem in dataPetShop['pets']:
        cont+=1
        print(f"\n{cont}.")
        print(f"> Tipo:{elem['tipo']}")
        print(f"> Raza:{elem['raza']}")
        print(f"> Precio:{elem['precio']}")
        print("> Servicios: ")
        max=len(elem['servicios'])
        for i in range (0,max):
            print(f'{i+1}. {elem["servicios"][i]}')
        print("-"*30)

def agregarMascota():
    os.system('clear')
    print("***REGISTRO***\n")
    tipo=validarInput(">> Tipo: ".capitalize())
    raza=validarInput(">> Raza: ")
    talla=validarInput(">> Talla (grande/mediano/pequeño): ")
    precio=validarEntero(">> Precio: ")
    servicios=validarInput("Ingrese los servicios separados por comas (','): ")
    servicios=servicios.replace(' ','')
    listServicios=servicios.split(",")
    dataPetShop['pets'].append({
        "tipo":tipo,
        "raza":raza,
        "talla":talla,
        "precio":precio,
        "servicios":listServicios
    })

    with open ('PetShopping.json','w') as miArchivo:
        json.dump(dataPetShop,miArchivo,ensure_ascii=False,indent=8)

def actualizarTipo(indiMascota):
    os.system('clear')
    new=validarInput(">> Ingrese el cambio de tipo: ")
    dataPetShop['pets'][indiMascota]['tipo']=new.capitalize()
    UpdateJson()

def actualizarRaza(indiMascota):
    os.system('clear')
    new=validarInput(">> Ingrese el cambio de raza: ")
    dataPetShop['pets'][indiMascota]['raza']=new
    UpdateJson()

def actualizarTalla(indiMascota):
    os.system('clear')
    new=validarInput(">> Ingrese el cambio de talla: ")
    dataPetShop['pets'][indiMascota]['talla']=new
    UpdateJson()

def actualizarPrecio(indiMascota):
    os.system('clear')
    new=validarEntero(">> Ingrese el cambio de precio: ")
    dataPetShop['pets'][indiMascota]['precio']=new
    UpdateJson()

def actualizarServicios(indiMascota):
    os.system('clear')
    new=validarInput(">> Ingrese el cambio de servicios separados por coma. (','): ")
    new=new.replace(' ','')
    listNew=new.split(',')
    dataPetShop['pets'][indiMascota]['servicios']=listNew
    UpdateJson()

def opcionesCambio():
    os.system('clear')
    indiMascota=buscarMascota("Cual mascota desea modificar?. (Ingrese el indice): ")
    print("\nQue dato desea actualizar?")
    print("\n***OPCIONES***\n")
    print("1. Tipo.")
    print("2. Raza.")
    print("3. Talla.")
    print("4. Precio.")
    print("5. Servicios.")
    print("6. Ninguno.")
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
        actualizarTipo(indiMascota)
    if op==2:
        actualizarRaza(indiMascota)
    if op==3:
        actualizarTalla(indiMascota)
    if op==4:
        actualizarPrecio(indiMascota)
    if op==5:
        actualizarServicios(indiMascota)

def buscarMascota(msg):
    os.system('clear')
    listarMascotas()
    while True:
        try:
            r=int(input(msg))
            numMacotas=len(dataPetShop['pets'])
            if r<1 or r>numMacotas:
                msgError("Indice incorrecto. Vuelva a intentarlo")
                continue
            else:    
                indiMascota=r-1
                break
        except ValueError:
            msgError("Ingrese el indice de forma numerica...")
    return indiMascota

def actualizarDatos():
    opcionesCambio()

def eliminar():
    os.system('clear')
    listarMascotas()
    indiMascota=buscarMascota("Ingrese el indice de la mascota que desea eliminar: ")
    mascotaEliminada=dataPetShop['pets'].pop(indiMascota)
    print ("Se elimino: ")
    print(f"> Tipo:{mascotaEliminada['tipo']}")
    print(f"> Raza:{mascotaEliminada['raza']}")
    print(f"> Precio:{mascotaEliminada['precio']}")
    UpdateJson()

def UpdateJson():
    with open ('PetShopping.json','w') as miArchivo:
        json.dump(dataPetShop,miArchivo,ensure_ascii=False,indent=8)

def buscarPorTipo():
    os.system('clear')
    r=validarInput("Ingrese el tipo: ")
    cont=0
    for elem in dataPetShop["pets"]:
        if elem['tipo']==r.capitalize():
            cont+=1
            print(f"\n{cont}.")
            print(f"> Raza:{elem['raza']}")
            print(f"> Precio:{elem['precio']}")
            print("Servicios: ")
            max=len(elem['servicios'])
            for i in range (0,max):
                print(f'{i+1}. {elem["servicios"][i]}')
    if cont==0:
        msgError("Este tipo no se encuentra en la tienda...")        
        
def mostrarMascota():
    os.system('clear')
    print("***BUSCAR MASCOTA***")
    buscarPorTipo()

def menu():
    os.system('clear')
    seguir=True 
    while seguir:
        print("-"*10,"TIENDA DE MASCOTAS","-"*10)
        print(">> MENU:")
        print("1. Mostrar todas las mascotas.")
        print("2. Agregar mascota.")
        print("3. Mostrar una mascota.")
        print("4. Actualizar datos de mascota.")
        print("5. Eliminar mascota.")
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
            listarMascotas()
        if op==2:
            agregarMascota()
        if op==3:
            mostrarMascota()
        if op==4:
            actualizarDatos()
        if op==5:
            eliminar()
        if op==6:
            print("Gracias por utilizar el programa... Suerte!")
            seguir=False
menu()