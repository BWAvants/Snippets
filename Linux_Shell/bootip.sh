#!/bin/bash

# Runs after network established via systemd

IPS=`hostname -I`

if [ -z $IPS ]
  then
    exit 68
fi

WIFI=""

for IP in $IPS
do
  if [ $IP != "10.250.250.2" ] && [ $IP != "10.250.250.3" ]
  then
    WIFI=$IP
  fi
done

if [ -z $WIFI ]
then
  echo "0.0.0.0" > /var/old.ips
  exit 225
fi

EMAIL=$(cat /home/pi/email.address)
echo "IP Report On Boot"
SSID=`iwgetid --raw`
BODY="NETWORK: $SSID \n\t$WIFI"
echo -e "$BODY"
echo -e "$BODY" | /usr/bin/mail -s "RasPi IP Report" $EMAIL
echo $WIFI > /var/old.ips

exit 0
