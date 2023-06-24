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


def read_normativas():
    cursor = conn.cursor()

    # Prompt the user to choose the search criteria
    print("Seleccione el criterio de búsqueda:")
    print("1. Número de Normativa")
    print("2. Palabra Clave")
    opcion = input("Ingrese su opción: ")

    if opcion == "1":
        nro_normativa = input("Ingrese el número de normativa: ")
        query = """SELECT N.id_normativa, N.nro_normativa, N.fecha, N.descripcion, C.categoria, J.poder, O.organo, T.normativa, N.palabras_clave 
                FROM NORMATIVA N
                JOIN CATEGORIA C ON C.id_categoria = N.id_categoria 
                JOIN JURISDICCION J ON J.id_jurisdiccion = N.id_jurisdiccion 
                JOIN ORGANO_LEGISLATIVO O ON O.id_organo = N.id_organo
                JOIN TIPO_NORMATIVA T ON T.id_tipo_normativa = N.id_tipo_normativa 
                WHERE N.nro_normativa LIKE %s ;
                """
        params = (nro_normativa,)
    elif opcion == "2":
        palabra_clave = input("Ingrese la palabra clave: ")
        query = """SELECT N.id_normativa, N.nro_normativa, N.fecha, N.descripcion, C.categoria, J.poder, O.organo, T.normativa, N.palabras_clave 
                FROM NORMATIVA N
                JOIN CATEGORIA C ON C.id_categoria = N.id_categoria 
                JOIN JURISDICCION J ON J.id_jurisdiccion = N.id_jurisdiccion 
                JOIN ORGANO_LEGISLATIVO O ON O.id_organo = N.id_organo
                JOIN TIPO_NORMATIVA T ON T.id_tipo_normativa = N.id_tipo_normativa 
                WHERE N.palabras_clave LIKE %s ;
                """
        params = (f"%{palabra_clave}%",)
    else:
        print("Opción inválida.")
        return

    try:
        cursor.execute(query, params)
        normativas = cursor.fetchall()

        if normativas:
            print("Normativas:")
            for normativa in normativas:
                print('')
                print("Id Normativa: " + str(normativa[0]))
                print("Nro ley: " + str(normativa[1]))
                print("Fecha: " + str(normativa[2]))
                print("Descripción: "+ normativa[3])
                print("Tipo Categoría: " + normativa[4])
                print("Jurisdicción: "+ normativa[5])
                print("Órgano Legislativo: " + normativa[6])
                print("Tipo Normativa: " + normativa[7])
                print('Palabras Clave: '+ normativa[8])
        else:
            print("No se encontraron normativas.")
    except mysql.connector.Error as error:
        print(f"No se pudo leer la normativa: {error}")
    finally:
        cursor.close()