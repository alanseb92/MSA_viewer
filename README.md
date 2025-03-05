##MSA Viewer
Una aplicación simple en Streamlit para visualizar alineamientos múltiples de secuencias (MSA) en formato FASTA utilizando la librería pymsaviz. Permite cargar un archivo FASTA y muestra una visualización estática con opciones de descarga.

Características
Visualización de alineamientos múltiples de secuencias (MSA) desde archivos FASTA.
Uso de datos de prueba (MRGPRG.fa) por defecto si no se carga un archivo.
Descarga de la visualización como imagen PNG.
Desplegable en Streamlit Community Cloud.
Requisitos
Python 3.7 o superior
Dependencias listadas en requirements.txt
Instalación
Clona este repositorio:
bash

Collapse

Wrap

Copy
git clone https://github.com/tu_usuario/msa-viewer.git
cd msa-viewer
Crea un entorno virtual (opcional pero recomendado):
bash

Collapse

Wrap

Copy
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
Instala las dependencias:
bash

Collapse

Wrap

Copy
pip install -r requirements.txt
Uso
Ejecuta la aplicación localmente:
bash

Collapse

Wrap

Copy
streamlit run app.py
Se abrirá en tu navegador en http://localhost:8501.
Opciones:
Usa el archivo de prueba por defecto (MRGPRG.fa) para ver una visualización de ejemplo.
(Nota: Esta versión no permite cargar archivos personalizados; consulta versiones posteriores para esa funcionalidad).
Descarga la imagen generada haciendo clic en el botón "Descargar visualización".
Estructura del proyecto
app.py: Código principal de la aplicación Streamlit.
requirements.txt: Lista de dependencias necesarias.
Despliegue en Streamlit Community Cloud
Sube el repositorio a GitHub.
Ve a Streamlit Community Cloud e inicia sesión con tu cuenta de GitHub.
Crea una nueva app seleccionando este repositorio y especificando app.py como archivo principal.
Una vez desplegada, obtendrás un enlace público para acceder a la app.
Ejemplo de visualización
La aplicación genera una imagen como esta basada en MRGPRG.fa:

Rango: posiciones 1 a 180.
Longitud de envoltura: 60 caracteres.
Muestra consenso y marcadores predefinidos.
Dependencias
streamlit: Framework para la interfaz web.
pymsaviz: Librería para visualizar alineamientos múltiples.
Limitaciones
Solo muestra un archivo de prueba predefinido (MRGPRG.fa).
No permite cargar archivos FASTA personalizados (ver versiones posteriores para esta funcionalidad).
Contribuciones
¡Siéntete libre de abrir issues o enviar pull requests para mejorar esta aplicación!

Licencia
Este proyecto está bajo la Licencia MIT.
