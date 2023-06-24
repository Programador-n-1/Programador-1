from db_connection import conn
import mysql
from datetime import datetime

class Normativa:
   
    def __init__(self, id_normativa, nro_normativa, fecha, descripcion, id_tipo_normativa, id_categoria, id_jurisdiccion, palabras_clave):
        self.id_normativa = id_normativa
        self.nro_normativa = nro_normativa
        self.fecha = fecha
        self.descripcion = descripcion
        self.id_tipo_normativa = id_tipo_normativa
        self.id_categoria = id_categoria
        self.id_jurisdiccion = id_jurisdiccion
        self.palabras_clave = palabras_clave


def create_normativa():
    cursor = conn.cursor()
    nro_normativa = input("Ingrese el número de normativa: ")
    fecha = input("Ingrese la fecha (DD/MM/AAAA): ")
    descripcion = input("Ingrese la descripción: ")
    id_tipo_normativa = input("Ingrese el ID de tipo de normativa\n (1- Ley, 2- Decreto, 3- Resolución): ")
    id_categoria = input("Ingrese el ID de categoría\n (1- Laboral, 2- Penal, 3- Civil, 4- Comercial, 5- Familia y Sucesiones, 6- Agrario y Ambiental, 7- Minería, 8- Derecho Informático): ")
    id_jurisdiccion = input("Ingrese el ID de la jurisdicción\n (1- Nacional, 2- Provincial): ")
    palabras_clave = input("Ingrese las palabras clave separadas por coma: ")

    try:
        fecha = datetime.strptime(fecha, '%d/%m/%Y').strftime('%Y-%m-%d')
    except ValueError:
        print("Formato de fecha incorrecto. Utilice el formato DD/MM/AAAA.")

    if id_jurisdiccion == "1":
        id_organo = "1" 
    elif id_jurisdiccion == "2":
        id_organo = "2" 

    query = "INSERT INTO NORMATIVA (nro_normativa, fecha, descripcion, id_tipo_normativa, id_categoria, id_jurisdiccion, id_organo, palabras_clave) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (nro_normativa, fecha, descripcion, id_tipo_normativa, id_categoria, id_jurisdiccion, id_organo, palabras_clave)

    try:
        cursor.execute(query, values)
        conn.commit()
        print("Normativa creada exitosamente.")
    except mysql.connector.Error as error:
        print(f"No se pudo crear la normativa: {error}")
    finally:
        cursor.close()

def update_normativa():
    cursor = conn.cursor()
    id_normativa = input("Ingrese el ID de la normativa a actualizar: ")
    descripcion = input("Ingrese la nueva descripción: ")

    query = "UPDATE NORMATIVA SET descripcion = %s WHERE id_normativa = %s"
    values = (descripcion, id_normativa)

    try:
        cursor.execute(query, values)
        conn.commit()
        print("Normativa actualizada exitosamente.")
    except mysql.connector.Error as error:
        print(f"No se pudo actualizar la normativa: {error}")
    finally:
        cursor.close()


def delete_normativa():
    cursor = conn.cursor()
    id_normativa = input("Ingrese el ID de la normativa a eliminar: ")

    query = "DELETE FROM NORMATIVA WHERE id_normativa = %s"
    values = (id_normativa,)

    try:
        cursor.execute(query, values)
        conn.commit()
        print("Normativa eliminada exitosamente.")
    except mysql.connector.Error as error:
        print(f"No se pudo eliminar la normativa: {error}")
    finally:
        cursor.close()