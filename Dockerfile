FROM python:2.7

MAINTAINER Shahbaz Nazir "shahbaznazir1992@gmail.com"

# Copying the requirements for installation to take
# advantage of the caching.
COPY tgc/ /tgc/
RUN pip install -r /tgc/requirements.txt
RUN pip install /tgc

EXPOSE 8000
