@echo off
title Kantin POS - Django
cd /d "%~dp0"
echo.
echo === KANTIN POS ===
echo Folder project: %CD%
echo.
py -m pip install -r requirements.txt
if errorlevel 1 (
  echo.
  echo Gagal memasang Django. Pastikan Python/py sudah terpasang dan internet aktif.
  pause
  exit /b 1
)
echo.
py manage.py check
if errorlevel 1 (
  echo.
  echo Ada error pada project. Baca pesan di atas.
  pause
  exit /b 1
)
echo.
py manage.py migrate
echo.
echo Membuka server Kantin POS...
echo Jangan tutup jendela ini selama website digunakan.
start "" http://127.0.0.1:8000/
py manage.py runserver
pause
