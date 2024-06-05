#!/bin/bash
cd /home/ec2-user/CICD
chmod +x ./startup-script.sh
./startup-script.sh > deploy.log