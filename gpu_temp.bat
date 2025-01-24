@echo off
echo Monitorando temperatura da CPU Intel Core i5-3570...
cd /d "C:\Users\diegorego\Downloads\openhardwaremonitor-v0.9.6" <-- Caminho correto para o OpenHardwareMonitor 
OpenHardwareMonitor.exe /minimize /silent /noSplash > temp.log


:: Filtrar as informações de temperatura da CPU e salvar em temp_output.txt
findstr /i "Intel" temp.log | findstr /i "Core" > temp_output.txt


echo Temperatura da CPU:
type temp_output.txt


:: Verificar se a temperatura excedeu 80°C
for /f "tokens=2 delims=;" %%a in ('findstr /i "Core" temp_output.txt') do set temp=%%a


if %temp% geq 80 (

   echo ALERTA: Temperatura da CPU esta muito alta! (%temp% °C)
 ) else (  
    echo Temperatura da CPU: %temp% °C
)


del temp.log
pause
