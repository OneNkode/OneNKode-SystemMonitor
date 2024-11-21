@echo off
set PACKAGES=psutil GPUtil setuptools
set COUNT=1
set TOTAL=3

echo Package installer for .:SS:. - SuperSpecs
echo Made by OneNKode
echo.
echo Installing required Python packages...

echo Press any key to proceed with the installation
pause >NUL

echo Starting package installation...
color 0A


setlocal enabledelayedexpansion
for %%P in (%PACKAGES%) do (
    echo [!COUNT!/%TOTAL%] Installing %%P...
echo Connecting to secure servers...
echo Downloading package %%P...

    python -m pip install %%P || (
        echo Error installing %%P. Exiting...
        exit /b 1
    )
    echo Installation successful! Moving to the next package...

    echo.
    set /a COUNT+=1
)

echo All installations completed! System secure. Press any key to continue...
color
pause >NUL
