@echo off

if exist "activate.bat" (
    call activate.bat
)
python tools\simplify_dfm_onnx.py ./dfl_models_convert ./dfl_models --extension .dfm --dynamic_input morph_value:0