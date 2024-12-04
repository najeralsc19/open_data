import os
import pandas as pd

ruta = 'E://files_pandas//datos_abiertos//sinac//nacimientos'
archivos_parquet = [f for f in os.listdir(ruta) if f.endswith('.parquet')]

# Diccionario para almacenar los encabezados de cada archivo
encabezados = {}

for archivo_parquet in archivos_parquet:
    archivo_path = os.path.join(ruta, archivo_parquet)
    try:
        df = pd.read_parquet(archivo_path)
        encabezados[archivo_parquet] = df.columns.tolist()
        print(f'Encabezados de {archivo_parquet}: {df.columns.tolist()}')
    except Exception as e:
        print(f'Error al leer {archivo_parquet}: {e}')

# Mostrar los encabezados de todos los archivos
for archivo, columnas in encabezados.items():
    print(f'\nArchivo: {archivo}')
    print(f'Columnas: {columnas}')