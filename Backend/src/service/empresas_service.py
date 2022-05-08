from ..repository import EmpresasRepository


class EmpresasService:

    def get_empresas(self, empresas_repository: EmpresasRepository, empresa):
        empresas = []
        data = empresas_repository.get_empresas_bd(empresa)
        empresa = 0
        for result in data:
            if empresa != result[0]:
                    empresas.append(
                        {
                            'cod_empresa': result[0],
                            'nombre': result[1],
                            'servicio': result[2],
                        }
                    )
            empresa = result[0]
        return empresas
