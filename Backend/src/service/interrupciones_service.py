import csv

from ..repository import InterrupcionesRepository

from flask import send_file  # descargar archivos

class InterrupcionesService:

    def get_interrupciones(self, interrupciones_repository: InterrupcionesRepository, anio, mes, empresa, causa):
        causas = self.__verifyCausas(causa)
        interrupciones = []
        data = interrupciones_repository.get_interrupciones_bd(anio, mes, empresa, causas)
        for result in data:
            interrupciones.append(
                {
                    'nom_empresa': result[0],
                    'centro_poblado': result[1],
                    'longitude': result[2],
                    'latitude': result[3],
                    'cod_dane': result[4],
                    'cod_empresa': result[5],
                    'ano': result[6],
                    'mes': result[7],
                    'pnexc': result[8],
                    'npnexc': result[9],
                    'remer': result[10],
                    'stnstr': result[11],
                    'segciu': result[12],
                    'fnivel1': result[13],
                    'castnat': result[14],
                    'terr': result[15],
                    'calzesp': result[16],
                    'tsubest': result[17],
                    'infra': result[18],
                    'sumi': result[19],
                    'exp': result[20],
                    'total': result[21],
                    'chrome': 1 # Esto se coloca para que renderice el mapa en chrome
                }
            )
        return self.__getCSV(interrupciones)

    def __getCSV(self, arrayInterrupciones):
        with open('src/sources/file_interrupciones.csv', 'w', newline='') as csvfile:
            fieldnames = ['nom_empresa', 'centro_poblado', 'longitude', 'latitude', 'cod_dane', 'cod_empresa', 'ano', 'mes', 'pnexc', 'npnexc',
                          'remer', 'stnstr', 'segciu', 'fnivel1',  'castnat', 'terr', 'calzesp', 'tsubest', 'infra', 'sumi', 'exp', 'total', 'chrome']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(arrayInterrupciones)
        return send_file('sources/file_interrupciones.csv', as_attachment=True)

    def __verifyCausas(self, causa):
        resp = {'PNEXC_ARG': 0, 'NPNEXC_ARG': 0, 'REMER_ARG': 0, 'STNSTR_ARG': 0, 'SEGCIU_ARG': 0, 'FNIVEL1_ARG': 0, 'CASTNAT_ARG': 0, 'TERR_ARG': 0, 'CALZESP_ARG': 0, 'TSUBEST_ARG': 0, 'INFRA_ARG': 0, 'SUMI_ARG': 0, 'EXP_ARG': 0}
        if causa == 0:
            resp = {'PNEXC_ARG': 16, 'NPNEXC_ARG': 18, 'REMER_ARG': 20, 'STNSTR_ARG': 22, 'SEGCIU_ARG': 24, 'FNIVEL1_ARG': 26, 'CASTNAT_ARG': 28, 'TERR_ARG': 30, 'CALZESP_ARG': 32, 'TSUBEST_ARG': 34, 'INFRA_ARG': 36, 'SUMI_ARG': 38, 'EXP_ARG': 4}
        else:
            if causa == 16:
                resp['PNEXC_ARG'] = 16
            if causa == 18:
                resp['NPNEXC_ARG'] = 18
            if causa == 20:
                resp['REMER_ARG'] = 20
            if causa == 22:
                resp['STNSTR_ARG'] = 22
            if causa == 24:
                resp['SEGCIU_ARG'] = 24
            if causa == 26:
                resp['FNIVEL1_ARG'] = 26
            if causa == 28:
                resp['CASTNAT_ARG'] = 28
            if causa == 30:
                resp['TERR_ARG'] = 30
            if causa == 32:
                resp['CALZESP_ARG'] = 32
            if causa == 34:
                resp['TSUBEST_ARG'] = 34
            if causa == 36:
                resp['INFRA_ARG'] = 36
            if causa == 38:
                resp['SUMI_ARG'] = 38
            if causa == 40:
                resp['EXP_ARG'] = 40
        return resp
