# Resultados de Encuesta sobre Inteligencia Artificial en Biblioteca

Esta aplicación de Streamlit muestra los resultados de una encuesta realizada a las bibliotecas chilenas sobre el uso de la inteligencia artificial en sus actividades. Proporciona una visualización interactiva de los datos recopilados y permite explorar las respuestas obtenidas.

## Requisitos

Antes de ejecutar la aplicación, asegúrate de tener instaladas las siguientes dependencias:

- Python 3.7 o superior
- Las bibliotecas especificadas en el archivo requirements.txt

Puedes instalar todas las dependencias mediante el siguiente comando:

```
pip install -r requirements.txt
```

## Instrucciones de ejecución

Sigue los pasos a continuación para ejecutar la aplicación:

1. Clona este repositorio en tu máquina local.
2. Navega hasta la carpeta del proyecto.

```
cd IA_st
```

4. Asegúrate de haber instalado todas las dependencias mencionadas en el archivo requirements.txt.
5. Ejecuta el siguiente comando para iniciar la aplicación:

```
streamlit run Pagina_Principal.py
```

6. Se abrirá una ventana del navegador con la aplicación de Streamlit, donde podrás interactuar y explorar los resultados de la encuesta.

## Archivo docker-compose

Además de la instalación manual, también puedes utilizar Docker para ejecutar la aplicación. Este repositorio incluye un archivo docker-compose.yml que facilita la configuración del entorno de ejecución.

Sigue los pasos a continuación para ejecutar la aplicación con Docker:

1. Asegúrate de tener Docker instalado en tu máquina local.
2. Clona este repositorio en tu máquina local.
3. Navega hasta la carpeta del proyecto.

```
cd IA_st
```

4. Ejecuta el siguiente comando para construir y ejecutar los contenedores:

```
docker-compose up -d
```

5. Una vez que los contenedores estén en ejecución, podrás acceder a la aplicación a través de tu navegador web en http://localhost:8501.