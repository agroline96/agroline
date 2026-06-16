
import base64
import time
import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
from urllib.parse import quote

st.set_page_config(page_title="Agroline", layout="wide")
GA_ID = "G-34PEPJNC3B"

components.html(
    f"""
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={GA_ID}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());
      gtag('config', '{GA_ID}');
    </script>
    """,
    height=0,
)
st.markdown("""
<style>
.block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
}


</style>
""", unsafe_allow_html=True)


fondos = [
    "imagenes/fondo1.png",
    
]

fondo_actual = fondos[int(time.time() / 10) % len(fondos)]
with open(fondo_actual, "rb") as img:
    fondo_base64 = base64.b64encode(img.read()).decode()
with open("imagenes/agroline_logo_limpio.png", "rb") as logo:
    logo_base64 = base64.b64encode(logo.read()).decode()

st.markdown(
    f"""
    <div style="
        height:300px;
        background-image:url('data:image/jpg;base64,{fondo_base64}');
        background-size:cover;
        background-position:center;
        border-radius:10px;
        position:relative;
        overflow:hidden;
    ">
        <img src="data:image/png;base64,{logo_base64}" style="
            position:absolute;
            left:-20px;
            bottom:-60px;
            width:250px;
        ">
    </div>
    """,
    unsafe_allow_html=True
)


st.markdown("""
<style>
.stApp {
    background-color: #F5F8F4;
}

.block-container {
    padding-top: 0rem;
    padding-bottom: 0rem;
}


</style>
""", unsafe_allow_html=True)

st.markdown("""

<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

[data-testid="stToolbar"] {
    display: none;
}

[data-testid="stDecoration"] {
    display: none;
}

section[data-testid="stSidebar"] {
    display: none;
}

button[kind="header"] {
    display: none;
}
@media (max-width: 768px) {

    .encabezado-productos {
        padding: 10px !important;
        font-size: 14px !important;
    }

    .encabezado-productos h3 {
        font-size: 18px !important;
        margin: 0 !important;
    }

}

@media (max-width: 768px) {



    .stMarkdown {
        color: #222222 !important;
    }

    p, span, div {
        font-size: 14px !important;
    }

    button {
        font-size: 14px !important;
    }

}

</style>

""", unsafe_allow_html=True)
col_logo, col_wp = st.columns([3, 1])

with col_logo:
    st.markdown("<div style='margin-top:20px'></div>", unsafe_allow_html=True)
    st.markdown("""
<h3 style='color:#2D5D36;'>
Más de 20 años de experiencia en repuestos agricolas
</h3>

<p style='font-size:16px; color:#666; margin-bottom:0px;'>
Correas • Cuchillas • Cadenas • Rodamientos • Cardanes
</p>
<p style='font-size:16px; color:#666;'>
Para cosechadoras, sembradoras e industrias
</p>

""", unsafe_allow_html=True)
st.markdown("""
<p style='font-size:18px;
          color:#F58220;
          font-weight:bold;
          margin-top:15px;'>
🌿 REPRESENTANTE OFICIAL STIHL
</p>
""", unsafe_allow_html=True)



st.link_button("🟢 WhatsApp", "https://wa.me/5493537585428")
st.link_button("📸 Instagram", "https://www.instagram.com/agroline.ferreteria")
st.link_button("📍Ubicacion","https://www.google.com/maps/place/Belgrano+855,+X2550+Bell+Ville,+C%C3%B3rdoba/@-32.6413207,-62.6958088,17z/data=!4m15!1m8!3m7!1s0x95cbfbacf6561f81:0x7ccbbc8b53ecdfc2!2sBelgrano+855,+X2550+Bell+Ville,+C%C3%B3rdoba!3b1!8m2!3d-32.6413252!4d-62.6932339!16s%2Fg%2F11thrb95qf!3m5!1s0x95cbfbacf6561f81:0x7ccbbc8b53ecdfc2!8m2!3d-32.6413252!4d-62.6932339!16s%2Fg%2F11thrb95qf?entry=ttu&g_ep=EgoyMDI2MDYwMy4xIKXMDSoASAFQAw%3D%3D")

st.markdown("📍 Dirección :Belgrano 855     🏢 Localidad:  Bell Ville-Cordoba       ✉️ Mail: agrolineferreteria@gmail.com ")

archivo = "catalogo.xlsx"

@st.cache_data
def cargar_hoja(nombre_hoja):
    return pd.read_excel(archivo, sheet_name=nombre_hoja)

excel = pd.ExcelFile(archivo)
st.markdown("""
<style>
div[data-testid="stVerticalBlock"]:has(h3) {
    gap: 0rem;
}
</style>
""", unsafe_allow_html=True)
st.divider()

st.divider()

st.markdown("## 🏆 Algunas de nuestras marcas")

logos = [
    "skf.png",
    "stihl.png",
    "ew.png",
    "ibaf.png",
    "barrax.png",
    "peer.png",
    "duter.png",
    "ingersoll.png",
]

cols = st.columns(1)

for i, logo in enumerate(logos):
    with cols[i % 1]:
        st.image(f"./imagenes/logos/{logo}", width=80)

st.markdown("## 📁 Categorías")

categorias = [
    "Correas para cosechadoras",
    "Correas A-B-C y Kevlar",
    "Rodamientos y retenes",
    "Cadenas linea ASA",
    "Poda y jardineria Stihl",
    "Niveladoras para sembradora",
    "Secciones-puntones-barras armadas-accesorios",
    "Baterias",
    "Poleas-engranajes-mazas",
    "Mangueras-abrazaderas y acoples polipropileno",
    "Horquillas y trilobulares",
    "Tubos telescopicos y acoples",
    "Tanques",
    "Gato para lanza",
    "Calzado de trabajo",
    "LISTA COMPLETA",
]
categoria = st.selectbox(
    "Seleccioná una categoría",
    categorias
)



if categoria.lower() == "secciones-puntones-barras armadas-accesorios":
    hojas_marca = [
        "ACCESORIOS BARRA CORTE",
        "BARRAS DE CORTE ARMADAS",
        "SECCIONES DE CORTE",
        "PUNTONES"
    ]
if categoria.lower() == "correas cosechadoras":

    marca = st.selectbox(
        "Seleccioná marca",
        ["Todas", "John Deere", "Case", "New Holland", "Massey Ferguson", "Vassalli"]
    )

    if marca == "Todas":
        hojas_marca = [
            h for h in excel.sheet_names
            if any(x in h.lower() for x in [
                "john",
                "case",
                "new holland",
                "massey",
                "vassalli"
            ])
        ]
    else:
        hojas_marca = [
            h for h in excel.sheet_names
            if marca.lower().replace(" ", "-") in h.lower()
            or marca.lower().split()[0] in h.lower()
        ]

else:
    if categoria == "Lista completa":
        hojas_marca = ["LISTA COMPLETA"]

    elif categoria == "Correas para cosechadoras":
        hojas_marca = [
        "CORREAS B",
        "CORREAS C",
        "CORREAS KEVLAR"
    ]
            
        

    else:
        hojas_marca = [categoria]

if hojas_marca:
    if categoria == "Correas para cosechadoras":
        hojas_marca = [
            "CASE 1688",
            "CASE 2166",
            "CASE 2188",
            "CASE 2366",
            "CASE 2388",
            "CASE 2399",
            "CASE 2688",
            "CASE 2799",
            "CASE 4130",
            "CASE 5130",
            "CASE 7010",
            "CASE 7088",
            "CASE 7120",
            "CASE 7230",
            "CASE 7250",
            "CASE 8010",
            "CASE 8120",
            "CASE 8230",
            "CASE 9010",
            "CASE 9120",
            "CASE 9230",
            "CASE 9250",
            "CLAAS MEDION 320",
            "CLAAS MEDION 330",
            "CLAAS MEDION 340",
            "CLAAS MEGA 350",
            "CLAAS MEGA 360",
            "CLAAS MEGA 370",
            "CLAAS TUCANO 470",
            "CLAAS TUCANO 570",
            "CLAAS TUCANO 580",
            "CLAS JAGUAR 820",
            "CLAS LEXION 600",
            "DON ROQUE 125",
            "DON ROQUE 150",
            "JOHN DEERE 1075",
            "JOHN DEERE 1165",
            "JOHN DEERE 1175",
            "JOHN DEERE 1185",
            "JOHN DEERE 1450",
            "JOHN DEERE 1470",
            "JOHN DEERE 1550",
            "JOHN DEERE 1570",
            "JOHN DEERE 9470",
            "JOHN DEERE 9500",
            "JOHN DEERE 9510",
            "JOHN DEERE 9570",
            "JOHN DEERE 9600",
            "JOHN DEERE 9610",
            "JOHN DEERE 9870",
            "JOHN DEERE 9550",
            "JOHN DEERE 9660",
            "JOHN DEERE 9670",
            "JOHN DEERE 9680",
            "JOHN DEERE 9860",
            "MASSEY FERGUSON 32",
            "MASSEY FERGUSON 34",
            "MASSEY FERGUSON 3640",
            "MASSEY FERGUSON 38",
            "MASSEY FERGUSON 5650",
            "MASSEY FERGUSON 6845",
            "MASSEY FERGUSON 8780",
            "MASSEY FERGUSON 6855",
            "MASSEY FERGUSON 9690",
            "MASSEY FERGUSON 9790",
            "MASSEY FERGUSON 9895",
            "NEW HOLLAND 8040",
            "NEW HOLLAND 8055",
            "NEW HOLLAND CR 5.85",
            "NEW HOLLAND CR 6080",
            "NEW HOLLAND CR 8050",
            "NEW HOLLAND CR 8060",
            "NEW HOLLAND CR 8080",
            "NEW HOLLAND CR 8090",
            "NEW HOLLAND CR 9060",
            "NEW HOLLAND CR 9080",
            "NEW HOLLAND CS 660",
            "NEW HOLLAND TC 5070",
            "NEW HOLLAND TC 5090",
            "NEW HOLLAND TC 55",
            "NEW HOLLAND TC 57",
            "NEW HOLLAND TC 59",
            "NEW HOLLAND TR 98",
            "NEW HOLLAND TX 68",
            
    ]
        hoja = st.selectbox("Seleccioná modelo", hojas_marca)
        df = cargar_hoja(hoja)

    else:
        mapa_hojas = {
    "Lista completa": "LISTA COMPLETA",
    "Rodamientos y retenes": ["RETENES", "RODAMIENTOS"],
    "Correas A-B-C y Kevlar": [
    "CORREAS A",
    "CORREAS B",
    "CORREAS C",
    "CORREAS KEVLAR"
], 
    "Cadenas linea ASA": "CADENAS SIMPLES-REFORZ.-DOBLES",
    "Poda y jardineria Stihl": "STIHL",
    "Niveladoras para sembradora": "NIVELADORAS TOSSOLINI",
    "Secciones-puntones-barras armadas-accesorios": [
    "SECCIONES DE CORTE",
    "PUNTONES",
    "BARRAS DE CORTE ARMADAS",
    "ACCESORIOS BARRA CORTE"
],
    "Baterias": "BATERIA STRONG LIFE",
    "Poleas-engranajes-mazas": ["MAZAS", "ENGRANAJES", "POLEA FUNDICION"],
    "Mangueras-abrazaderas y acoples polipropileno": [
    "ABRAZADERAS ESTANDAR",
    "ACOPLE POLIPROPILENO",
    "MANGUERAS",
    "ABRAZADERA ALTA RESISTENCIA"
],
    "Horquillas y trilobulares": "CAÑO TRILOBULAR",
    "Tubos telescopicos y acoples": "TUBO FLEXIBLE",
    "Tanques": "TANQUES",
    "Gato para lanza": "GATOS",
    "Calzado de trabajo": "CALZADO",
}
        

        hoja = mapa_hojas.get(categoria, categoria)

if isinstance(hoja, list):
    df = pd.concat(
        [pd.read_excel(archivo, sheet_name=h) for h in hoja],
        ignore_index=True
    )
else:
    df = pd.read_excel(archivo, sheet_name=hoja)
   

st.markdown(
    "<h3 style='color:#25D366;'>🔎 Buscar repuestos</h3>",
    unsafe_allow_html=True
)

busqueda = st.text_input(
    "",
    placeholder="Ej: correa, cuchilla, JD 1175, Gates..."
)


if busqueda:
    texto = busqueda.strip().lower()

    filtro = df.astype(str).apply(
        lambda columna: columna.str.lower().str.contains(texto, na=False)
    ).any(axis=1)

    df = df[filtro]
st.markdown(
    f"<h4 style='color:#25D366;'>📦 Productos encontrados: {len(df)}</h4>",
    unsafe_allow_html=True
)
df.columns = df.columns.astype(str).str.strip().str.upper()

df = df.rename(columns={
    "DESCRIPCIÓN": "DESCRIPCION",
    "APLICACION": "APLICACION-MEDIDA",
    "APLICACIÓN": "APLICACION-MEDIDA",
    "APLICACIÓN MEDIDA": "APLICACION-MEDIDA",
    "APLICACION MEDIDA": "APLICACION-MEDIDA",
})
columnas = ["CODIGO", "DESCRIPCION", "APLICACION-MEDIDA", "MARCA"]

df = df[[col for col in columnas if col in df.columns]]

df = df.astype(str)

col0, col1, col2, col3, col4, col5 = st.columns([1.5, 2, 5, 4, 2, 2.4])

col1.markdown("<h4 style='color:white; background:#25D366; padding:10px; text-align:center;'>Código</h4>", unsafe_allow_html=True)

col2.markdown("<h4 style='color:white; background:#25D366; padding:10px; text-align:center;'>Descripción</h4>", unsafe_allow_html=True)

col3.markdown("<h4 style='color:white; background:#25D366; padding:10px; text-align:center;'>Aplicación</h4>", unsafe_allow_html=True)

col4.markdown("<h4 style='color:white; background:#25D366; padding:10px; text-align:center;'>Marca</h4>", unsafe_allow_html=True)
col5.markdown(
    """
    <div style="
        background-color:#4CAF50;
        color:white;
        text-align:center;
        padding:10px;
        font-weight:bold;
        border-radius:2px;
    ">
        Stock
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()
st.markdown("""
<div style="overflow-x:auto; width:100%;">
""", unsafe_allow_html=True)
for i, fila in df.iterrows():
    col0, col1, col2, col3, col4, col5 = st.columns([1.5, 2, 5, 4, 2, 2.4])

    foto = str(fila.get("FOTO", "")).strip()

    if foto and foto.lower() != "nan":
        ruta_imagen = f"imagenes/{foto}"
        
        try:
            col0.image(ruta_imagen, width=120)

            if col0.button("Ver foto", key=f"foto_{i}"):
                st.image(ruta_imagen, width=600)

        except:
           col0.write("")
    else:
        col0.write("")
       
    col1.markdown(f"<div style='text-align:center'>{fila.get('CODIGO','')}</div>", unsafe_allow_html=True)
    col2.markdown(f"<div style='text-align:center'>{fila.get('DESCRIPCION','')}</div>", unsafe_allow_html=True)
    col3.markdown(f"<div style='text-align:center'>{fila.get('APLICACION-MEDIDA','')}</div>", unsafe_allow_html=True)
    col4.markdown(f"<div style='text-align:center'>{fila.get('MARCA','')}</div>", unsafe_allow_html=True)

    mensaje = f"Hola, quiero consultar por el stock y precio del producto {fila.get('CODIGO','')} - {fila.get('DESCRIPCION','')}"
    mensaje = quote(mensaje)
    url_wp = f"https://wa.me/5493537585428?text={mensaje}"

    col5.markdown(f'<a href="{url_wp}" target="_blank" style="background-color:#25D366; color:white; padding:8px 15px; border-radius:8px; text-decoration:none; font-weight:bold; display:inline-block; text-align:center;">CONSULTAR STOCK</a>', unsafe_allow_html=True)

