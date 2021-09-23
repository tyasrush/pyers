import db.pg as pg

pg.DB_NAME = 'test_db'
po = pg.get_pool()

pg.test_import_()

results = pg.query(po, 'select * from allorders limit 5')
print(type(results))