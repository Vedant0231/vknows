# vknows
Vknows is a articals publication website . This is my personal project which is under development.
requirements

asgiref==3.6.0
backports.zoneinfo==0.2.1
Django==4.2
mysql==0.0.3
mysql-connector-python==8.0.32
mysqlclient==2.1.1
protobuf==3.20.3
sqlparse==0.4.3

table schema
CREATE TABLE users (
    ->     name VARCHAR(100),
    ->     surname VARCHAR(100),
    ->     email VARCHAR(100),
    ->     usernum INT,
    ->     userpassword VARCHAR(100),
    ->     gender VARCHAR(100)
    -> );

