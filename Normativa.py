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