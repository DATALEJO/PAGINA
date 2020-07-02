FROM ubuntu

ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update
#ENV PYTHONUNBUFFERED 1
RUN apt-get install -y apt-utils vim curl apache2 apache2-utils
RUN apt-get -y install python3 libapache2-mod-wsgi-py3
RUN apt-get install nano
#RUN apt-get install ps
RUN ln /usr/bin/python3 /usr/bin/python
RUN apt-get -y install python3-pip
RUN ln /usr/bin/pip3 /usr/bin/pip
RUN pip install --upgrade pip
RUN pip install django ptvsd
RUN pip install djangorestframework
RUN pip install django-cors-headers
ADD ./demo_site.conf /etc/apache2/sites-available/000-default.conf
EXPOSE 80 3500 443
CMD ["apache2ctl", "-D", "FOREGROUND"]
