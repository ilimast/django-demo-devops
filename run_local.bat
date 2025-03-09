@echo off
setlocal

REM Definir variables
set VENV_DIR=.venv
set PYTHON=%VENV_DIR%\Scripts\python.exe
set PIP=%VENV_DIR%\Scripts\pip.exe

REM Verificar si el entorno virtual existe, si no, crearlo
if not exist %VENV_DIR% (
    echo Creando el entorno virtual...
    python -m venv %VENV_DIR%
)

REM Activar el entorno virtual
echo Activando el entorno virtual...
call %VENV_DIR%\Scripts\activate

REM Instalar dependencias si es necesario
echo Instalando dependencias desde requirements.txt...
%PIP% install --upgrade pip
%PIP% install -r requirements.txt

REM Ejecutar las migraciones y correr el servidor
echo Ejecutando migraciones...
%PYTHON% manage.py makemigrations
%PYTHON% manage.py migrate

echo Iniciando el servidor Django en http://127.0.0.1:9095/
%PYTHON% manage.py runserver 0.0.0.0:9095

endlocal
