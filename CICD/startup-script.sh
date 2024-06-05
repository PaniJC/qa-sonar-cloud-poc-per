#!/bin/bash
mkdir -p ../app
echo "Clean old images and containers"
if [ -n "$(docker ps -aq)" ] # If exists images on EC2 
then 
    sudo docker rm $(docker kill $(docker ps -aq))
    sudo docker rmi $(docker images -q)
fi
chmod +x ./docker-scripts/pull.sh

## Get ECR Images
docker-scripts/pull.sh > getECR.log
docker-scripts/startup.sh > startup.log