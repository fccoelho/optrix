#!/bin/sh

set -e

VERSION=$1;

# Dump wq configuration object to file

db/manage.py dump_config --format amd > app/js/data/config.js


# Compile templates into fixture
cd app;
wq collectjson

# Update version.txt
if [ "$VERSION" ]; then
    wq setversion $VERSION
    
fi;


cd ..;
