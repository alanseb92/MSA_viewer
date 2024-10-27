import streamlit as st # type: ignore
from pymsaviz import MSAViz
from Bio import AlignIO

# Configuración de la app
st.title("Visualización de Alineamiento Múltiple con pyMSAviz")
st.write("Cargar y visualizar un archivo de alineamiento múltiple en formato FASTA.")

# Cargar el archivo de secuencias MSA
uploaded_file = st.file_uploader("Sube un archivo FASTA para alineamiento", type="fasta")

if uploaded_file is not None:
    # Cargar el alineamiento
    alignment = AlignIO.read(uploaded_file, "fasta")

    # Visualizar el alineamiento con pyMSAviz
    viz = MSAViz(alignment)
    fig = viz.plot(show=False)

    # Mostrar en Streamlit
    st.pyplot(fig)
