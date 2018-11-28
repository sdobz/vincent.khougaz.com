#!/bin/bash

echo Ensuring awscli is installed
sudo apt install awscli

echo Checking secret credentials
if [ ! -f aws.secret]; then
    echo "Missing aws.secret file"
    exit 1
fi

aws configure set preview.cloudfront true
