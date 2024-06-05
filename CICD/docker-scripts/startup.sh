#!/bin/bash
cd docker-scripts
sudo mv docker-compose.yml ../../app/
cd ../../app/
sudo docker-compose up -d