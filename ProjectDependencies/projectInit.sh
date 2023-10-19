#!/bin/bash

# install pip required to install python libaries
apt install pip -y 

cd ~/ProjectDependencies

# uses pip to install list of libaries
pip install -r requirements.txt