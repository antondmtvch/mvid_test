set app=mvid
set curdir=%~dp0

docker stop %app%
docker rm %app%

rem Обязательный шаг!
python %curdir%\dataset2hd5.py

if %errorlevel% neq 0 (
    exit /b %errorlevel%
) else (
    docker build -t %app% .
    docker run -p 5000:80 --name=%app% -v "%curdir%\data":/var/www/mvid/data %app%
)