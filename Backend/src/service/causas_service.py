from ..repository import CausasRepository


class CausasService:

    def get_causas(self, causas_repository: CausasRepository, causa):
        causas = []
        data = causas_repository.get_causas_bd(causa)
        causa = 0
        for result in data:
            if causa != result[0]:
                    causas.append(
                        {
                    'cod_causa': result[0],
                    'col_sui': result[1],
                    'descripcion': result[2]
                }
                    )
            causa = result[0]
        return causas
