FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ 'America/Sao_Paulo'
RUN echo $TZ > /etc/timezone
RUN apt-get update && \
    apt-get install -q -y locales \
      python3 \
      python3-pip \
      python3-setuptools \
      apache2 \
      libapache2-mod-wsgi-py3 \
#      postgresql-10 \
      python3-venv \
      nodejs

# Set locale
RUN echo "pt_BR.UTF-8 UTF-8" > /etc/locale.gen
RUN locale-gen pt_BR.UTF-8
RUN update-locale pt_BR.UTF-8
ENV LC_ALL pt_BR.UTF-8
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

# Create project directory and venv

ENV PROJECTSDIR=/srv/deploy
ENV PROJECTNAME=optrix

RUN mkdir $PROJECTSDIR
RUN cd $PROJECTSDIR
RUN mkdir $PROJECTNAME
RUN chown `whoami` $PROJECTNAME
RUN cd $PROJECTNAME
WORKDIR /srv/deploy/optrix
ADD . /srv/deploy/$PROJECTNAME
RUN rm -rf venv
RUN python3 -m venv venv
RUN . venv/bin/activate
RUN python3 -m pip install --upgrade pip # optional

# Install wq within venv
RUN python3 -m pip install wq


RUN pip install -r requirements.txt
# Start Django
RUN cd db && ./manage.py makemigrations
RUN cd db && ./manage.py migrate
# Apache setup
RUN ln -s $PROJECTSDIR/$PROJECTNAME/conf/$PROJECTNAME.conf /etc/apache2/sites-available/
RUN a2ensite $PROJECTNAME
RUN a2enmod expires
RUN service apache2 restart

#RUN rm app/js/lib
#RUN rm app/css/lib
#RUN ./deploy.sh 0.0.1

EXPOSE 80 3500
CMD ["apache2ctl", "-D", "FOREGROUND"]