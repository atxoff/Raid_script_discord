@echo off
REM Vérifier si pip est installé
pip --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo pip n'est pas installé. Veuillez installer Python et pip avant de continuer.
    pause
    exit /b 1
)

REM Installer les packages à partir de requirements.txt
echo Installation des packages à partir de requirements.txt
pip install -r requirements.txt

REM Vérifier si l'installation a réussi
IF %ERRORLEVEL% EQU 0 (
    echo Les packages ont été installés avec succès.
) ELSE (
    echo Une erreur est survenue lors de l'installation des packages.
)

pause