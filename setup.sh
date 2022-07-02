#!/bin/bash

sudo apt-get update -y
sudo apt-get upgrade -y

sudo apt-get install python3-pip -y

sudo pip3 install --upgrade setuptools

sudo apt-get install i2c-tools libgpiod-dev -y

pip3 install -r requirements.txt