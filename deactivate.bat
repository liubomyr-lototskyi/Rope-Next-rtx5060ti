@echo off

if exist "venv3.10\Scripts\deactivate.bat" (
    call "venv3.10\Scripts\deactivate.bat"
) else (
    echo venv3.10\Scripts\deactivate.bat file not found.
)

REM unset used variables
if defined _OLD_CUDA_PATH_V12_4 (
	set "CUDA_PATH_V12_4=%_OLD_CUDA_PATH_V12_4%"
	set "_OLD_CUDA_PATH_V12_4="
)

if defined _OLD_CUDA_PATH (
	set "CUDA_PATH=%_OLD_CUDA_PATH%"
	set "_OLD_CUDA_PATH="
)

REM Pulisci altre variabili
set "ROPE_NEXT_ROOT="
set "EXT_DEPENDENCIES="
set "FFMPEG_PATH="

REM Gestione della variabile PATH
set "_OLD_PATH="