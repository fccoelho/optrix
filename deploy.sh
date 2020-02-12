#!/bin/sh

# Exit on error
set -e

VERSION=$1;

if [ -z "$VERSION" ]; then
    echo "Usage: ./deploy.sh [VERSION]"
    exit 1
fi;

# (Re-)generate templates for all registered models
wq maketemplates \
     --django-dir db \
     --input-dir master_templates \
     --template-dir templates

# Regenerate JSON fixtures
./update_json.sh $VERSION;

cd app;
wq icons;


# Build javascript with wq.app
wq build $VERSION

# Force important files through any unwanted server caching
cd ../;
sed -i "s/optrix.js/optrix.js?v="$1"/" htdocs-build/optrix.appcache
sed -i "s/optrix.css/optrix.css?v="$1"/" htdocs-build/optrix.appcache

# Preserve Django's static files (e.g. admin)
if [ -d htdocs/static ]; then
    cp -a htdocs/static htdocs-build/static
fi;

# Replace existing htdocs with new version
rm -rf htdocs;
mv -i htdocs-build/ htdocs;


# Restart Django
touch db/optrix/wsgi.py

