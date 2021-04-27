import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

with open("./basic/files/books.sql", "r") as f:
    dbcon = psycopg2.connect(host="localhost", port=5432, user="postgres", password="postgres")
    dbcon.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = dbcon.cursor()
    cur.execute("DROP DATABASE IF EXISTS test_library")
    cur.execute("CREATE DATABASE test_library")
    dbcon.close()

    dbcon = psycopg2.connect(host="localhost", port=5432, user="postgres", password="postgres", dbname="test_library")
    cur = dbcon.cursor()
    cur.execute(f.read())
    dbcon.commit()
    dbcon.close()

    f.close()