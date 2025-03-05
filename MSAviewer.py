import streamlit as st
from pymsaviz import MsaViz, get_msa_testdata
import os

# Título de la aplicación
st.title("Visualización de Alineación multiple de secuencia")

# Permitir al usuario subir un archivo FASTA
uploaded_file = st.file_uploader("Sube un archivo FASTA", type=["fa", "fasta"])

# Determinar qué archivo usar
if uploaded_file is not None:
    # Guardar el archivo subido temporalmente
    msa_file = "uploaded_msa.fasta"
    with open(msa_file, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success("Archivo cargado con éxito")
else:
    # Usar el archivo de prueba por defecto si no se sube nada
    msa_file = get_msa_testdata("MRGPRG.fa")
    st.info("Usando archivo de prueba 'MRGPRG.fa' por defecto")

# Crear la visualización con MsaViz
mv = MsaViz(msa_file, start=1, end=180, wrap_length=60, show_consensus=True)

# Extraer posiciones con menos del 50% de identidad de consenso
pos_ident_less_than_50 = []
ident_list = mv._get_consensus_identity_list()
for pos, ident in enumerate(ident_list, 1):
    if ident <= 50:
        pos_ident_less_than_50.append(pos)

# Añadir marcadores
mv.add_markers([1])
mv.add_markers([10, 20], color="orange", marker="o")
mv.add_markers([30, (40, 50), 55], color="green", marker="+")
mv.add_markers(pos_ident_less_than_50, marker="x", color="blue")

# Añadir anotaciones de texto
mv.add_text_annotation((76, 102), "Gap Region", text_color="red", range_color="red")
mv.add_text_annotation((112, 123), "Gap Region", text_color="green", range_color="green")

# Guardar la visualización como imagen
fig_path = "api_example03.png"
mv.savefig(fig_path)

# Mostrar la imagen en Streamlit
st.image(fig_path, caption="Alineación Múltiple con Marcadores y Anotaciones")

# Botón para descargar la imagen
with open(fig_path, "rb") as file:
    st.download_button(
        label="Descargar visualización",
        data=file,
        file_name="api_example03.png",
        mime="image/png"
    )

# Limpiar archivo temporal si se usó uno subido
if uploaded_file is not None and os.path.exists(msa_file):
    os.remove(msa_file)
