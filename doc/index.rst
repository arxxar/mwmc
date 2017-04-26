================
EC2 Installation
================

sudo yum update

-----------
Dynamic DNS
-----------

http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dynamic-dns.html

::

  sudo yum-config-manager --enable epel
  sudo yum install -y noip
  sudo chkconfig noip on
  chkconfig --list noip
  sudo service noip start

http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-hostname.html

::

  sudo vi /etc/sysconfig/network
  sudo reboot

-----------------
Mount Data Volume
-----------------

http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-using-volumes.html

::

  lsblk

  NAME    MAJ:MIN RM SIZE RO TYPE MOUNTPOINT
  xvda    202:0    0   8G  0 disk
  └─xvda1 202:1    0   8G  0 part /
  xvdb    202:16   0  32G  0 disk


  sudo file -s /dev/xvdb
  sudo mkfs -t ext4 /dev/xvdb
  sudo mkdir /minecraft
  sudo mount /dev/xvdb /minecraft
  sudo chown ec2-user:ec2-user /minecraft
  sudo file -s /dev/xvdb
  sudo vi /etc/fstab
  sudo mount -a
  sudo reboot

https://www.spigotmc.org/wiki/buildtools/

::

  sudo yum install git
  mkdir /minecraft/BuildTools
  cd /minecraft/BuildTools

  wget -O BuildTools.jar https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar

  git config --global --unset core.autocrlf
  java -jar BuildTools.jar

http://minecraft.gamepedia.com/Tutorials/Server_startup_script

::

  cd /minecraft
  cp BuildTools/spigot*.jar spigot.jar

  wget -O minecraft "http://minecraft.gamepedia.com/Tutorials/Server_startup_script/Script?action=raw"

  vi minecraft
  sudo cp minecraft /etc/init.d/minecraft-alfa
  sudo vi /etc/init.d/minecraft-alfa
  sudo chmod a+x /etc/init.d/minecraft-alfa
  sudo chkconfig --add minecraft-alfa
  sudo ntsysv
  sudo service minecraft-alfa start
  vi /minecraft/eula.txt




xxx
Apache
Overviewer
