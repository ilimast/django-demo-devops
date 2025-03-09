# Dockerfile

FROM python:3.11-slim

# Instalar dependencias necesarias
RUN apt-get update && apt-get install -y libpq-dev gcc

# Configurar el directorio de trabajo
WORKDIR /app

# Instalar dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar la aplicación
COPY . .

# Hacer el script ejecutable
RUN chmod +x entrypoint.sh

# Ejecutar el script de inicio
CMD ["sh", "/app/entrypoint.sh"]
