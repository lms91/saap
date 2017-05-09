#!/bin/sh

create_env() {
    # check if file exists
    if [ -f "/var/interlegis/saap/data/secret.key" ]; then
        KEY=`cat /var/interlegis/saap/data/secret.key`
    else
        KEY=`python3 genkey.py`
        echo $KEY > data/secret.key
    fi

    # TODO: rename env-test-bash to .env
    FILENAME="/var/interlegis/saap/saap/.env"

    if [ -z "${DATABASE_URL:-}" ]; then
        DATABASE_URL="postgresql://saap:saap@saapdb:5432/saap"
    fi

    # ALWAYS replace the content of .env variable
    # If want to conditionally create only if absent then use IF below
    #    if [ ! -f $FILENAME ]; then

    touch $FILENAME

    # explicitly use '>' to erase any previous content
    echo "SECRET_KEY="$KEY > $FILENAME
    # now only appends
    echo "DATABASE_URL = "$DATABASE_URL >> $FILENAME
    echo "DEBUG = ""${DEBUG-True}" >> $FILENAME
    echo "EMAIL_USE_TLS = ""${USE_TLS-True}" >> $FILENAME
    echo "EMAIL_PORT = ""${EMAIL_PORT-587}" >> $FILENAME
    echo "EMAIL_HOST = ""${EMAIL_HOST-''}" >> $FILENAME
    echo "EMAIL_HOST_USER = ""${EMAIL_HOST_USER-''}" >> $FILENAME
    echo "EMAIL_HOST_PASSWORD = ""${EMAIL_HOST_PASSWORD-''}" >> $FILENAME
}

echo "creating .env file..."
create_env
echo "done."

# # python3 gen-env.py

python3 manage.py bower install

/bin/sh busy-wait.sh $DATABASE_URL

python3 manage.py migrate
python3 manage.py collectstatic --no-input

/bin/sh gunicorn_start.sh