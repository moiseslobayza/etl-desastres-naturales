# load/load.py

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def ensure_dir(output_path: str) -> None:
    """
    Crea la carpeta de salida si no existe.
    """

    if output_path:
        dirpath = os.path.dirname(output_path)

        if dirpath:
            os.makedirs(dirpath, exist_ok=True)


def save_or_show(output_path: str = None) -> None:
    """
    Guarda el gráfico si se indica una ruta.
    Si no se indica ruta, lo muestra en pantalla.
    """

    plt.tight_layout()

    if output_path:
        ensure_dir(output_path)
        plt.savefig(output_path, bbox_inches="tight")
        plt.close()
    else:
        plt.show()


def export_table_to_csv(df: pd.DataFrame, output_path: str) -> None:
    """
    Exporta una tabla resumen en formato CSV.
    """

    ensure_dir(output_path)
    df.to_csv(output_path, index=False, encoding="utf-8-sig")


def plot_disasters_by_year(
    tabla_anual: pd.DataFrame,
    output_path: str = None,
    title: str = "Cantidad de desastres naturales por año"
) -> None:
    """
    Grafica la cantidad de desastres naturales por año.
    """

    plt.figure(figsize=(12, 5))

    sns.lineplot(
        data=tabla_anual,
        x="year",
        y="cantidad_desastres",
        marker="o"
    )

    plt.title(title)
    plt.xlabel("Año")
    plt.ylabel("Cantidad de desastres")
    plt.grid(True, alpha=0.3)
    plt.xticks(tabla_anual["year"], rotation=45)

    save_or_show(output_path)


def plot_disasters_by_month(tabla_mensual: pd.DataFrame, output_path: str = None) -> None:
    """
    Grafica la cantidad de desastres naturales por mes.
    """

    plt.figure(figsize=(10, 5))

    sns.barplot(
        data=tabla_mensual,
        x="month",
        y="cantidad_desastres"
    )

    plt.title("Cantidad de desastres naturales por mes")
    plt.xlabel("Mes")
    plt.ylabel("Cantidad de desastres")
    plt.xticks(rotation=45)

    save_or_show(output_path)


def plot_seasonal_heatmap(tabla_heatmap: pd.DataFrame, output_path: str = None) -> None:
    """
    Grafica un heatmap año-mes para analizar estacionalidad.
    """

    plt.figure(figsize=(12, 7))

    sns.heatmap(
        tabla_heatmap,
        linewidths=0.3
    )

    plt.title("Heatmap estacional de desastres naturales")
    plt.xlabel("Mes")
    plt.ylabel("Año")

    save_or_show(output_path)


def plot_type_region(
    tabla_tipo_region: pd.DataFrame,
    top_n: int = 10,
    output_path: str = None
) -> None:
    """
    Grafica los principales cruces entre tipo de desastre y región.
    """

    tabla_top = tabla_tipo_region.head(top_n).copy()
    tabla_top["cruce"] = tabla_top["Disaster Type"] + " - " + tabla_top["Region"]

    plt.figure(figsize=(12, 6))

    sns.barplot(
        data=tabla_top,
        x="cantidad_desastres",
        y="cruce"
    )

    plt.title("Principales cruces entre tipo de desastre y región")
    plt.xlabel("Cantidad de desastres")
    plt.ylabel("Tipo de desastre - Región")

    save_or_show(output_path)


def plot_generic_bar(
    data: pd.DataFrame,
    x_col: str,
    y_col: str,
    title: str,
    xlabel: str,
    ylabel: str,
    output_path: str = None
) -> None:
    """
    Grafica barras para tablas resumen.
    """

    plt.figure(figsize=(10, 5))

    sns.barplot(
        data=data,
        x=x_col,
        y=y_col
    )

    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)

    save_or_show(output_path)