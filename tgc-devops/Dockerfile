FROM python:2.7

MAINTAINER Shahbaz Nazir "shahbaznazir1992@gmail.com"

# Copying the requirements for installation to take
# advantage of the caching.
COPY tgc/ /tgc/
COPY setup.py /
COPY requirements.txt /
RUN pip install -r /requirements.txt
RUN python setup.py install

EXPOSE 8080
