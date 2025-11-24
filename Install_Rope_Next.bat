@echo off
if exist "activate.bat" (
    call activate.bat
)
git init
git remote add origin https://github.com/Alucard24/Rope.git
git pull origin
git checkout -f -b development origin/development
git reset --hard origin/development

git checkout -f -b main origin/main
git reset --hard origin/main

call Update_Rope_Next_Stable.bat

echo.
echo --------Installation Complete--------
echo.
echo You can now start the program by running the Start_Rope_Next_Stable.bat or Start_Rope_Next_Dev.bat file

pause