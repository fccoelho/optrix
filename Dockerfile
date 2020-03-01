FROM ubuntu:latest

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ 'America/Sao_Paulo'

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN echo $TZ > /etc/timezone
RUN apt-get update && \
    apt-get install -q -y locales \
      python3 \
      python3-pip \
      python3-setuptools \
      gunicorn3 \
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
RUN mkdir -p $PROJECTSDIR/$PROJECTNAME/logs
RUN chown `whoami` $PROJECTNAME
RUN cd $PROJECTNAME
WORKDIR /srv/deploy/optrix

#create deploy user
RUN useradd -m deploy

ADD . /srv/deploy/$PROJECTNAME
RUN chown -R deploy:deploy $PROJECTSDIR/$PROJECTNAME
ENV VIRTUAL_ENV=$PROJECTSDIR/$PROJECTNAME/venv
RUN rm -rf venv
RUN python3 -m venv venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN . venv/bin/activate
RUN python3 -m pip install --upgrade pip # optional

# Install wq within venv
RUN python3 -m pip install wq


RUN pip install -r requirements.txt
#RUN gunicorn -v

RUN cd db && ./manage.py makemigrations
RUN cd db && ./manage.py migrate

EXPOSE 8000

USER deploy
