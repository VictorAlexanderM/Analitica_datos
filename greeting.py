
import pandas as pd
# greeting.py - A simple script to greet the user
def greet():
    print("Hello! Welcome to this Python script")

    archivo_excel = 'ruta/al/archivo.xlsx'
    # Lee el archivo Excel y guarda los datos en un DataFrame
    df = pd.read_excel(archivo_excel, sheet_name='NombreDeLaHoja')

    # Muestra las primeras filas del DataFrame
    print(df.head())
if __name__ == "__main__":
    greet()
