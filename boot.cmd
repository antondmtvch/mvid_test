set app=mvid
set curdir=%~dp0

docker stop %app%
docker rm %app%

docker build -t %app% .
docker run -p 5000:80 --name=%app% -v "%curdir%\data":/var/www/mvid/data %app%