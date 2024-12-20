@echo off

REM Check if an argument is provided
if "%1"=="" (
    echo "Provide a script to run. Usage: statify [init|compile|templates]"
    exit /b
)

REM Run a specific Python script based on the first argument
if /i "%1"=="compile" (
    python "%~dp0compile.py"
) else if /i "%1"=="init" (
    python "%~dp0init.py" %2
) else if /i "%1"=="templates" (
    python "%~dp0templates.py"
) else (
    echo "Unknown script. Usage: statify [init|compile|templates]"
    exit /b
)
