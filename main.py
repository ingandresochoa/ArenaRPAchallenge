import pandas as pd

def leer_datos_excel(ruta_archivo, nombre_hoja = 0):
    try:
        df = pd.read_excel(ruta_archivo, sheet_name=nombre_hoja)
        return df
    except FileNotFoundError:
        print("El archivo Excel no fue encontrado.")
        return None
    except Exception as e:
        print(f"Error al leer el archivo Excel: {e}")
        return None
    
def main():
    
    ruta_archivo = "C:\\Users\\andre\\OneDrive\\Escritorio\\dev\\ArenaRPAchallenge\\Arena RPA FormData.xlsx"
    
    datos = leer_datos_excel(ruta_archivo)

    if datos is not None:
        print(datos)

if __name__ == "__main__":
    main()