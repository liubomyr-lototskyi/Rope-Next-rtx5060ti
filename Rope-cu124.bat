@echo off
set CUDA_PATH=%CUDA_PATH_V12_4%
if exist "tensorrt-engines" rmdir "tensorrt-engines"
if not exist "tensorrt-engines-cu124" mkdir "tensorrt-engines-cu124"
mklink /D tensorrt-engines tensorrt-engines-cu124
call conda activate Rope-cu124 && python Rope.py 
pause