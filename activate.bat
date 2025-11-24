@echo off

REM Verifica se esiste activate.bat
if exist ".\venv3.10\Scripts\activate.bat" (
    REM Chiama activate.bat per attivare l'ambiente virtuale
    call ".\venv3.10\Scripts\activate.bat"
) else (
    echo venv3.10\Scripts\activate.bat file not found.
)

REM Gestione della variabile PATH
if defined _OLD_PATH (
	set "PATH=%_OLD_PATH%"
) else (
	set "_OLD_PATH=%PATH%"
)

REM Gestione della variabile CUDA_PATH_V12_4
if defined _OLD_CUDA_PATH_V12_4 (
	set "CUDA_PATH_V12_4=%_OLD_CUDA_PATH_V12_4%"
) else (
	set "_OLD_CUDA_PATH_V12_4=%CUDA_PATH_V12_4%"
)

REM Gestione della variabile CUDA_PATH
if defined _OLD_CUDA_PATH (
	set "CUDA_PATH=%_OLD_CUDA_PATH%"
) else (
	set "_OLD_CUDA_PATH=%CUDA_PATH%"
)

REM Impostazione delle variabili d'ambiente
SET "ROPE_NEXT_ROOT=%~dp0"
SET "ROPE_NEXT_ROOT=%ROPE_NEXT_ROOT:~0,-1%"
SET "EXT_DEPENDENCIES=%ROPE_NEXT_ROOT%\ext_dependencies"
SET "CUDA_PATH_V12_4=%EXT_DEPENDENCIES%\CUDA\v12.4"
SET "CUDA_PATH=%CUDA_PATH_V12_4%"
SET "FFMPEG_PATH=%EXT_DEPENDENCIES%\ffmpeg\bin"
SET "PATH=%FFMPEG_PATH%;%CUDA_PATH%\libnvvp;%CUDA_PATH%\bin;%PATH%"