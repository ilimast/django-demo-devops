@echo off
set CONTAINER_NAME=django_app
set IMAGE_NAME=django-app

echo Deteniendo contenedor si ya está corriendo...
docker stop %CONTAINER_NAME% 2>nul
docker rm %CONTAINER_NAME% 2>nul

echo Construyendo la imagen...
docker build -t %IMAGE_NAME% .

echo Iniciando el contenedor...
docker run -d --env-file .env.development -p 9095:8000 --name %CONTAINER_NAME% %IMAGE_NAME%

echo Contenedor en ejecución. Accede en http://localhost:9095/
pause
