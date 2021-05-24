
import logging
import psycopg2
from psycopg2 import pool
import traceback

config = dict(host='localhost', port=5432, user='postgres', password='postgres')
DB_NAME, MAX_CONN = '', 1

def __init():
    if len(DB_NAME.strip()) > 0:
        dbname_param = {'dbname': DB_NAME}
        config.update(dbname_param)

def get_pool():
    __init()
    pgpool = pool.ThreadedConnectionPool(1, MAX_CONN, **config)
    if pgpool:
        print('PostgreSQL connection pool success')
        # logging.info('postgres pool connection success')

    return pgpool

def query(pgpool, query: str, params = None):
    try:
        conn = pgpool.getconn()
        cur = conn.cursor()
        cur.execute(query, params)
        results = cur.fetchall()
        cur.close()
        pgpool.putconn(conn)
        return results, None
    except Exception as e:
        logging.error('Error on query', { 'where': traceback.format_exc(), 'error': e })
        return None, e


def query_commit(pgpool, query: str, params = None):
    try:
        conn = pgpool.getconn()
        cur = conn.cursor()
        cur.execute(query, params)
        cur.commit()
        cur.close()
        pgpool.putconn(conn)
        return None
    except Exception as e:
        logging.error('Error on query commit', { 'where': traceback.format_exc(), 'error': e })
        return e

def release_all_conn(pool):
    pool.closeall()

def test_import_():
    print('testing')