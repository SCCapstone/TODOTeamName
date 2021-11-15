CREATE DATABASE pgdb;
CREATE USER admin WITH PASSWORD 'password'
ALTER ROLE admin SET client_encoding TO 'utf8';
ALTER ROLE admin SET default_transaction_isolation TO 'read committed';
ALTER ROLE admin SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE helloworld TO <yourname>;

