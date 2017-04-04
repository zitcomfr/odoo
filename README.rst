ZIT.COM odoo project
====================

.. image:: https://api.travis-ci.org/zitcomfr/odoo.svg?branch=master
    :target: https://travis-ci.org/zitcomfr/odoo
    :alt: Travis state


A way to start to setup postgresql with postgis is to use docker. I you have
docker installed then you can run the following command to start it::

    docker run --name pg_zitcom -d \
        -e POSTGRES_PASSWORD=zitcom \
        -e POSTGRES_USER=zitcom \
        -e POSTGRES_DB=odoo -p 5427:5432 \
        mdillon/postgis:9.6-alpine

if you needs your data to be persistent do not to setup volume properly!

The you can use buildout-pg_in_docker.cfg file to properly set odoo.cfg while
running buildout!

Then to prepare your database whith demo data to be able to run unit test::

    bin/upgrade_odoo -d odoo --init-load-demo-data

To launch zitcom unittest::

    bin/nosetests -d odoo -- -s -v modules/
