Set up Linux to periodically check for changes in the primary IP address and email a designated address with the new IP.

sudo apt-get install ssmtp
sudo apt-get install mailutils

make a backup of the /etc/ssmtp/ssmtp.conf file
  sudo mv /etc/ssmtp/ssmtp.conf /etc/ssmtp/ssmtp.conf.bak

create new ssmtp.conf file in its place
  sudo nano /etc/ssmtp/ssmtp.conf
    root=postmaster
    mailhub=smtp.gmail.com:587
    hostname=raspberrypi
    AuthUser=robinsonlabiot@gmail.com
    AuthPass=TheGmailPassword
    AuthMethod=LOGIN
    FromLineOverride=YES
    UseTLS=Yes
    UseSTARTTLS=YES

place the 'mailip' file in /usr/bin and make it executable
  sudo chmod +x /usr/bin/mailip

modify the root chrontable to check regularly and update as necessary
  sudo crontab -e
    @reboot echo "0.0.0.0" > /var/old.ips ; sh /usr/bin/mailip &
    0 * * * * sh /usr/bin/mailip &
    0 0 * * 0 /sbin/shutdown -r +5 Weekly Reboot

create the file /home/pi/email.address to specify recipient
  nano /home/pi/email.address
    sendto@email.com
