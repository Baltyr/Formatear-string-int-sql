@echo off
SET SCRIPT_NAME=number_formatter.py
SET EXEC_NAME=FormateadorNumeros

echo ===============================
echo Verificando PyInstaller...
echo ===============================
python -m pip show pyinstaller >nul 2>&1
IF ERRORLEVEL 1 (
    echo PyInstaller no esta instalado. Instalando...
    python -m pip install pyinstaller
)

echo ===============================
echo Compilando el ejecutable .exe...
echo ===============================
python -m PyInstaller --noconfirm --windowed --icon=icono.ico --name=%EXEC_NAME% %SCRIPT_NAME%

echo ===============================
echo ¡Compilación terminada!
echo Ejecutable en: dist\%EXEC_NAME%\%EXEC_NAME%.exe
echo ===============================
pause
