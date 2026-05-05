# transform/transform.py
import pandas as pd


MESES_ES = {
    1: "Enero",
    2: "Febrero",
    3: "Marzo",
    4: "Abril",
    5: "Mayo",
    6: "Junio",
    7: "Julio",
    8: "Agosto",
    9: "Septiembre",
    10: "Octubre",
    11: "Noviembre",
    12: "Diciembre"
}


def create_date_column(df: pd.DataFrame) -> pd.DataFrame:
    """
    Crea la columna 'fecha' a partir de Start Year y Start Month.
    """

    df = df.copy()

    df["Start Year"] = pd.to_numeric(df["Start Year"], errors="coerce").astype("Int64")
    df["Start Month"] = pd.to_numeric(df["Start Month"], errors="coerce").astype("Int64")

    fecha_texto = (
        df["Start Year"].astype("string")
        + "-"
        + df["Start Month"].astype("string").str.zfill(2)
        + "-01"
    )

    df["fecha"] = pd.to_datetime(fecha_texto, errors="coerce")

    return df


def clean_text_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Limpia y estandariza columnas categóricas importantes.
    """

    df = df.copy()

    columns_to_clean = [
        "Disaster Type",
        "Disaster Subtype",
        "Country",
        "Region",
        "Continent"
    ]

    for col in columns_to_clean:
        if col in df.columns:
            df[col] = (
                df[col]
                .fillna("Unknown")
                .astype(str)
                .str.strip()
                .str.replace(r"\s+", " ", regex=True)
            )

    return df


def add_temporal_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Agrega columnas auxiliares para análisis temporal.
    """

    df = df.copy()

    df["year"] = df["fecha"].dt.year
    df["month"] = df["fecha"].dt.month
    df["month_name"] = df["month"].map(MESES_ES)

    return df


def filter_last_decades(df: pd.DataFrame, decades: int = 2) -> pd.DataFrame:
    """
    Filtra el dataset para quedarse con las últimas décadas disponibles.
    """

    df = df.copy()

    max_year = int(df["year"].max())
    min_year = max_year - (decades * 10) + 1

    return df[df["year"].between(min_year, max_year)].copy()


def disasters_by_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cuenta la cantidad de desastres por año.
    """

    return (
        df.groupby("year")
        .size()
        .reset_index(name="cantidad_desastres")
        .sort_values("year")
    )


def disasters_by_month(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cuenta la cantidad de desastres por mes.
    """

    return (
        df.groupby(["month", "month_name"])
        .size()
        .reset_index(name="cantidad_desastres")
        .sort_values("month")
    )


def seasonal_heatmap_table(df: pd.DataFrame) -> pd.DataFrame:
    """
    Genera una tabla año-mes para luego visualizar como heatmap.
    """

    return pd.pivot_table(
        df,
        index="year",
        columns="month",
        aggfunc="size",
        fill_value=0
    )


def disasters_by_type_and_region(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cruza tipo de desastre con región.
    """

    return (
        df.groupby(["Disaster Type", "Region"])
        .size()
        .reset_index(name="cantidad_desastres")
        .sort_values("cantidad_desastres", ascending=False)
    )


def top_earthquakes_by_country(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    """
    Distribución geográfica de terremotos por país.
    """

    filtered = df[df["Disaster Type"].str.contains("Earthquake", case=False, na=False)]

    return (
        filtered.groupby("Country")
        .size()
        .reset_index(name="cantidad_terremotos")
        .sort_values("cantidad_terremotos", ascending=False)
        .head(top_n)
    )


def top_floods_by_region(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    """
    Regiones con mayor incidencia de inundaciones.
    """

    filtered = df[df["Disaster Type"].str.contains("Flood", case=False, na=False)]

    return (
        filtered.groupby("Region")
        .size()
        .reset_index(name="cantidad_inundaciones")
        .sort_values("cantidad_inundaciones", ascending=False)
        .head(top_n)
    )


def droughts_by_region(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    """
    Patrones regionales de sequías.
    """

    filtered = df[df["Disaster Type"].str.contains("Drought", case=False, na=False)]

    return (
        filtered.groupby("Region")
        .size()
        .reset_index(name="cantidad_sequias")
        .sort_values("cantidad_sequias", ascending=False)
        .head(top_n)
    )


def storms_by_continent(df: pd.DataFrame) -> pd.DataFrame:
    """
    Frecuencia de tormentas por continente.
    """

    filtered = df[df["Disaster Type"].str.contains("Storm", case=False, na=False)]

    return (
        filtered.groupby("Continent")
        .size()
        .reset_index(name="cantidad_tormentas")
        .sort_values("cantidad_tormentas", ascending=False)
    )


def wildfires_by_region_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Tendencia histórica de incendios forestales por región y año.
    """

    filtered = df[df["Disaster Type"].str.contains("Wildfire", case=False, na=False)]

    return (
        filtered.groupby(["year", "Region"])
        .size()
        .reset_index(name="cantidad_incendios")
        .sort_values(["year", "cantidad_incendios"], ascending=[True, False])
    )


def top_earthquakes_by_country(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    """
    Distribución geográfica de terremotos por país.
    """

    filtered = df[df["Disaster Type"].str.contains("Earthquake", case=False, na=False)]

    return (
        filtered.groupby("Country")
        .size()
        .reset_index(name="cantidad_terremotos")
        .sort_values("cantidad_terremotos", ascending=False)
        .head(top_n)
    )


def top_floods_by_region(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    """
    Regiones con mayor incidencia de inundaciones.
    """

    filtered = df[df["Disaster Type"].str.contains("Flood", case=False, na=False)]

    return (
        filtered.groupby("Region")
        .size()
        .reset_index(name="cantidad_inundaciones")
        .sort_values("cantidad_inundaciones", ascending=False)
        .head(top_n)
    )


def droughts_by_region(df: pd.DataFrame, top_n: int = 10) -> pd.DataFrame:
    """
    Patrones regionales de sequías.
    """

    filtered = df[df["Disaster Type"].str.contains("Drought", case=False, na=False)]

    return (
        filtered.groupby("Region")
        .size()
        .reset_index(name="cantidad_sequias")
        .sort_values("cantidad_sequias", ascending=False)
        .head(top_n)
    )


def storms_by_continent(df: pd.DataFrame) -> pd.DataFrame:
    """
    Frecuencia de tormentas por continente.
    """

    filtered = df[df["Disaster Type"].str.contains("Storm", case=False, na=False)]

    return (
        filtered.groupby("Continent")
        .size()
        .reset_index(name="cantidad_tormentas")
        .sort_values("cantidad_tormentas", ascending=False)
    )


def wildfires_by_region_year(df: pd.DataFrame) -> pd.DataFrame:
    """
    Tendencia histórica de incendios forestales por región y año.
    """

    filtered = df[df["Disaster Type"].str.contains("Wildfire", case=False, na=False)]

    return (
        filtered.groupby(["year", "Region"])
        .size()
        .reset_index(name="cantidad_incendios")
        .sort_values(["year", "cantidad_incendios"], ascending=[True, False])
    )


def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Ejecuta el proceso principal de transformación.
    """

    df = create_date_column(df)
    df = clean_text_columns(df)
    df = add_temporal_columns(df)

    return df