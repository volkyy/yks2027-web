@echo off
REM YKS2027 WEB - Windows Quick Start Script
REM Bu script uygulamayi Windows'ta hizlica baslatir

echo ============================================================
echo YKS2027 WEB - Hizli Baslatma Script
echo ============================================================
echo.

REM Check if virtual environment exists
if not exist "venv\Scripts\activate.bat" (
    echo [INFO] Sanal ortam bulunamadi, olusturuluyor...
    python -m venv venv
    if errorlevel 1 (
        echo [ERROR] Sanal ortam olusturma hatasi!
        pause
        exit /b 1
    )
    echo [INFO] Sanal ortam olusturuldu.
)

REM Activate virtual environment
echo [INFO] Sanal ortam aktif ediliyor...
call venv\Scripts\activate.bat

REM Install/upgrade pip
echo [INFO] Pip guncelleniyor...
python -m pip install --upgrade pip --quiet

REM Check if requirements are installed
echo [INFO] Bagimliliklar kontrol ediliyor...
pip show flask >nul 2>&1
if errorlevel 1 (
    echo [INFO] Bagimliliklar yukleniyor...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo [ERROR] Bagimlilik yukleme hatasi!
        pause
        exit /b 1
    )
)

REM Create instance directory if not exists
if not exist "instance" mkdir instance

REM Check if .env exists
if not exist ".env" (
    echo [INFO] .env dosyasi bulunamadi, .env.example kopyalaniyor...
    copy .env.example .env
)

echo.
echo ============================================================
echo Uygulama baslatiliyor...
echo ============================================================
echo.
echo Erisim Adresi: http://localhost:5000
echo Durdurmak icin: Ctrl+C
echo.

REM Start the application
python run.py

pause
