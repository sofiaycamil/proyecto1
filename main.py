import  sqlite3

def conectar():
    return sqlite3.connect("hospital.db")

def agregar():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    fecha = int(input("Fecha: "))
    que_necesita = input("¿Qué necesita?: ")
    
    conn = conectar()
    conn.execute ("INSERT INTO consulta (nombre, edad, fecha, 'que necesita') VALUES (?,?, ?, ?)")

    conn.commit()
    conn.close()
    print("Registro agregado.")
def mostrar():
    conn = conectar()
    cursor = conn.execute("SELECT * FROM consulta")
    filas = cursor.fetchall()
    for fila in filas:
        print(fila)
    conn.close()

def eliminar():
    nombre = input("Ingrese el nombre de la persona a eliminar: ")
    conn = conectar()
    conn.execute("DELETE FROM consulta WHERE nombre = ?", (nombre,))
    conn.commit()
    conn.close()
    print("Registro eliminado.")
def buscar():
    nombre = input("Ingrese el nombre a buscar: ")
    conn = conectar()
    cursor = conn.execute("SELECT * FROM consulta WHERE nombre = ?", (nombre,))
    resultados = cursor.fetchall()
    if resultados:
        for fila in resultados:
            print(fila)
    else:
        print("No se encontraron resultados.")
    conn.close()

def menu():
    while True:
        print("Menú")
        print("1. Agregar registro")
        print("2. Mostrar registros")
        print("3. Eliminar registro")
        print("4. Buscar registro")
        print("5. Salir")
opcion = input("Elegí una opción: ")
match opcion:
 case "1":
  agregar()
 case "2":
    mostrar()
 case "3":
    eliminar()
 case "4":
    buscar()
 case "5":
    print("Programa finalizado.")
    break
 case _:
    print("Opción no válida.")

menu()