#!/bin/bash
mkdir -p ../app
echo "Clean old images and containers"
if [ -n "$(docker images -q)" ] # If exists images on EC2 
then
    echo "Stop container.."
    sudo docker stop $(docker ps -aq)
    echo "Delete  containers..." 
    sudo docker rm $(docker ps -aq)
    echo "Delete images"
    sudo docker rmi $(docker images -q)
fi
chmod +x ./docker-scripts/pull.sh

## Get ECR Images
echo "Get ECR Images..."
docker-scripts/pull.sh > getECR.log
echo "Start Docker Compose APP"
docker-scripts/startup.sh > startup.log