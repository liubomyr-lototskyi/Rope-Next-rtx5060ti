@echo off
set CUDA_PATH=%CUDA_PATH_V11_8%
if exist "tensorrt-engines" rmdir "tensorrt-engines"
if not exist "tensorrt-engines-cu118" mkdir "tensorrt-engines-cu118"
mklink /D tensorrt-engines tensorrt-engines-cu118
call conda activate Rope && python Rope.py 
pause