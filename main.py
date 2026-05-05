from extract.extract import extract_data, validate_data, explore_data

from transform.transform import (
    transform_data,
    filter_last_decades,
    disasters_by_year,
    disasters_by_month,
    disasters_by_type_and_region,
    seasonal_heatmap_table,
    top_earthquakes_by_country,
    top_floods_by_region,
    droughts_by_region,
    storms_by_continent,
    wildfires_by_region_year
)

from load.load import (
    plot_disasters_by_year,
    plot_disasters_by_month,
    plot_seasonal_heatmap,
    plot_type_region,
    plot_generic_bar,
    export_table_to_csv
)


def main():
    ruta = "data/1970-2021_DISASTERS.xlsx - emdat data.csv"

    # 1. Extracción
    df = extract_data(ruta)

    validate_data(df)
    explore_data(df)

    # 2. Transformación
    df_transformado = transform_data(df)
    df_reciente = filter_last_decades(df_transformado, decades=2)

    tabla_anual = disasters_by_year(df_reciente)
    tabla_anual_total = disasters_by_year(df_transformado)
    tabla_mensual = disasters_by_month(df_reciente)
    tabla_tipo_region = disasters_by_type_and_region(df_reciente)
    tabla_heatmap = seasonal_heatmap_table(df_reciente)
    terremotos = top_earthquakes_by_country(df_reciente)
    inundaciones = top_floods_by_region(df_reciente)
    sequias = droughts_by_region(df_reciente)
    tormentas = storms_by_continent(df_reciente)
    incendios = wildfires_by_region_year(df_reciente)

    print("\nDataset transformado:")
    print(df_transformado.head())

    print("\nÚltimas dos décadas:")
    print(df_reciente[["fecha", "year", "month", "Disaster Type", "Country", "Region"]].head())

    print("\nDesastres por año:")
    print(tabla_anual.head())

    print("\nDesastres por mes:")
    print(tabla_mensual)

    print("\nTipo de desastre por región:")
    print(tabla_tipo_region.head(10))

    print("\nTabla para heatmap estacional:")
    print(tabla_heatmap.head())

    # 3. Load / salida de resultados

    plot_disasters_by_year(
    tabla_anual,
    "outputs/graficos/desastres_por_anio_ultimas_dos_decadas.png",
    title="Cantidad de desastres naturales por año - Últimas dos décadas"
    )

    plot_disasters_by_year(
    tabla_anual_total,
    "outputs/graficos/desastres_por_anio_total.png",
    title="Cantidad de desastres naturales por año - Dataset completo"
    )

    plot_disasters_by_month(
        tabla_mensual,
        "outputs/graficos/desastres_por_mes.png"
    )

    plot_seasonal_heatmap(
        tabla_heatmap,
        "outputs/graficos/heatmap_estacional.png"
    )

    plot_type_region(
        tabla_tipo_region,
        top_n=10,
        output_path="outputs/graficos/tipo_desastre_region.png"
    )

    plot_generic_bar(
        terremotos,
        x_col="Country",
        y_col="cantidad_terremotos",
        title="Países con mayor cantidad de terremotos",
        xlabel="País",
        ylabel="Cantidad de terremotos",
        output_path="outputs/graficos/terremotos_por_pais.png"
    )

    plot_generic_bar(
        inundaciones,
        x_col="Region",
        y_col="cantidad_inundaciones",
        title="Regiones con mayor cantidad de inundaciones",
        xlabel="Región",
        ylabel="Cantidad de inundaciones",
        output_path="outputs/graficos/inundaciones_por_region.png"
    )

    plot_generic_bar(
        sequias,
        x_col="Region",
        y_col="cantidad_sequias",
        title="Regiones con mayor cantidad de sequías",
        xlabel="Región",
        ylabel="Cantidad de sequías",
        output_path="outputs/graficos/sequias_por_region.png"
    )

    plot_generic_bar(
        tormentas,
        x_col="Continent",
        y_col="cantidad_tormentas",
        title="Tormentas por continente",
        xlabel="Continente",
        ylabel="Cantidad de tormentas",
        output_path="outputs/graficos/tormentas_por_continente.png"
    )

    export_table_to_csv(terremotos, "outputs/reportes/terremotos_por_pais.csv")
    export_table_to_csv(inundaciones, "outputs/reportes/inundaciones_por_region.csv")
    export_table_to_csv(sequias, "outputs/reportes/sequias_por_region.csv")
    export_table_to_csv(tormentas, "outputs/reportes/tormentas_por_continente.csv")
    export_table_to_csv(incendios, "outputs/reportes/incendios_por_region_anio.csv")

    export_table_to_csv(
        tabla_anual,
        "outputs/reportes/desastres_por_anio.csv"
    )

    export_table_to_csv(
        tabla_mensual,
        "outputs/reportes/desastres_por_mes.csv"
    )

    export_table_to_csv(
        tabla_tipo_region,
        "outputs/reportes/tipo_desastre_region.csv"
    )

    print("\nETL completado correctamente.")
    print("Gráficos guardados en outputs/graficos/")
    print("Tablas guardadas en outputs/reportes/")


if __name__ == "__main__":
    main()