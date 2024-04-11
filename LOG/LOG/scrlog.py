import logging

def generar_log(log: str):
    # Configuración básica de los registros
    logging.basicConfig(filename='mi_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

    try:
        # Aquí puedes agregar tu lógica o procesamiento
        # ...

        # Ejemplo de registro de un error
        logging.error(f"Error en el proceso: {log}")

        # Ejemplo de registro de información adicional
        logging.info("Información adicional relevante")

    except Exception as e:
        # Manejo de excepciones y registro de errores
        logging.exception(f"Excepción ocurrida: {str(e)}")

if __name__ == "__main__":
    generar_log("Este es un mensaje de prueba")
    
#Se configura un archivo de registro llamado mi_log.txt.
#Se utiliza el nivel de registro INFO para registrar información general.
#Se registra un mensaje de error y también información adicional.