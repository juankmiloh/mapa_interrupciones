from sqlalchemy.sql import text


class EmpresasRepository:
    def __init__(self, db):
        self.db = db

    def get_empresas_bd(self, empresa):
        sql = '''
            SELECT 
                IDEMPRESA, NOMBRE, 'ENERGIA' AS SERVICIO, COD_SERVICIO, SIGLA, NIT 
            FROM 
            (
                SELECT DISTINCT 
                    IDENTIFICADOR_EMPRESA IDEMPRESA,
                    TRIM(NOMBRE_DE_LA_EMPRESA) NOMBRE,
                    TRIM(SIGLA_DE_LA_EMPRESA) SIGLA,
                    TO_NUMBER(NIT_DE_LA_EMPRESA) NIT,
                    DECODE(ACUEDUCTO,1,1,0,0) ACUEDUCTO,
                    DECODE(ALCANTARILLADO,1,2,0,0) ALCANTARILLADO,
                    DECODE(ASEO,1,3,0,0) ASEO,
                    DECODE(ENERGIA,1,4,0,0) ENERGIA,
                    DECODE(GAS_NATURAL,1,5,0,0) GAS_NATURAL,
                    DECODE(GLP,1,7,0,0) GLP
                FROM RENASER.BODEGA_EMPRESAS_ORFEO 
                WHERE
                    (ACUEDUCTO=1 OR ALCANTARILLADO=1 OR ASEO=1 OR ENERGIA=1 OR GAS_NATURAL=1 OR GLP=1)
            )
            UNPIVOT 
            (
                COD_SERVICIO FOR SERVICIO IN (ACUEDUCTO,ALCANTARILLADO,ASEO,ENERGIA,GAS_NATURAL,GLP)
            )
            WHERE COD_SERVICIO != 0 
            AND COD_SERVICIO = 4 
            AND (IDEMPRESA = :EMPRESA_ARG OR 0 = :EMPRESA_ARG) 
            ORDER BY 2
        '''
        return self.db.engine.execute(text(sql), EMPRESA_ARG=empresa).fetchall()