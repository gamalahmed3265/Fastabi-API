@echo off

echo  http://localhost:8000
cmd /k "conda activate yolo7 & uvicorn main:app --reload"

@REM pytest -v --disable-warnings

