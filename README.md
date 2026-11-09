# Dashboard de Gestión de Operaciones – Corporación Rehobot

Dashboard integrado desarrollado con Python, Streamlit, Pandas y Plotly.

## 1. Requisitos
- Windows 10/11
- Python 3.10 o superior
- Visual Studio Code

## 2. Abrir el proyecto
1. Descomprime `dashboard_rehobot.zip`.
2. Abre Visual Studio Code.
3. Selecciona **Archivo > Abrir carpeta**.
4. Selecciona la carpeta `dashboard_rehobot`.

## 3. Crear entorno virtual (recomendado)
Abre la terminal integrada de VS Code y ejecuta:

```bash
python -m venv .venv
```

Activar en Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Si usas CMD:

```cmd
.venv\Scripts\activate
```

## 4. Instalar librerías

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## 5. Ejecutar el dashboard

```bash
python -m streamlit run app.py
```

Se abrirá el dashboard en el navegador. Si no se abre automáticamente, copia la dirección local que aparece en la terminal (normalmente http://localhost:8501).

## 6. Archivos principales
- `app.py`: interfaz y gráficos del dashboard.
- `data.py`: datos auditados de los cuatro objetivos.
- `requirements.txt`: librerías necesarias.

## 7. Actualizar datos
Cuando cambies las cifras en el Excel, actualiza los valores equivalentes en `data.py`.
No cambies los valores de forma aislada en `app.py`: los gráficos y KPIs toman sus datos desde `data.py`.

## 8. Criterios de auditoría incorporados
- Objetivo 1: se deja la distancia propuesta pendiente de validación.
- Objetivo 2: se muestra ahorro por servicio y punto de equilibrio; no se anualiza sin volumen anual confirmado.
- Objetivo 3: se muestran los 315 servicios/año y la evaluación económica anual registrada.
- Objetivo 4: se separa la reducción valorizada de diferencias de inventario del flujo de caja; meta ERI pendiente de confirmar (90% o 95%).
