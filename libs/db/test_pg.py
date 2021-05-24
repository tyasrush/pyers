import libs.db.pg as pg
import pytest
from psycopg2 import pool, connect, extensions

config = dict(host='localhost', port=5432, user='postgres', password='postgres', dbname='testingdong')
p = None

@pytest.fixture()
def pools():
    pg.DB_NAME = 'testingdong'
    p = pg.get_pool()
    if p:
        print("Connection pool created successfully")

    yield p

def test_init_db():
    conn = connect(host="localhost", port=5432, user="postgres", password="postgres")
    conn.set_isolation_level(extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    cur = conn.cursor()
    cur.execute('CREATE DATABASE testingdong')
    cur.close()
    conn.close()

def test_create_table(pools):
    err = pg.query_commit(pools, 'CREATE TABLE IF NOT EXISTS test_table_ini')
    if err:
        print(err)
        pytest.fail
    
    pg.release_all_conn(pools)

def test_release_conn(pools):
    pg.release_all_conn(pools)

def test_drop_db():
    conn = connect(host="localhost", port=5432, user="postgres", password="postgres")
    conn.set_isolation_level(extensions.ISOLATION_LEVEL_AUTOCOMMIT)

    cur = conn.cursor()
    cur.execute('DROP DATABASE testingdong')
    cur.close()
    conn.close()