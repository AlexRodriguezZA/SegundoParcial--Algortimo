from grafo import Grafo
# Cargar el esquema de red de la siguiente figura en un grafo e implementar los algoritmos
# necesarios para resolver las tareas, listadas a continuación:
# 1. cada nodo además del nombre del equipo deberá almacenar su tipo: pc, notebook, servidor, router, switch, impresora;
# 2. realizar un barrido en profundidad y amplitud partiendo desde la tres notebook: Red
# Hat, Debian, Arch;
# 3. encontrar el camino más corto para enviar a imprimir un documento desde la pc:
# Debian y Red Hat, hasta el servidor “MongoDB”;
# 4. encontrar el árbol de expansión mínima;
# 5. la impresora esta temporalmente fuera de linea por mantenimiento, quítela del grafo y
# realice un barrido en profundidad para corroborar que efectivamente fue borrada;
# 6. debe utilizar un grafo no dirigido.

grafo = Grafo(dirigido=False)

def cargarvertices(grafo):
    grafo.insertar_vertice("manjaro",data={"tipo":"PC"})
    grafo.insertar_vertice("parrot",data={"tipo":"PC"})
    grafo.insertar_vertice("Fedora",data={"tipo":"PC"})
    grafo.insertar_vertice("Mint",data={"tipo":"PC"})
    grafo.insertar_vertice("Ubuntu",data={"tipo":"PC"})

    grafo.insertar_vertice("guarani",data={"tipo":"Servidor"})
    grafo.insertar_vertice("mongoDB",data={"tipo":"Servidor"})


    grafo.insertar_vertice("Impresora",data={"tipo":"impresora"})

    grafo.insertar_vertice("Router1",data={"tipo":"Router"})
    grafo.insertar_vertice("Router2",data={"tipo":"Router"})
    grafo.insertar_vertice("Router3",data={"tipo":"Router"})

    grafo.insertar_vertice("red hat",data={"tipo":"notebook"})
    grafo.insertar_vertice("debian",data={"tipo":"notebook"})
    grafo.insertar_vertice("arch",data={"tipo":"notebook"})

    grafo.insertar_vertice("switch1",data={"tipo":"switch"})
    grafo.insertar_vertice("switch2",data={"tipo":"switch"})

def cargarArista(grafo):
    grafo.insertar_arista(12,"switch2","parrot")
    grafo.insertar_arista(40,"switch2","manjaro")
    grafo.insertar_arista(5,"switch2","mongoDB")
    grafo.insertar_arista(56,"switch2","arch")
    grafo.insertar_arista(3,"switch2","Fedora")
    grafo.insertar_arista(61,"switch2","Router3")


    grafo.insertar_arista(50,"Router3","Router2")
    grafo.insertar_arista(43,"Router3","Router1")

    grafo.insertar_arista(29,"Router1","switch1")
    grafo.insertar_arista(37,"Router1","Router2")

    grafo.insertar_arista(9,"Router2","guarani")
    grafo.insertar_arista(25,"Router2","red hat")

    grafo.insertar_arista(17,"switch1","debian")
    grafo.insertar_arista(80,"switch1","Mint")
    grafo.insertar_arista(22,"switch1","Impresora")
    grafo.insertar_arista(18,"switch1","Ubuntu")

def expansionMinima(grafo):
    arbolExpancionMinima = []
    arbolExpancionMinima = grafo.prim();

    print("Arbol de expansion minima")
    for e in arbolExpancionMinima:
        print(e)

def buscarCaminoMascorto(grafo, verticeOrigen, verticeDestino):
    punto1 = grafo.buscar_vertice(verticeOrigen)
    punto2 = grafo.buscar_vertice(verticeDestino)

    caminocorto = grafo.dijkstra(punto1, punto2)

    costo = None
    while(not caminocorto.pila_vacia()):
        dato = caminocorto.desapilar()
        if(dato[1][0] == verticeDestino):
            if(costo is None):
                costo = dato[0]
            print(dato[1][0])
            verticeDestino = dato[1][1]
    print('el costo total del camino es:', costo)

#CARGAMOS LOS NODOS Y ARISTAS
cargarvertices(grafo)
cargarArista(grafo)
# print("BARRIDOS")
# posRedHAT = grafo.buscar_vertice("red hat")
# grafo.barrido_profundidad(posRedHAT)
# grafo.barrido_amplitud(posRedHAT)
# print()
# posdebian = grafo.buscar_vertice("debian")
# grafo.barrido_profundidad(posdebian)
# grafo.barrido_amplitud(posdebian)
# print()
# posArch = grafo.buscar_vertice("arch")
# grafo.barrido_profundidad(posArch)
# grafo.barrido_amplitud(posArch)

# print("Camino mas corto desde Debian")
# buscarCaminoMascorto(grafo,"debian","mongoDB")
# print("Camino mas corto desde Red Hat")
# buscarCaminoMascorto(grafo,"red hat","mongoDB")

# expansionMinima(grafo)

# grafo.eliminar_vertice("Impresora")
#VERIFICAMOS
# grafo.barrido_profundidad(0)

