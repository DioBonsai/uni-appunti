@echo off
rem Apre il Quaderno di ripasso come sito locale (http://127.0.0.1:8765). Si puo' chiudere questa finestra.
cd /d "%~dp0"
start "" "C:\Users\admin\AppData\Local\Programs\Python\Python312\pythonw.exe" "_sistema\pagina_studio\serve.py"
