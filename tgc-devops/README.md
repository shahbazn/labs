# The Great Calculation

The Great Calculation - is a sample app to demonstrate DevOps strategies

## Deployment

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

* Base VM with Ubuntu Server 16.04 LTS
* VM specifications: RAM 1GB - vCPU 1 
* Security group rule to allow ingress traffic port 80

### Deployment Steps

* Launch a VM meeting above requirements
* SSH into your VM and follow the following steps
```
sudo apt-get update
sudo apt-get install git build-essential libssl-dev libffi-dev python-dev python-pip -y
git clone git@github.com:shahbazn/labs.git
cd ~/labs/tgc-devops
sudo pip install -r requirements.txt
cd configurations/ansible/
sudo ansible-playbook sandbox_setup.yml
sudo su - tgcapp
sudo docker-compose up -d --force-recreate # password for tgcapp is changeme
```

### Notes
* Default credentials for application user
```
Username: tgcapp
Password: changeme
```
