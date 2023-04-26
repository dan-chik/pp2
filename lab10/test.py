import psycopg2

hostname = 'localhost'
database = 'suppliers'
username = 'postgres'
pwd = '12345'
#port_id = 5432

conn = psycopg2.connect(
            host = hostname,
            dbname = database,
            user = username,
            password = pwd)
            




