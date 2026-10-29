Write-Host "Checking Windows Application Control permissions for Python DLLs..."
Get-ChildItem -Path "$PSScriptRoot\venv313\Lib\site-packages\torch\lib\*.dll" -ErrorAction SilentlyContinue | Unblock-File
Write-Host "Starting AgriGen AI Backend & Frontend..."
Start-Process powershell -ArgumentList "-NoExit -Command `"cd '$PSScriptRoot\backend'; ..\venv313\Scripts\python.exe -m uvicorn main:app --reload --port 8000`""
Start-Process powershell -ArgumentList "-ExecutionPolicy Bypass -NoExit -Command `"cd '$PSScriptRoot\frontend'; npm.cmd run dev`""
Write-Host "Backend and Frontend servers launching..."
