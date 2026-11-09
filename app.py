import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

from data import OBJETIVO_1, OBJETIVO_2, OBJETIVO_3, OBJETIVO_4

st.set_page_config(
    page_title="Dashboard Corporación Rehobot",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Paleta visual
AZUL = "#183B56"
CELESTE = "#4F9DA6"
VERDE = "#2E8B57"
NARANJA = "#E09F3E"
ROJO = "#C44536"
GRIS = "#64748B"

st.markdown("""
<style>
    .main {background-color: #F5F7FA;}
    .block-container {padding-top: 1.4rem; padding-bottom: 2rem;}
    div[data-testid="stMetric"] {
        background: white; border: 1px solid #E5EAF0;
        padding: 14px 16px; border-radius: 12px;
    }
    .section-note {
        background: #EEF4F8; padding: 12px 16px; border-radius: 10px;
        border-left: 4px solid #4F9DA6; margin-bottom: 12px;
    }
</style>
""", unsafe_allow_html=True)


def money(value):
    return f"S/ {value:,.2f}"


def pct(value):
    return f"{value:.2f}%"


def metric_row(items):
    cols = st.columns(len(items))
    for col, (label, value, delta) in zip(cols, items):
        col.metric(label, value, delta)


def show_alerts(alerts):
    if alerts:
        with st.expander("Observaciones y criterios de interpretación", expanded=False):
            for alert in alerts:
                st.warning(alert)


def comparison_bar(title, labels, before, after, y_title):
    df = pd.DataFrame({
        "Indicador": labels * 2,
        "Escenario": ["Antes"] * len(labels) + ["Después"] * len(labels),
        "Valor": before + after,
    })
    fig = px.bar(
        df, x="Indicador", y="Valor", color="Escenario", barmode="group",
        text_auto=".2f", title=title,
        color_discrete_map={"Antes": ROJO, "Después": VERDE},
    )
    fig.update_layout(
        yaxis_title=y_title, xaxis_title="", legend_title="",
        plot_bgcolor="white", paper_bgcolor="white",
        margin=dict(l=10, r=10, t=55, b=10),
    )
    st.plotly_chart(fig, use_container_width=True)


def economic_table(rows):
    st.dataframe(pd.DataFrame(rows), use_container_width=True, hide_index=True)


st.sidebar.title("Corporación Rehobot")
st.sidebar.caption("Business Intelligence · Gestión de operaciones")
st.sidebar.markdown("---")
st.sidebar.info(
    "Dashboard construido con los datos auditados del archivo Excel. "
    "Los supuestos y datos pendientes se identifican en cada módulo."
)

st.title("📊 Dashboard de Gestión de Operaciones")
st.caption("Corporación Rehobot | Comparación AS IS vs. TO BE | Evaluación técnica y económica")

tabs = st.tabs([
    "Resumen general",
    "Objetivo 1 · Almacén",
    "Objetivo 2 · POE y 5S",
    "Objetivo 3 · OWAS y tiempos",
    "Objetivo 4 · Inventarios",
])

# ---------------------------------------------------------------------
# RESUMEN GENERAL
# ---------------------------------------------------------------------
with tabs[0]:
    st.subheader("Panel ejecutivo")
    st.markdown(
        '<div class="section-note">Vista consolidada de los cuatro objetivos. '
        'Los beneficios económicos no se suman en un único total porque incluyen '
        'ahorros laborales, beneficios condicionados a volumen de servicios y '
        'reducciones valorizadas de diferencias de inventario.</div>',
        unsafe_allow_html=True,
    )

    metric_row([
        ("Objetivos desarrollados", "4", "4 módulos"),
        ("Inversión inicial registrada", money(434 + 290 + 2250 + 204), "Suma de inversiones"),
        ("Objetivos con comparación AS IS / TO BE", "4 de 4", "Información disponible"),
        ("Objetivo con PRI documentado", "2", "Objetivos 1 y 3"),
    ])

    st.markdown("### Comparación de indicadores principales")
    resumen = pd.DataFrame([
        {"Objetivo": "O1 · Preparación", "Indicador": "Tiempo por preparación", "Antes": 85, "Después": 60, "Unidad": "min"},
        {"Objetivo": "O2 · Mantenimiento", "Indicador": "Tiempo de ciclo", "Antes": 371.25, "Después": 288, "Unidad": "min"},
        {"Objetivo": "O3 · Ergonomía", "Indicador": "Tiempo estándar", "Antes": 72.94, "Después": 56.47, "Unidad": "min"},
        {"Objetivo": "O4 · Inventarios", "Indicador": "ERI", "Antes": 58.33, "Después": 100, "Unidad": "%"},
    ])
    st.dataframe(resumen, use_container_width=True, hide_index=True)

    c1, c2 = st.columns(2)
    with c1:
        tiempos = resumen[resumen["Unidad"] == "min"].copy()
        fig = px.bar(
            tiempos, x="Objetivo", y=["Antes", "Después"], barmode="group",
            title="Tiempos operativos: antes y después (min)",
            color_discrete_map={"Antes": ROJO, "Después": VERDE},
        )
        fig.update_layout(plot_bgcolor="white", paper_bgcolor="white")
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        eri = pd.DataFrame([
            {"Escenario": "Antes", "ERI (%)": OBJETIVO_4["antes"]["eri_pct"]},
            {"Escenario": "Después", "ERI (%)": OBJETIVO_4["despues"]["eri_pct"]},
        ])
        fig = px.bar(
            eri, x="Escenario", y="ERI (%)", text_auto=".1f",
            title="Exactitud del inventario (Objetivo 4)",
            color="Escenario",
            color_discrete_map={"Antes": ROJO, "Después": VERDE},
        )
        fig.update_layout(yaxis_range=[0, 110], showlegend=False,
                          plot_bgcolor="white", paper_bgcolor="white")
        st.plotly_chart(fig, use_container_width=True)

    c3, c4 = st.columns(2)
    with c3:
        fin = pd.DataFrame([
            {"Objetivo": "O1", "Inversión inicial": 434},
            {"Objetivo": "O2", "Inversión inicial": 290},
            {"Objetivo": "O3", "Inversión inicial": 2250},
            {"Objetivo": "O4", "Inversión inicial": 204},
        ])
        fig = px.bar(
            fin, x="Objetivo", y="Inversión inicial", text_auto=".2f",
            title="Inversión inicial por objetivo",
            color="Objetivo",
        )
        fig.update_layout(showlegend=False, plot_bgcolor="white", paper_bgcolor="white")
        st.plotly_chart(fig, use_container_width=True)
    with c4:
        st.markdown("**Lectura del panel**")
        st.write("Los tres primeros objetivos comparan tiempos operativos. El cuarto utiliza ERI, que es un indicador porcentual de exactitud de inventario; por eso se grafica por separado.")

    st.markdown("### Resultados económicos por objetivo")
    economic_table([
        {"Objetivo": "1 · Almacén", "Inversión": money(434), "Beneficio reportado": money(46), "Naturaleza": "Beneficio neto año 1", "PRI": "10.85 meses"},
        {"Objetivo": "2 · POE y 5S", "Inversión": money(290), "Beneficio reportado": money(83.25), "Naturaleza": "Ahorro por servicio", "PRI": "No calculable sin volumen anual"},
        {"Objetivo": "3 · OWAS y tiempos", "Inversión": money(2250), "Beneficio reportado": money(712.83), "Naturaleza": "Beneficio neto año 1", "PRI": "9.11 meses"},
        {"Objetivo": "4 · Inventarios", "Inversión": money(204), "Beneficio reportado": money(1553.50), "Naturaleza": "Beneficio potencial año 1", "PRI": "No calculado"},
    ])
    st.caption("No sumar directamente los beneficios reportados: sus horizontes y naturalezas económicas son diferentes.")


# ---------------------------------------------------------------------
# OBJETIVO 1
# ---------------------------------------------------------------------
with tabs[1]:
    d = OBJETIVO_1
    st.subheader("Objetivo 1 · Optimización del almacén y preparación de recursos")
    metric_row([
        ("Tiempo antes", f'{d["antes"]["tiempo_min"]:.0f} min', None),
        ("Tiempo después", f'{d["despues"]["tiempo_min"]:.0f} min', "-25 min"),
        ("Reducción del tiempo", pct((1-d["despues"]["tiempo_min"]/d["antes"]["tiempo_min"])*100), None),
        ("Inversión inicial", money(d["inversion"]), None),
    ])

    c1, c2 = st.columns(2)
    with c1:
        comparison_bar(
            "Tiempo por preparación",
            ["Tiempo (min)"],
            [d["antes"]["tiempo_min"]],
            [d["despues"]["tiempo_min"]],
            "Minutos",
        )
    with c2:
        comparison_bar(
            "Costo por preparación",
            ["Costo (S/)"],
            [d["antes"]["costo_servicio"]],
            [d["despues"]["costo_servicio"]],
            "S/",
        )
    abc = pd.DataFrame(d["abc_resumen"])
    fig = px.pie(
        abc, names="clase", values="valor", hole=0.48,
        title="Distribución del valor anual ABC (resumen)",
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Evaluación económica")
    economic_table([
        {"Concepto": "Costo por preparación", "Antes": money(d["antes"]["costo_servicio"]), "Después": money(d["despues"]["costo_servicio"])},
        {"Concepto": "Costo mensual", "Antes": money(d["antes"]["costo_mensual"]), "Después": money(d["despues"]["costo_mensual"])},
        {"Concepto": "Costo anual", "Antes": money(d["antes"]["costo_anual"]), "Después": money(d["despues"]["costo_anual"])},
        {"Concepto": "Ahorro mensual", "Antes": "—", "Después": money(d["ahorro_mensual"])},
        {"Concepto": "Ahorro anual", "Antes": "—", "Después": money(d["ahorro_anual"])},
        {"Concepto": "Beneficio neto año 1", "Antes": "—", "Después": money(d["beneficio_neto_anio1"])},
    ])
    metric_row([
        ("Ahorro por preparación", money(10), None),
        ("Ahorro anual", money(d["ahorro_anual"]), None),
        ("PRI", f'{d["pri_meses"]:.2f} meses', None),
        ("B/C simple", f'{d["ahorro_anual"]/d["inversion"]:.2f}', None),
    ])
    st.markdown("### Distancias y layout")
    st.info(
        "La distancia inicial registrada es 120 m. La distancia TO BE se mantiene "
        "pendiente de validación para no mostrar un dato contradictorio del layout."
    )
    show_alerts(d["alertas"])


# ---------------------------------------------------------------------
# OBJETIVO 2
# ---------------------------------------------------------------------
with tabs[2]:
    d = OBJETIVO_2
    st.subheader("Objetivo 2 · Estandarización del mantenimiento mediante POE y 5S")
    reduccion = (1 - d["despues"]["tiempo_min"] / d["antes"]["tiempo_min"]) * 100
    mejora_5s = d["despues"]["cumplimiento_5s"] - d["antes"]["cumplimiento_5s"]
    metric_row([
        ("Tiempo antes", f'{d["antes"]["tiempo_min"]:.2f} min', None),
        ("Tiempo después", f'{d["despues"]["tiempo_min"]:.0f} min', f'-{d["antes"]["tiempo_min"]-d["despues"]["tiempo_min"]:.2f} min'),
        ("Reducción de tiempo", pct(reduccion), None),
        ("Inversión POE", money(d["inversion"]), None),
    ])
    c1, c2 = st.columns(2)
    with c1:
        comparison_bar(
            "Tiempo de ciclo del servicio",
            ["Tiempo (min)"],
            [d["antes"]["tiempo_min"]],
            [d["despues"]["tiempo_min"]],
            "Minutos",
        )
    with c2:
        df5s = pd.DataFrame([
            {"Escenario": "Antes", "Cumplimiento": d["antes"]["cumplimiento_5s"]},
            {"Escenario": "Después", "Cumplimiento": d["despues"]["cumplimiento_5s"]},
        ])
        fig = px.bar(
            df5s, x="Escenario", y="Cumplimiento", text_auto=".1f",
            title="Cumplimiento de metodología 5S",
            color="Escenario",
            color_discrete_map={"Antes": ROJO, "Después": VERDE},
        )
        fig.update_layout(yaxis_title="Cumplimiento (%)", yaxis_range=[0, 100],
                          showlegend=False, plot_bgcolor="white", paper_bgcolor="white")
        st.plotly_chart(fig, use_container_width=True)

    comparison_bar(
        "Costo de mano de obra por servicio",
        ["Costo (S/)"],
        [d["antes"]["costo_servicio"]],
        [d["despues"]["costo_servicio"]],
        "S/",
    )

    st.markdown("### Evaluación económica por servicio")
    economic_table([
        {"Concepto": "Costo de mano de obra por servicio", "Antes": money(d["antes"]["costo_servicio"]), "Después": money(d["despues"]["costo_servicio"])},
        {"Concepto": "Costo de actividades NVA", "Antes": money(d["antes"]["costo_nva"]), "Después": money(d["despues"]["costo_nva"])},
        {"Concepto": "Ahorro total por servicio", "Antes": "—", "Después": money(d["ahorro_por_servicio"])},
        {"Concepto": "Ahorro NVA incluido en el total", "Antes": "—", "Después": money(d["ahorro_nva_incluido"])},
        {"Concepto": "Inversión inicial POE", "Antes": "—", "Después": money(d["inversion"])},
    ])
    metric_row([
        ("Mejora 5S", f"+{mejora_5s:.0f} puntos porcentuales", None),
        ("Ahorro por servicio", money(d["ahorro_por_servicio"]), None),
        ("Punto de equilibrio", f'{d["punto_equilibrio_servicios"]} servicios', None),
        ("Costo residual NVA", money(d["despues"]["costo_nva"]), None),
    ])
    st.info(
        "El punto de equilibrio es la cantidad mínima de servicios necesaria para "
        "recuperar la inversión de S/ 290 con un ahorro de S/ 83.25 por servicio. "
        "No se calcula ROI ni PRI anual porque falta el volumen anual de servicios."
    )
    show_alerts(d["alertas"])


# ---------------------------------------------------------------------
# OBJETIVO 3
# ---------------------------------------------------------------------
with tabs[3]:
    d = OBJETIVO_3
    st.subheader("Objetivo 3 · Evaluación ergonómica OWAS y estudio de tiempos")
    reduccion = (1 - d["despues"]["tiempo_estandar_min"] / d["antes"]["tiempo_estandar_min"]) * 100
    metric_row([
        ("Tiempo estándar antes", f'{d["antes"]["tiempo_estandar_min"]:.2f} min', None),
        ("Tiempo estándar después", f'{d["despues"]["tiempo_estandar_min"]:.2f} min', f'-{d["antes"]["tiempo_estandar_min"]-d["despues"]["tiempo_estandar_min"]:.2f} min'),
        ("Reducción", pct(reduccion), None),
        ("Servicios anuales", f'{d["servicios_anuales"]:,}', "Proyección"),
    ])
    actividades = pd.DataFrame(d["actividades"])
    fig = px.bar(
        actividades, x="actividad", y=["antes", "despues"], barmode="group",
        title="Tiempo estándar por actividad: antes y después",
        labels={"value": "Minutos", "actividad": "Actividad", "variable": "Escenario"},
        color_discrete_map={"antes": ROJO, "despues": VERDE},
    )
    fig.update_layout(xaxis_tickangle=-25, plot_bgcolor="white", paper_bgcolor="white")
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Evaluación económica anual")
    economic_table([
        {"Concepto": "Costo anual de mano de obra", "Antes": money(d["antes"]["costo_anual"]), "Después": money(d["despues"]["costo_anual"])},
        {"Concepto": "Inversión inicial", "Antes": "—", "Después": money(d["inversion"])},
        {"Concepto": "Costo recurrente anual", "Antes": "—", "Después": money(d["costo_recurrente_anual"])},
        {"Concepto": "Ahorro bruto anual", "Antes": "—", "Después": money(d["ahorro_bruto_anual"])},
        {"Concepto": "Beneficio neto primer año", "Antes": "—", "Después": money(d["beneficio_neto_anio1"])},
    ])
    metric_row([
        ("ROI", pct(d["roi_pct"]), None),
        ("Relación B/C", f'{d["bc"]:.2f}', None),
        ("PRI", f'{d["pri_meses"]:.2f} meses', None),
        ("Beneficio neto año 1", money(d["beneficio_neto_anio1"]), None),
    ])

    st.markdown("### Distribución de posturas observadas – situación inicial")
    st.caption("Las frecuencias posturales suman 400 observaciones y corresponden a la evaluación inicial.")
    sub1, sub2, sub3 = st.tabs(["Espalda", "Brazos", "Piernas"])
    for subtab, key, title in [
        (sub1, "espalda", "Frecuencia de posturas de espalda"),
        (sub2, "brazos", "Frecuencia de posturas de brazos"),
        (sub3, "piernas", "Frecuencia de posturas de piernas"),
    ]:
        with subtab:
            df = pd.DataFrame(d["owas_frecuencias"][key])
            fig = px.bar(df, x="postura", y="frecuencia", text_auto=True, title=title)
            fig.update_layout(xaxis_tickangle=-25, plot_bgcolor="white", paper_bgcolor="white")
            st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Registros OWAS representativos")
    st.dataframe(pd.DataFrame(d["owas_muestra"]), use_container_width=True, hide_index=True)
    st.caption("La tabla muestra los cinco registros representativos de la matriz, no la distribución completa de las 400 observaciones.")
    show_alerts(d["alertas"])


# ---------------------------------------------------------------------
# OBJETIVO 4
# ---------------------------------------------------------------------
with tabs[4]:
    d = OBJETIVO_4
    st.subheader("Objetivo 4 · Control de inventarios mediante Kardex, ABC y conteo cíclico")
    metric_row([
        ("ERI antes", pct(d["antes"]["eri_pct"]), None),
        ("ERI después", pct(d["despues"]["eri_pct"]), f"+{d['despues']['eri_pct']-d['antes']['eri_pct']:.2f} pp"),
        ("Diferencias antes", money(d["antes"]["diferencias_valorizadas"]), None),
        ("Diferencias después", money(d["despues"]["diferencias_valorizadas"]), None),
    ])

    c1, c2 = st.columns(2)
    with c1:
        df_eri = pd.DataFrame([
            {"Escenario": "Antes", "ERI": d["antes"]["eri_pct"]},
            {"Escenario": "Después", "ERI": d["despues"]["eri_pct"]},
            {"Escenario": "Meta consignada", "ERI": d["meta_eri_pct"]},
        ])
        fig = px.bar(
            df_eri, x="Escenario", y="ERI", text_auto=".1f",
            title="Exactitud del registro de inventario (ERI)",
            color="Escenario",
            color_discrete_map={"Antes": ROJO, "Después": VERDE, "Meta consignada": NARANJA},
        )
        fig.update_layout(yaxis_title="ERI (%)", yaxis_range=[0, 110],
                          showlegend=False, plot_bgcolor="white", paper_bgcolor="white")
        st.plotly_chart(fig, use_container_width=True)
    with c2:
        df_dif = pd.DataFrame([
            {"Escenario": "Antes", "Valor": d["antes"]["diferencias_valorizadas"]},
            {"Escenario": "Después", "Valor": d["despues"]["diferencias_valorizadas"]},
        ])
        fig = px.bar(
            df_dif, x="Escenario", y="Valor", text_auto=".2f",
            title="Valor de diferencias de inventario",
            color="Escenario",
            color_discrete_map={"Antes": ROJO, "Después": VERDE},
        )
        fig.update_layout(yaxis_title="S/", showlegend=False,
                          plot_bgcolor="white", paper_bgcolor="white")
        st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Evaluación económica")
    economic_table([
        {"Concepto": "Diferencias valorizadas", "Antes": money(d["antes"]["diferencias_valorizadas"]), "Después": money(d["despues"]["diferencias_valorizadas"])},
        {"Concepto": "Reducción valorizada", "Antes": "—", "Después": money(d["reduccion_diferencias"])},
        {"Concepto": "Inversión inicial", "Antes": "—", "Después": money(d["inversion"])},
        {"Concepto": "Costos recurrentes anuales", "Antes": "—", "Después": money(d["costo_recurrente_anual"])},
        {"Concepto": "Beneficio neto potencial año 1", "Antes": "—", "Después": money(d["beneficio_neto_potencial_anio1"])},
    ])
    metric_row([
        ("Reducción valorizada", money(d["reduccion_diferencias"]), None),
        ("Inversión inicial", money(d["inversion"]), None),
        ("Costo recurrente", money(d["costo_recurrente_anual"]), "Anual"),
        ("Beneficio neto potencial", money(d["beneficio_neto_potencial_anio1"]), "Primer año"),
    ])

    st.markdown("### Detalle de diferencias valorizadas")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("**Antes de la mejora**")
        st.dataframe(pd.DataFrame(d["diferencias_antes"]), use_container_width=True, hide_index=True)
    with col2:
        st.markdown("**Después de la mejora**")
        st.dataframe(pd.DataFrame(d["diferencias_despues"]), use_container_width=True, hide_index=True)

    st.info(
        f"Meta ERI utilizada provisionalmente: {d['meta_eri_pct']:.0f}%. "
        f"El Excel también menciona {d['meta_eri_alternativa_pct']:.0f}%; "
        "debe confirmarse cuál es la meta oficial."
    )
    show_alerts(d["alertas"])

st.markdown("---")
st.caption(
    "Fuente: archivo Excel de desarrollo del Proyecto Final GEESOP de Corporación Rehobot. "
    "Cifras transcritas de las hojas de los cuatro objetivos y sujetas a validación de las observaciones indicadas."
)
