#!/bin/bash

if [ "$EUID" -ne 0 ]
    then echo "Veuillez lancer init en tant que root"
    exit
fi
dnf install -y python3 python3-pip
pip install -r ./requirement.txt
useradd monit -s /bin/sh -u 2000
groupadd monit
usermod -aG monit monit
pip install -r ./requirement.txt
mkdir -p /etc/monit/conf.d /var/monit /var/log/monit
cp ./conf/conf.json ./conf/api_conf.json /etc/monit/conf.d/
cp ./app/api.py ./app/monit.py /var/monit/
cp ./monit.service ./monit.timer /etc/systemd/system/
chown -R monit:monit /etc/monit/conf.d /var/monit /var/log/monit /etc/systemd/system/monit.*
systemctl daemon-reload
systemctl enable monit.timer
systemctl start monit.timer