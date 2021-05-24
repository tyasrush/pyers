import logging
import db.pg as pg
import pytest

@pytest.fixture
def initiate_db():
    sql = '''
    CREATE DATABASE test;
    CREATE TABLE IF NOT EXISTS book(
        _id BIGSERIAL PRIMARY KEY UNIQUE,
        title VARCHAR(255) NOT NULL,
        isbn VARCHAR(255),
        created_at TIMESTAMPTZ DEFAULT NOW()
    )

    INSERT INTO book(title, isbn) VALUES ('book 1', '8ntw8gw89yn7fg');
    INSERT INTO book(title, isbn) VALUES ('book 2', '9879my987n7g7g7n');
    INSERT INTO book(title, isbn) VALUES ('book 3', '887wt2nrg37627g287y');

    '''

    logging.debug(sql)
    pg.MAX_CONN = 5
    pool = pg.get_pool()
    pg.query_commit(pool, sql)

    yield pool

def test_select(initiate_db):
    pg.DB_NAME = 'test'
    pool = initiate_db
    result, err = pg.query(pool, 'SELECT * FROM book LIMIT 1')
    if err != None:
        pytest.fail(err)

    print(result)
