# Product.
[![Build Status](https://api.travis-ci.org/m-babar/api_project.png?branch=master)](https://api.travis-ci.org/m-babar/api_project)



It's django basic project
###### Basically implement Django ORM, Ajax request, template inheritance etc.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites
Python version : python3.6
###### python installtion in ubuntu machine
**sudo add-apt-repository ppa:jonathonf/python-3.6**
**sudo apt-get update**
**sudo apt-get install python3.6**

**sudo apt-get update**
**sudo apt-get install python3.6**

###### Install virtualenv
**sudo apt-get install python3-pip**
**sudo pip3 install virtualenv**

###### Python installtion in windows machine.
https://www.python.org/downloads/

**Install virtual envoirment**

###### Installing
1. clone from repository

**git clone https://github.com/nishuk0007/product_app_repo.git**

2. create virtualenvoirment

**virtualenv --python=python3.6 product_env**

3. Activate virtual envoirment

**source product_env/bin/activate**

4. Install python dependancy packages.
Note, requirments.txt file present in project root direcotry


**pip install -r requirments.txt**

5. start project below command.

**python manage.py runserver**

6. Copy this URL on your browsers tab 

**http://127.0.0.1:8000/**

7. Check test cases put below command on your terminal

**python manage.py test product.tests.model_test**

**python manage.py test product.tests.view_test -k**

## project Video
https://drive.google.com/open?id=1SK21LF-1VnsUrGT74i67-MCcT6dSiZNt
