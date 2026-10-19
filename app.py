import streamlit as st

from catalogo import listar_especialidades, buscar_especialidades

st.set_page_config(
    page_title="Portal de Especialidades",
    page_icon="🎓",
    layout="wide",
)

st.title("Portal de Especialidades Técnicas")
st.write("Aprendemos, creamos e innovamos.")
st.subheader("Conoce nuestras especialidades")

consulta = st.text_input(
    "Buscar por nombre o descripción",
    placeholder="Ejemplo: programación",
)

if consulta:
    resultados = buscar_especialidades(consulta)
else:
    resultados = listar_especialidades()

if resultados:
    for item in resultados:
        with st.container(border=True):
            st.subheader(item["nombre"])
            st.write(item["descripcion"])
            st.caption(f"Nivel sugerido: {item['nivel']}")

else:
    st.warning("No se encontraron especialidades.")

st.divider()
st.caption("Proyecto académico de Lenguajes de Programación")