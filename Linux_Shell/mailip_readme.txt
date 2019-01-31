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

place the bootip.sh file in /home/pi and make it executable
  sudo chmod +x /home/pi/bootip.sh
  
place the bootip.service file in /etc/systemd/system and make enable it
  sudo systemctl daemon-reload
  sudo systemctl enable bootip

modify the root chrontable to check regularly and update as necessary
  sudo crontab -e
    0 * * * * sh /usr/bin/mailip &
    0 0 * * 0 /sbin/shutdown -r +5 Weekly Reboot

create the file /home/pi/email.address to specify recipient (example will email itself)
[for multiple recipients, put them all on one line seperated by a space... it is best not to remove the self email as a backup]
  nano /home/pi/email.address
    robinsonlabiot@gmail.com

change the finger information "Full Name" for root so emails are "FROM" an identifiable source
  sudo chfn -f "Email Sender Name" root
