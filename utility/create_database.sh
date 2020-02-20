#!/bin/bash

sudo -u postgres psql -c "CREATE ROLE regis_perfect WITH PASSWORD '1234';"
sudo -u postgres psql -c "ALTER ROLE regis_perfect WITH LOGIN;"
#sudo -u postgres psql -c "DROP DATABASE test1;"
sudo -u postgres psql -c "CREATE DATABASE regis_perfect;"
sudo -u postgres psql -c "GRANT ALL PRIVILEGES ON DATABASE regis_perfect TO regis_perfect;"

