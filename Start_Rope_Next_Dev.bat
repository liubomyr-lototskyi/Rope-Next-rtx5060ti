if exist "activate.bat" (
    call activate.bat
)
git checkout -f development
python Rope.py
pause