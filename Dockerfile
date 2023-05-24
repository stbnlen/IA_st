# Establecer la imagen base
FROM python:3.10-slim-buster

# Establecer el directorio de trabajo
WORKDIR /code

# Copiar los archivos de la aplicación
COPY . .

# Instalar los requerimientos
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto 8501 para la aplicación de Streamlit
EXPOSE 8501

# Establecer el comando por defecto
CMD ["streamlit", "run", "Pagina_Principal.py", "--server.enableCORS", "false"]