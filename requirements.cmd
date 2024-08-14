@echo off
echo Package installer for .:SS:. - SuperSpecs
echo Made by NDXCode
echo.
echo Installing required Python packages...

echo Press any key to proceed with the installation
pause >NUL

echo Starting package installation...

echo [1/3] Installing psutil...
python -m pip install psutil
echo Done!
echo.

echo [2/3] Installing GPUtil...
python -m pip install GPUtil
echo Done!
echo.

echo [3/3] Installing Setuptools...
python -m pip install setuptools
echo Done!
echo.

echo Installations finished, press any key to continue.
pause >NUL