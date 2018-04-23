#tunnel through
ssh -i /Users/colinbrochard/.aws/colinbrochard.pem ec2-user@ec2-18-218-168-126.us-east-2.compute.amazonaws.com

ssh -i /Users/colinbrochard/.aws/colinbrochard.pem ec2-user@ec2-18-219-201-191.us-east-2.compute.amazonaws.com

#send files to

$scp -i /Users/colinbrochard/.aws/colinbrochard.pem <data> ec2-18-219-201-191.us-east-2.compute.amazonaws.com

# pull from
$scp $scp -i /Users/colinbrochard/.aws/colinbrochard.pem ec2-18-219-201-191.us-east-2.compute.amazonaws.com/<data> <local path>



#!/bin/bash
HOME=/home/ec2-user
touch $HOME/.bootstrap-start
# Update & Install packages
sudo yum -y update
sudo yum -y install tmux
# Download and install Anaconda
wget -S -T 10 -t 5 \
  https://repo.continuum.io/archive/Anaconda3-5.1.0-Linux-x86_64.sh \
  -O $HOME/anaconda.sh
bash $HOME/anaconda.sh -b -p $HOME/anaconda
rm $HOME/anaconda.sh
chown -R ec2-user:ec2-user $HOME/anaconda
export PATH=$HOME/anaconda/bin:$PATH
# Add Anaconda to path
echo -e "\n\n# Anaconda3" >> $HOME/.bashrc
echo "export PATH=$HOME/anaconda/bin:$PATH" >> $HOME/.bashrc
touch $HOME/.bootstrap-end
