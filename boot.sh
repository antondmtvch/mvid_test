#!/bin/bash
app="mvid"
docker build -t ${app} .
docker run -d -p 5000:80 --name=${app} -v $PWD/data:/var/www/mvid/data ${app}
