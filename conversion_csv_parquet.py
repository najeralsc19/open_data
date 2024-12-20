import os
import pandas as pd

def codificaciones(archivo_path):
    codif = ['utf-8', 'latin1', 'iso-8859-1', 'cp1252']
    for codificacion in codif:
        try:
            df = pd.read_csv(archivo_path, encoding=codificacion, low_memory=False)
            return df
        except UnicodeDecodeError:
            continue
    raise UnicodeDecodeError(f'No se pudo leer el archivo {archivo_path} con las codificaciones probadas.')

ruta = 'E://files_pandas//datos_abiertos//sinac'
errores = []

# Listar todos los archivos CSV en la ruta
archivos_csv = [f for f in os.listdir(ruta) if f.endswith('.csv')]

for archivo_csv in archivos_csv:
    try:
        archivo_path = os.path.join(ruta, archivo_csv)
        df = codificaciones(archivo_path)
        archivo_parquet = archivo_csv.replace('.csv', '.parquet')
        df.to_parquet(os.path.join(ruta, archivo_parquet))
        print(f'Convertido {archivo_csv} a {archivo_parquet}')
    except Exception as e:
        print(f'Error al convertir {archivo_csv}: {e}')
        errores.append((archivo_csv, str(e)))

if errores:
    print('Los siguientes archivos no se pudieron convertir:')
    for archivo, error in errores:
        print(f'Archivo: {archivo}, Error: {error}')
else:
    print('Todos los archivos se convirtieron correctamente')