FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -q -y locales \
      python3 \
      python3-pip \
      python3-setuptools \
      apache2 \
      libapache2-mod-wsgi-py3 \
      postgresql-10 \
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

RUN cd $PROJECTSDIR
RUN mkdir $PROJECTNAME
RUN chown `whoami` $PROJECTNAME
RUN cd $PROJECTNAME
WORKDIR $PROJECTDIR/$PROJECTNAME
RUN python3 -m venv venv
RUN . venv/bin/activate
RUN python3 -m pip install --upgrade pip # optional

# Install wq within venv
RUN python3 -m pip install wq
RUN wq start $PROJECTNAME .

ADD . /srv/deploy/$PROJECTNAME
RUN pip install -r requirements.txt