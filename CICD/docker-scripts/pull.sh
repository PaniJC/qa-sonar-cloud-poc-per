#!/bin/bash
sudo echo pull new image
sudo aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 590183966112.dkr.ecr.us-east-1.amazonaws.com/poc-ec2-deploy
docker pull 590183966112.dkr.ecr.us-east-1.amazonaws.com/poc-ec2-deploy:Lasted
chmod +x ./docker-scripts/startup.sh