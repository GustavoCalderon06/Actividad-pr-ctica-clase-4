import requests
import re

# URL base del microservicio Flask
base_url  ='http://52.200.139.211:8000/tareas'

def obtener_tareas():
    response = requests.get(base_url)
    return response.json()

def agregar_tarea(titulo, descripcion, rut):
    data = {"titulo": titulo, "descripcion": descripcion, "rut": rut}
    response = requests.post(base_url, json=data)
    return response.json()


def actualizar_tarea(tarea_id, titulo, descripcion):
    data = {"titulo": titulo, "descripcion": descripcion}
    url = f"{base_url}/{tarea_id}"
    response = requests.put(url, json=data)
    return response.json()

def eliminar_tarea(tarea_id):
    url = f"{base_url}/{tarea_id}"
    response = requests.delete(url)
    return response.json()

if __name__ == "__main__":
    while True:
        print("\nOpciones:")
        print("1. Obtener todas las tareas")
        print("2. Agregar una nueva tarea")
        print("3. Actualizar una tarea")
        print("4. Eliminar una tarea")
        print("5. Salir")

        opcion = input("Ingrese el número de la opción que desea realizar: ")

        if opcion == "1":
            print("Obteniendo todas las tareas:")
            print(obtener_tareas())
        elif opcion == "2":
            rut = input("Ingrese su RUT (formato: XX.XXX.XXX-X o XX.XXX.XXX-K): ")
            while not re.match(r'^\d{2}\.\d{3}\.\d{3}-[kK0-9]$', rut):
                print("RUT inválido. Por favor, ingrese un RUT válido.")
                rut = input("Ingrese su RUT (formato: XX.XXX.XXX-X o XX.XXX.XXX-K): ")

            titulo = input("Ingrese el título de la tarea: ")
            descripcion = input("Ingrese la descripción de la tarea: ")
            print("Agregando una nueva tarea:")
            print(agregar_tarea(titulo, descripcion, rut))

        elif opcion == "3":
            tarea_id = input("Ingrese el ID de la tarea a actualizar: ")
            titulo = input("Ingrese el nuevo título de la tarea: ")
            descripcion = input("Ingrese la nueva descripción de la tarea: ")
            print("Actualizando una tarea:")
            print(actualizar_tarea(tarea_id, titulo, descripcion))
        elif opcion == "4":
            tarea_id = input("Ingrese el ID de la tarea a eliminar: ")
            print("Eliminando una tarea:")
            print(eliminar_tarea(tarea_id))
        elif opcion == "5":
            break
        else:
            print("Opción inválida. Por favor, ingrese un número válido.")
