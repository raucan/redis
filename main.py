import redis

redis = redis.Redis(host= 'localhost', port= '6379', db=1)

def main():
    menu = """
1) Agregar nueva palabra
2) Editar palabra existente
3) Eliminar palabra existente
4) Ver listado de palabras
5) Buscar significado de palabra
6) Salir
Elige: """
    eleccion = ""
    while eleccion != "6":
        eleccion = input(menu)
        if eleccion == "1":
            palabra = input("Ingresa la palabra que quieres agregar: ")
            # Comprobar si no existe
            posible_significado = buscar_significado_palabra(palabra)
            if posible_significado:
                print(f"La palabra '{palabra}' ya existe")
            else:
                significado = input("Ingresa el significado de la palabra: ")
                agregar_palabra(palabra, significado)
                print("Palabra agregada")
        if eleccion == "2":
            palabra = input("Ingresa la palabra que quieres editar: ")
            nuevo_significado = input("Ingresa el nuevo significado: ")
            editar_palabra(palabra, nuevo_significado)
            print("Palabra actualizada")
        if eleccion == "3":
            palabra = input("Ingresa la palabra que quieres eliminar: ")
            eliminar_palabra(palabra)
        if eleccion == "4":
            print("=== Lista de palabras ===")
            palabras = obtener_palabras()

        if eleccion == "5":
            palabra = input(
                "Ingresa la palabra de la cual quieres saber el significado: ")
            significado = buscar_significado_palabra(palabra)

def agregar_palabra(palabra, significado):
    redis.set(palabra, significado)
def editar_palabra(palabra, nuevo_significado):
    redis.delete(palabra)
    redis.set(palabra, nuevo_significado)
def eliminar_palabra(palabra):
    redis.delete(palabra)
def obtener_palabras():
    palabras=redis.hgetall(redis)
    print(palabras)
def buscar_significado_palabra(palabra):
    palabras=redis.get(palabra)
    print(palabras)

if __name__ == '__main__':
    main()
