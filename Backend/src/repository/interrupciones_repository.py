from sqlalchemy.sql import text


class InterrupcionesRepository:
    def __init__(self, db):
        self.db = db

    def get_interrupciones_bd(self, anio, mes, empresa, causa):
        sql = '''
            SELECT CONVERT(EMPRESA.IDEMPRESA, 'US7ASCII', 'EE8MSWIN1250'),
                INTERR.* 
            FROM 
            (
                SELECT 
                    CONVERT(CP.NOMBRE_CENTRO_POBLADO, 'US7ASCII', 'EE8MSWIN1250'),
                    CP.LONGITUD,
                    CP.LATITUD,
                    TO_CHAR(DANE_INTER.COD_DANE),
                    DANE_INTER.IDENTIFICADOR_EMPRESA,
                    DANE_INTER.CAR_CARG_ANO,
                    DANE_INTER.CAR_CARG_MES,
                    ROUND(DANE_INTER.PNEXC/60,2),
                    ROUND(DANE_INTER.NPNEXC/60,2),
                    ROUND(DANE_INTER.REMER/60,2),
                    ROUND(DANE_INTER.STNSTR/60,2),
                    ROUND(DANE_INTER.SEGCIU/60,2),
                    ROUND(DANE_INTER.FNIVEL1/60,2),
                    ROUND(DANE_INTER.CASTNAT/60,2),
                    ROUND(DANE_INTER.TERR/60,2),
                    ROUND(DANE_INTER.CALZESP/60,2),
                    ROUND(DANE_INTER.TSUBEST/60,2),
                    ROUND(DANE_INTER.INFRA/60,2),
                    ROUND(DANE_INTER.SUMI/60,2),
                    ROUND(DANE_INTER.PEXP/60,2),
                    DANE_INTER.TOTAL_INTER 
                FROM 
                (
                    SELECT 
                        INTER.*,
                        ROUND((PNEXC+NPNEXC+REMER+STNSTR+SEGCIU+FNIVEL1+CASTNAT+TERR+CALZESP+TSUBEST+INFRA+SUMI+PEXP)/60,2) AS TOTAL_INTER 
                    FROM 
                    (
                        SELECT 
                            TRAFODANE.COD_DANE,
                            F5.IDENTIFICADOR_EMPRESA,
                            F5.CAR_CARG_ANO,
                            F5.CAR_CARG_MES,
                            CASE WHEN (:PNEXC_ARG = 16) THEN SUM(F5.CAR_T442_MIN_PBEXC) ELSE 0 END AS PNEXC,
                            CASE WHEN (:NPNEXC_ARG = 18) THEN SUM(F5.CAR_T442_MIN_NPNEXC) ELSE 0 END AS NPNEXC,
                            CASE WHEN (:REMER_ARG = 20) THEN SUM(F5.CAR_T442_MIN_REMER) ELSE 0 END AS REMER,
                            CASE WHEN (:STNSTR_ARG = 22) THEN SUM(F5.CAR_T442_MIN_STNSTR) ELSE 0 END AS STNSTR,
                            CASE WHEN (:SEGCIU_ARG = 24) THEN SUM(F5.CAR_T442_MIN_SEG_CIU) ELSE 0 END AS SEGCIU,
                            CASE WHEN (:FNIVEL1_ARG = 26) THEN SUM(F5.CAR_T442_MIN_FNIVEL1) ELSE 0 END AS FNIVEL1,
                            CASE WHEN (:CASTNAT_ARG = 28) THEN SUM(F5.CAR_T442_MIN_CASTNAT) ELSE 0 END AS CASTNAT,
                            CASE WHEN (:TERR_ARG = 30) THEN SUM(F5.CAR_T442_MIN_TERR) ELSE 0 END AS TERR,
                            CASE WHEN (:CALZESP_ARG = 32) THEN SUM(F5.CAR_T442_MIN_CAL_ZESP) ELSE 0 END AS CALZESP,
                            CASE WHEN (:TSUBEST_ARG = 34) THEN SUM(F5.CAR_T442_MIN_TSUBEST) ELSE 0 END AS TSUBEST,
                            CASE WHEN (:INFRA_ARG = 36) THEN SUM(F5.CAR_T442_MIN_INFRA) ELSE 0 END AS INFRA,
                            CASE WHEN (:SUMI_ARG = 38) THEN SUM(F5.CAR_T442_MIN_SUMI) ELSE 0 END AS SUMI,
                            CASE WHEN (:PEXP_ARG = 40) THEN SUM(F5.CAR_T442_MIN_EXP) ELSE 0 END AS PEXP 
                        FROM 
                        (
                            SELECT 
                                * 
                            FROM 
                                CARG_COMERCIAL_E.CAR_T442_FORMATO5 
                            WHERE 
                                CAR_CARG_ANO = :ANIO_ARG
                                AND (IDENTIFICADOR_EMPRESA = :EMPRESA_ARG OR 0 = :EMPRESA_ARG)
                                AND (CAR_CARG_MES = :MES_ARG)
                        ) F5,
                        (SELECT * FROM TRAFO_DANE) TRAFODANE 
                        WHERE 
                            F5.CAR_T442_COD_TRANS = TRAFODANE.COD_TRAFO
                            AND F5.IDENTIFICADOR_EMPRESA = TRAFODANE.IDENTIFICADOR_EMPRESA 
                        GROUP BY 
                            TRAFODANE.COD_DANE,
                            F5.IDENTIFICADOR_EMPRESA,
                            F5.CAR_CARG_ANO,
                            F5.CAR_CARG_MES
                    ) INTER 
                    WHERE PNEXC+NPNEXC+REMER+STNSTR+SEGCIU+FNIVEL1+CASTNAT+TERR+CALZESP+TSUBEST+INFRA+SUMI+PEXP > 0
                ) DANE_INTER,
                (SELECT * FROM JHERRERAA.GIS_CENTRO_POBLADO) CP 
                WHERE DANE_INTER.COD_DANE = CP.CODIGO_CENTRO_POBLADO
            )INTERR,
            (
                SELECT 
                    IDEMPRESA, NOMBRE, COD_SERVICIO, SIGLA, NIT 
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
            )EMPRESA 
            WHERE IDENTIFICADOR_EMPRESA = IDEMPRESA
        '''
        return self.db.engine.execute(text(sql), ANIO_ARG=anio, MES_ARG=mes, EMPRESA_ARG=empresa, PNEXC_ARG=causa['PNEXC_ARG'], NPNEXC_ARG=causa['NPNEXC_ARG'], REMER_ARG=causa['REMER_ARG'], STNSTR_ARG=causa['STNSTR_ARG'], SEGCIU_ARG=causa['SEGCIU_ARG'], FNIVEL1_ARG=causa['FNIVEL1_ARG'], CASTNAT_ARG=causa['CASTNAT_ARG'], TERR_ARG=causa['TERR_ARG'], CALZESP_ARG=causa['CALZESP_ARG'], TSUBEST_ARG=causa['TSUBEST_ARG'], INFRA_ARG=causa['INFRA_ARG'], SUMI_ARG=causa['SUMI_ARG'], PEXP_ARG=causa['EXP_ARG']).fetchall()
        