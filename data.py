# Datos auditados del archivo Excel de Corporación Rehobot.
# Actualiza estos valores cuando se modifique el Excel.
# Los importes y métricas se mantienen separados por objetivo para evitar
# sumar beneficios de distinta naturaleza (ahorros laborales vs. diferencias de inventario).

OBJETIVO_1 = {
    "nombre": "Optimización del almacén y preparación de recursos",
    "antes": {
        "tiempo_min": 85.0,
        "costo_servicio": 34.0,
        "costo_mensual": 136.0,
        "costo_anual": 1632.0,
        "distancia_m": 120.0,
    },
    "despues": {
        "tiempo_min": 60.0,
        "costo_servicio": 24.0,
        "costo_mensual": 96.0,
        "costo_anual": 1152.0,
        # La distancia propuesta se deja pendiente porque la hoja requiere
        # reconciliar el detalle del layout con el indicador consolidado.
        "distancia_m": None,
    },
    "frecuencia_mensual": 4,
    "inversion": 434.0,
    "ahorro_mensual": 40.0,
    "ahorro_anual": 480.0,
    "pri_meses": 10.85,
    "beneficio_neto_anio1": 46.0,
    "abc_resumen": [
        {"clase": "A", "valor": 84000.0},
        {"clase": "B", "valor": 11000.0},
        {"clase": "C", "valor": 5000.0},
    ],
    "alertas": [
        "La distancia TO BE del layout debe conciliarse con el indicador consolidado antes de publicarse.",
        "La frecuencia de 4 preparaciones mensuales es un supuesto de simulación.",
    ],
}

OBJETIVO_2 = {
    "nombre": "Estandarización del mantenimiento mediante POE y 5S",
    "antes": {
        "tiempo_min": 371.25,
        "tiempo_horas": 6.1875,
        "costo_servicio": 371.25,
        "costo_nva": 71.25,
        "cumplimiento_5s": 14.0,
    },
    "despues": {
        "tiempo_min": 288.0,
        "tiempo_horas": 4.8,
        "costo_servicio": 288.0,
        "costo_nva": 3.0,
        "cumplimiento_5s": 78.0,
    },
    "ahorro_por_servicio": 83.25,
    "ahorro_nva_incluido": 68.25,
    "inversion": 290.0,
    "punto_equilibrio_servicios": 4,
    "alertas": [
        "No se encontró una frecuencia anual de servicios suficientemente documentada para calcular ahorro anual, ROI anual o PRI anual.",
        "El ahorro NVA de S/ 68.25 está incluido en el ahorro total de S/ 83.25 por servicio; no debe sumarse nuevamente.",
        "El costo de mano de obra por servicio se interpreta con una cuadrilla de 3 trabajadores a S/ 20 por hora cada uno.",
    ],
}

OBJETIVO_3 = {
    "nombre": "Evaluación ergonómica OWAS y estudio de tiempos",
    "antes": {
        "tiempo_estandar_min": 72.94,
        "horas_anuales": 765.87,
        "costo_servicio": 43.76,
        "costo_anual": 13785.66,
    },
    "despues": {
        "tiempo_estandar_min": 56.47,
        "horas_anuales": 592.94,
        "costo_servicio": 33.88,
        "costo_anual": 10672.83,
    },
    "servicios_anuales": 315,
    "tecnicos": 2,
    "costo_hora_tecnico": 18.0,
    "inversion": 2250.0,
    "costo_recurrente_anual": 150.0,
    "ahorro_bruto_anual": 3112.83,
    "beneficio_neto_anio1": 712.83,
    "roi_pct": 31.68,
    "bc": 1.30,
    "pri_meses": 9.11,
    "actividades": [
        {"actividad": "Preparación de herramientas", "antes": 9.41, "despues": 8.24, "categoria_owas": 1},
        {"actividad": "Manipulación de equipos", "antes": 14.12, "despues": 10.59, "categoria_owas": 2},
        {"actividad": "Instalación en zona baja", "antes": 21.18, "despues": 15.29, "categoria_owas": 4},
        {"actividad": "Ajuste de componentes", "antes": 11.76, "despues": 9.41, "categoria_owas": 1},
        {"actividad": "Fijación y verificación", "antes": 16.47, "despues": 12.94, "categoria_owas": 2},
    ],
    "owas_muestra": [
        {"registro": "R-001", "actividad": "Preparación de herramientas", "categoria": 1, "accion": "Mantener"},
        {"registro": "R-002", "actividad": "Manipulación de equipos", "categoria": 2, "accion": "Programar corrección"},
        {"registro": "R-003", "actividad": "Instalación en zona baja", "categoria": 4, "accion": "Intervención inmediata"},
        {"registro": "R-004", "actividad": "Ajuste de componentes", "categoria": 1, "accion": "Mantener"},
        {"registro": "R-005", "actividad": "Fijación de equipos", "categoria": 2, "accion": "Programar corrección"},
    ],
    "owas_frecuencias": {
        "espalda": [
            {"postura": "Recta", "frecuencia": 140},
            {"postura": "Doblada", "frecuencia": 140},
            {"postura": "Con giro", "frecuencia": 80},
            {"postura": "Doblada y girada", "frecuencia": 40},
        ],
        "brazos": [
            {"postura": "Ambos bajos", "frecuencia": 280},
            {"postura": "Un brazo elevado", "frecuencia": 100},
            {"postura": "Ambos elevados", "frecuencia": 20},
        ],
        "piernas": [
            {"postura": "De pie, ambas rectas", "frecuencia": 180},
            {"postura": "Una recta y otra flexionada", "frecuencia": 40},
            {"postura": "Ambas flexionadas", "frecuencia": 60},
            {"postura": "Ambas flexionadas y desequilibradas", "frecuencia": 20},
            {"postura": "Arrodillado", "frecuencia": 80},
            {"postura": "Caminando", "frecuencia": 20},
        ],
    },
    "alertas": [
        "La matriz OWAS disponible corresponde a la situación inicial; no se debe presentar como comparación OWAS antes/después.",
        "Las 400 observaciones posturales y los 50 ciclos del estudio de tiempos son muestras diferentes y deben mantenerse separadas.",
    ],
}

OBJETIVO_4 = {
    "nombre": "Control de inventarios mediante Kardex, ABC y conteo cíclico",
    "antes": {
        "eri_pct": 58.33,
        "diferencias_valorizadas": 1980.0,
        "herramientas_devueltas_pct": 33.3,
    },
    "despues": {
        "eri_pct": 100.0,
        "diferencias_valorizadas": 6.50,
        "herramientas_devuelta_pct": 70.0,
    },
    "meta_eri_pct": 90.0,
    "meta_eri_alternativa_pct": 95.0,
    "inversion": 204.0,
    "costo_recurrente_anual": 216.0,
    "reduccion_diferencias": 1973.50,
    "beneficio_neto_potencial_anio1": 1553.50,
    "diferencias_antes": [
        {"codigo": "EB-02", "item": "Electrobomba centrífuga 1 HP", "diferencia": 1, "precio": 620.0, "valor": 620.0},
        {"codigo": "HI-01", "item": "Tubería HDPE 2 pulgadas", "diferencia": 30, "precio": 14.0, "valor": 420.0},
        {"codigo": "HI-03", "item": "Perno galvanizado 5/8 pulgadas", "diferencia": 20, "precio": 2.5, "valor": 50.0},
        {"codigo": "EL-01", "item": "Cable sumergible 3x10 AWG", "diferencia": 50, "precio": 12.0, "valor": 600.0},
        {"codigo": "HE-03", "item": "Juego de llaves Stillson", "diferencia": 1, "precio": 290.0, "valor": 290.0},
    ],
    "diferencias_despues": [
        {"codigo": "HI-04", "item": "Codo PVC", "diferencia": 1, "precio": 6.5, "valor": 6.5},
    ],
    "alertas": [
        "La meta ERI aparece como 90% en la tabla de indicadores y como 95% en otra parte del desarrollo; requiere definición oficial.",
        "El 100% posterior corresponde a 12 de 12 registros dentro de la tolerancia de la clase ABC, no necesariamente a diferencia física cero.",
        "El beneficio neto es potencial: la reducción valorizada de diferencias de inventario no equivale automáticamente a flujo de caja.",
        "La tabla económica muestra S/ 426.50 como costo total del primer año incluyendo la diferencia residual de S/ 6.50; la suma inversión + recurrentes es S/ 420.00.",
    ],
}

OBJETIVOS = [OBJETIVO_1, OBJETIVO_2, OBJETIVO_3, OBJETIVO_4]
