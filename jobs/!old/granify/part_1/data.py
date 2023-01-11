class Data:
    def __init__(self, database):
        print("Connecting to database")

    def beginTran(self):
        print("Beginning a transaction")

    def commit(self):
        print("Committing transaction")

    def rollback(self):
        print("Rolling back transaction")

    def insert(self, table, object):
        print("Inserting " + object.getName() + " into table " + table)
