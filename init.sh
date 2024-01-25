#!/bin/bash

if [ "$EUID" -ne 0 ]
    then echo "Veuillez lancer init en tant que root"
    exit
fi
useradd monit -m -s /bin/sh -u 2000
groupadd monit
usermod -aG monit monit
pip install -r /requirement.txt
mkdir -p /var/log/monit
mkdir -p /etc/monit/conf.d
mkdir -p /var/monit
chown -R monit:monit /var/log/monit
chown -R monit:monit /etc/monit/conf.d
chown -R monit:monit /var/monit
cp /conf/conf.json /etc/monit/conf.d/
cp /conf/api_conf.json /etc/monit/conf.d/