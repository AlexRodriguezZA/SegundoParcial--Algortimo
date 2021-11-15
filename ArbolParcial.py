from arbol_binario import Arbol
# El encargado de Jurassic World nos solicita que desarrollemos un algoritmo que nos permita
# resolver los siguientes requerimientos:
# 1. almacenar los datos de los distintos dinosaurios que hay en la isla, de cada uno se
# conoce su nombre, código de cinco dígitos y zona de ubicación (un dígito y un carácter
# por ejemplo 7A), existen varios dinosaurios con el mismo nombre pero sus códigos son
# distintos, los códigos no pueden ser repetidos (tenga cuidado);
# 2. se deben almacenar los datos en dos arboles uno ordenado por nombre y otro por
# código;
# 3. realizar un barrido en orden del árbol ordenado por nombre;
# 4. mostrar toda la información del dinosaurio 792;
# 5. mostrar toda la información de todos los T-Rex que hay en la isla;
# 6. modificar el nombre del dinosaurio en Sgimoloch en ambos arboles porque esta mal
# cargado, su nombre correcto es Stygimoloch;
# 7. mostrar la ubicación de todos los Raptores que hay en la isla;
# 8. contar cuantos Diplodocus hay en el parque;
# 9. debe cargar al menos 15 elementos.

arbol = Arbol()
arbolCodigo = Arbol()

def mostarInfo(arbol,codigo):
    pos = arbol.busqueda(codigo)
    if(pos):
        print(pos.datos)

def modificarDino(arbol,arbolcodigo):
    pos = arbol.busqueda("Sgimolochr")
    if(pos):
        pos.datos['nombre'] = "Stygimoloch"
        pos.info = "Stygimoloch"
        #LO CAMBIAMOS DEL ARBOL DE CODIGOS
        poscodigo = arbolcodigo.busqueda(pos.datos["codigo"])
        if (poscodigo):
            poscodigo.datos["nombre"] = "Stygimoloch"
    else:
        print("NO se encuentra")
 

dino = {"nombre":"T-Rex","codigo":23450,"zona":"7A"}
arbol = arbol.insertar_nodo(dino["nombre"],dino)
arbolCodigo = arbolCodigo.insertar_nodo(dino["codigo"],dino)
dino = {"nombre":"T-Rex","codigo":22350,"zona":"9A"}
arbol = arbol.insertar_nodo(dino["nombre"],dino)
arbolCodigo = arbolCodigo.insertar_nodo(dino["codigo"],dino)
dino = {"nombre":"Diplodocus","codigo":23350,"zona":"7A"}
arbol = arbol.insertar_nodo(dino["nombre"],dino)
arbolCodigo = arbolCodigo.insertar_nodo(dino["codigo"],dino)
dino = {"nombre":"Argentinosaurus","codigo":28450,"zona":"8M"}
arbol = arbol.insertar_nodo(dino["nombre"],dino)
arbolCodigo = arbolCodigo.insertar_nodo(dino["codigo"],dino)
dino = {"nombre":"Sgimolochr","codigo":90850,"zona":"2A"}
arbol = arbol.insertar_nodo(dino["nombre"],dino)
arbolCodigo = arbolCodigo.insertar_nodo(dino["codigo"],dino)
dino = {"nombre":"T-Rex","codigo":23250,"zona":"4M"}
arbol = arbol.insertar_nodo(dino["nombre"],dino)
arbolCodigo = arbolCodigo.insertar_nodo(dino["codigo"],dino)
dino = {"nombre":"Diplodocus","codigo":21450,"zona":"7A"}
arbol = arbol.insertar_nodo(dino["nombre"],dino)
arbolCodigo = arbolCodigo.insertar_nodo(dino["codigo"],dino)
dino = {"nombre":"Diplodocus","codigo":792,"zona":"1Q"}
arbol = arbol.insertar_nodo(dino["nombre"],dino)
arbolCodigo = arbolCodigo.insertar_nodo(dino["codigo"],dino)
dino = {"nombre":"T-Rex","codigo":23420,"zona":"7A"}
arbol = arbol.insertar_nodo(dino["nombre"],dino)
arbolCodigo = arbolCodigo.insertar_nodo(dino["codigo"],dino)
dino = {"nombre":"Triseraptop","codigo":26650,"zona":"9A"}
arbol = arbol.insertar_nodo(dino["nombre"],dino)
arbolCodigo = arbolCodigo.insertar_nodo(dino["codigo"],dino)
dino = {"nombre":"Raptores","codigo":44440,"zona":"3A"}
arbol = arbol.insertar_nodo(dino["nombre"],dino)
arbolCodigo = arbolCodigo.insertar_nodo(dino["codigo"],dino)
dino = {"nombre":"T-Rex","codigo":98888,"zona":"4M"}
arbol = arbol.insertar_nodo(dino["nombre"],dino)
arbolCodigo = arbolCodigo.insertar_nodo(dino["codigo"],dino)
dino = {"nombre":"Triseraptop","codigo":18348,"zona":"2P"}
arbol = arbol.insertar_nodo(dino["nombre"],dino)
arbolCodigo = arbolCodigo.insertar_nodo(dino["codigo"],dino)
dino = {"nombre":"Raptores","codigo":15000,"zona":"2Z"}
arbol = arbol.insertar_nodo(dino["nombre"],dino)
arbolCodigo = arbolCodigo.insertar_nodo(dino["codigo"],dino)
dino = {"nombre":"Argentinosaurus","codigo":45678,"zona":"4Z"}
arbol = arbol.insertar_nodo(dino["nombre"],dino)
arbolCodigo = arbolCodigo.insertar_nodo(dino["codigo"],dino)
dino = {"nombre":"Raptores","codigo":98213,"zona":"9A"}
arbol = arbol.insertar_nodo(dino["nombre"],dino)
arbolCodigo = arbolCodigo.insertar_nodo(dino["codigo"],dino)

# arbol.inorden()

# mostarInfo(arbolCodigo,792)

# print("T-REXs")
# arbol.mostrarTRex()

# modificarDino(arbol,arbolCodigo)

# print("La ubicacion de los raptores")
# arbol.ubicacionRaptores()

# print("La cantidad de diplodocus es de ")
# print(arbol.contadordiplo())