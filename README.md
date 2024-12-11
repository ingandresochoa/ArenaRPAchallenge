# ArenaRPAchallenge

## Requisitos Previos

1. **Python**: Asegúrate de tener Python 3.x instalado.
2. **Dependencias**:
   - Instala las siguientes librerías ejecutando:
     ```bash
     pip install selenium pandas openpyxl
     ```
3. **Navegador y Driver**:
   - **Google Chrome**: Instala la última versión del navegador.
4. **Archivo Excel**:
   - Coloca el archivo llamado `Arena RPA FormData.xlsx` en el mismo directorio que el script, con los siguientes encabezados:
     - `Nombres`
     - `Apellidos`
     - `Empresa`
     - `Numero`
     - `Email`
     - `Pais`
     - `Web`

## Estructura del Proyecto

```
FormularioAutomatizado/
├── Arena RPA FormData.xlsx   # Archivo de datos de entrada
├── main.py                  # Script principal
├── README.md                # Archivo de documentación
```

## Cómo Ejecutar el Script

1. **Clonar el repositorio** (opcional):
   ```bash
   git clone <url_del_repositorio>
   cd FormularioAutomatizado
   ```

2. **Ejecutar el script**:
   ```bash
   python main.py
   ```

3. **Verificar resultados**:
   - El script abrirá el navegador, diligenciará el formulario y lo enviará por cada fila del Excel.
   - Después de completar los envíos, el navegador se cerrará automáticamente.

## Funciones Principales

### Clase `FormularioAutomatizado`

- **`iniciar_navegador`**: Abre el navegador, navega a la URL del formulario y maximiza la ventana.
- **`cerrar_navegador`**: Cierra el navegador al finalizar el proceso.

### Métodos Auxiliares

- **`obtener_ruta_excel`**: Verifica la existencia del archivo Excel en el directorio actual.
- **`leer_datos_excel`**: Carga los datos del archivo Excel en un DataFrame de Pandas.

### Flujo Principal

1. Carga el archivo Excel y lee los datos.
2. Inicializa el navegador y accede al formulario.
3. Itera por cada fila del archivo, llena el formulario con los datos y lo envía.
5. Cierra el navegador al finalizar.

## Posibles Errores y Soluciones

- **Archivo Excel no encontrado**:
  - Asegúrate de que el archivo `Arena RPA FormData.xlsx` está en el directorio del script.
  - Verifica que los encabezados coincidan exactamente.