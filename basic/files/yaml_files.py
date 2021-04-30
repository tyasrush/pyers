import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# with open("./basic/files/books.sql", "r") as f:
#     dbcon = psycopg2.connect(host="localhost", port=5432, user="postgres", password="postgres")
#     dbcon.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
#     cur = dbcon.cursor()
#     cur.execute("DROP DATABASE IF EXISTS test_library")
#     cur.execute("CREATE DATABASE test_library")
#     dbcon.close()

#     dbcon = psycopg2.connect(host="localhost", port=5432, user="postgres", password="postgres", dbname="test_library")
#     cur = dbcon.cursor()
#     cur.execute(f.read())
#     dbcon.commit()
#     dbcon.close()

#     f.close()

def MigrateUp(dict_conn, sql_file_path: str):
    try:
        dbName = dict_conn['dbname']
        print(dict_conn['dbname'])
        # Set new dictionary for database creation.
        withoutDbDict = dict_conn
        withoutDbDict.pop("dbname", None)

        # Create connection without dbname for database creation only.
        dbcon = psycopg2.connect(**withoutDbDict)
        # Set isolation auto commit cause database creation can't do in transaction query.
        dbcon.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = dbcon.cursor()
        cur.execute(f"DROP DATABASE IF EXISTS {dbName}")
        cur.execute(f"CREATE DATABASE {dbName}")
        # Close first connection.
        dbcon.close()

        # Open sql file that contains related queries for testing.
        sqlFile = open(sql_file_path, "r")
        # Create second connection for executing tables creation and some seed data (if it any data in sql file)
        dict_conn['dbname'] = dbName
        dbcon = psycopg2.connect(**dict_conn)
        cur = dbcon.cursor()
        cur.execute(sqlFile.read())
        dbcon.commit()
        dbcon.close()

        sqlFile.close()
    except Exception as e:
        raise e 

dictparam = dict(host="localhost", port=5432, user="postgres", password="postgres", dbname="indodax_agent")
MigrateUp(dictparam, "./basic/files/books.sql")