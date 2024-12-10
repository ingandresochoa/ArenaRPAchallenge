from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import pandas as pd
import time

class FormularioAutomatizado:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
    
    def iniciar_navegador(self):
        self.driver.get("https://arenarpa.com/crazy-form")
        self.driver.maximize_window()
        time.sleep(10)
    
    def cerrar_navegador(self):
        self.driver.quit()

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

    for index, fila in datos.iterrows():
        print(f"{fila['Nombres']} {fila['Apellidos']} - {fila['Empresa']} - {fila['Numero']} - {fila['Email']} - {fila['Pais']} - {fila['Web']}")

    bot = FormularioAutomatizado()
    try:
        bot.iniciar_navegador()
        bot.cerrar_navegador()
    finally:
        bot.cerrar_navegador()

if __name__ == "__main__":
    main()