@echo off
rem Apre il Quaderno di ripasso come sito locale (http://127.0.0.1:8765). Si puo' chiudere questa finestra.
cd /d "%~dp0"
where pythonw >nul 2>nul && (start "" pythonw "_sistema\pagina_studio\serve.py" & exit /b)
where pyw >nul 2>nul && (start "" pyw "_sistema\pagina_studio\serve.py" & exit /b)
if exist "%LOCALAPPDATA%\Programs\Python\Python312\pythonw.exe" (start "" "%LOCALAPPDATA%\Programs\Python\Python312\pythonw.exe" "_sistema\pagina_studio\serve.py" & exit /b)
echo Python non trovato: installalo da python.org e rilancia.
pause
