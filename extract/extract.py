import os
import pandas as pd




def extract_data(filepath: str) -> pd.DataFrame:
    """
    Lee el dataset de desastres naturales desde un archivo CSV
    y devuelve un DataFrame de pandas.
    """

    if not os.path.exists(filepath):
        raise FileNotFoundError(f"No se encontró el archivo: {filepath}")

    df = pd.read_csv(filepath, low_memory=False)

    if df.empty:
        raise ValueError("El archivo fue cargado, pero el DataFrame está vacío.")

    return df


def validate_data(df: pd.DataFrame) -> None:
    """
    Realiza validaciones básicas sobre el DataFrame cargado.
    """

    print("Carga exitosa del dataset.")
    print(f"Cantidad de filas: {df.shape[0]}")
    print(f"Cantidad de columnas: {df.shape[1]}")

    required_columns = [
        "Year",
        "Disaster Type",
        "Country",
        "Region",
        "Continent",
        "Start Year",
        "Start Month"
    ]

    missing_columns = [col for col in required_columns if col not in df.columns]

    if missing_columns:
        print("Columnas esperadas faltantes:")
        print(missing_columns)
    else:
        print("Todas las columnas principales están presentes.")


def explore_data(df: pd.DataFrame) -> None:
    """
    Muestra una exploración inicial de la estructura del dataset.
    """

    print("\nPrimeras filas:")
    print(df.head())

    print("\nColumnas del dataset:")
    print(df.columns.tolist())

    print("\nTipos de datos:")
    print(df.dtypes)

    print("\nValores nulos por columna:")
    print(df.isnull().sum())

