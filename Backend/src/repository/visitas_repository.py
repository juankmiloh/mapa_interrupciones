from sqlalchemy.sql import text


class VisitasRepository:
    def __init__(self, db):
        self.db = db

    def get_visitas_bd(self):
        sql = '''
            SELECT * FROM INTERRUPCIONES.VISITAS;
        '''
        return self.db.engine.execute(text(sql)).fetchall()
       
    def visitas_insert_bd(self, visitas):
        # print('-------------------------------------')
        # print('OBJ VISITA -> ', visitas)
        # print('-------------------------------------')

        sql = '''
            INSERT INTO INTERRUPCIONES.VISITAS(ID_USUARIO, OBSERVACION, FECHAREGISTRO)
            VALUES (:ID_USUARIO_ARG, :OBSERVACION_ARG, CURRENT_TIMESTAMP);
        '''
        resultsql = self.db.engine.execute(text(sql), ID_USUARIO_ARG=visitas["id_usuario"], OBSERVACION_ARG=visitas["observacion"])

        return resultsql

    def visitas_update_bd(self, visitas):
        # print('-------------------------------------')
        # print('* VISITA A ACTUALIZAR -> ', visitas)
        # print('-------------------------------------')

        sql = '''
            UPDATE 
                INTERRUPCIONES.VISITAS
	        SET 
                ID_USUARIO = :IDUSUARIO_ARG,
                OBSERVACION = :OBSERVACION_ARG,
                FECHAREGISTRO = CURRENT_TIMESTAMP
	        WHERE 
                ID_VISITA = :IDVISITA_ARG;
        '''
        resultsql = self.db.engine.execute(text(sql), IDVISITA_ARG=visitas["idvisita"], IDUSUARIO_ARG=visitas["idusuario"], OBSERVACION_ARG=visitas["observacion"])

        return resultsql
                        
    def visitas_delete_bd(self, visitas):
        # print('-------------------------------------')
        # print('* VISITA A ELIMINAR -> ', visitas)
        # print('-------------------------------------')
        sql = '''
            DELETE FROM
                INTERRUPCIONES.VISITAS
            WHERE
                ID_VISITA = :IDVISITA_ARG;
        '''
        resultsql = self.db.engine.execute(text(sql), IDVISITA_ARG=visitas["idvisita"])

        return resultsql
