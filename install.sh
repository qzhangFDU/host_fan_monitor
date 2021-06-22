#!/bin/bash

apt-get -y install python3-pip
pip3 install pynvml --proxy=http://10.176.51.14:3128 
chmod +x ./monitor_host_fan.sh
chmod +x ./ipmicfg
cp ./monitor_host_fan.sh /etc/init.d/
cp ./ipmicfg /usr/local/bin/
cp ./monitor.py /usr/local/bin/
cd /etc/init.d/
sudo update-rc.d monitor_host_fan.sh defaults 90

