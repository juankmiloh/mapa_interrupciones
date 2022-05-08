from sqlalchemy.sql import text


class CausasRepository:
    def __init__(self, db):
        self.db = db

    def get_causas_bd(self, causa):
        sql = '''
            SELECT * FROM JHERRERAA.CAUSAS_INTERR 
            WHERE (COD_CAUSA = :CAUSA_ARG OR 0 = :CAUSA_ARG)
        '''
        return self.db.engine.execute(text(sql), CAUSA_ARG=causa).fetchall()