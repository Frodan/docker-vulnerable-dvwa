#!/bin/bash

chown -R mysql:mysql /var/lib/mysql /var/run/mysqld

echo '[+] Starting mysql...'
service mysql start

echo '[+] Starting apache'
service apache2 start

sleep 5
curl -d "create_db=Create+%2F+Reset+Database" -X POST http://localhost/setup.php -vv
while true
do
    tail -f /var/log/apache2/*.log
    exit 0
done
