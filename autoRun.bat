:loop 
start python PATH\readBot.py REM enter the path to the readBot.py file
timeout /t 300 /nobreak  REM the 300 is the amount of seconds it takes to update
goto :loop 