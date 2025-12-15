import csv
archivoCrudo= "Archivos/train-metadata.csv"
archivoFiltrado = "Archivos/datasetFiltrado.csv"
def filtrado(archivoCrudo, archivoFiltrado):
    """filtrado
    Filtra el dataset original de la ISIC2024 con las variables selecionadas:
    {
    target,clin_size_long_diam_mm,tbp_lv_areaMM2,tbp_lv_perimeterMM,tbp_lv_color_std_mean,
    tbp_lv_deltaLBnorm,tbp_lv_minorAxisMM,tbp_lv_norm_border,tbp_lv_symm_2axis,
    tbp_lv_symm_2axis_angle
    }
    este filtrado solo toma en cuenta las imagenes que son 3D: XP y que los valores normalizados no sean 0 ni 10
    Args:
        archivoCrudo (str): path del dataset original
        archivoFiltrado (str): path del dataset filtrado
    """
    try:
        listadoFiltrado = []
        with open(archivoCrudo, "r", encoding="utf-8", newline="") as archivo:
            reader = csv.reader(archivo)
            header = next(reader)
            listadoFiltrado.append([header[1], header[6], header[19], header[34], header[21], header[26], header[30], header[32], header[38], header[39]]) 
            for row in reader:
                if row[1] != "" and row[6] != "" and row[19] != "" and row[34] != "" and row[21] != "" and row[26] != "" and row[30] != "" and row[32] != "" and row[38] != "" and row[39] != "" and row[8].__contains__("3D: XP") and row[21]!=0 and row[21]!=10 and row[26]!=0 and row[26]!=10:
                    listadoFiltrado.append([row[1], row[6], row[19], row[34], row[21], row[26], row[30], row[32], row[38], row[39]])
        with open(archivoFiltrado, "w", encoding="utf-8", newline="") as archivoE:
            writer = csv.writer(archivoE)
            for row in listadoFiltrado:
                writer.writerow(row)
    except Exception as e:
        print(f"Se ha producido un error: {e}")
filtrado(archivoCrudo, archivoFiltrado)
