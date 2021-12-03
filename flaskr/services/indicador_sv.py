from flaskr.apis.ibge.indicador_api import IndicadorApi
from flaskr.utils.debug import Debug


class IndicadorSv:
    def __init__(self) -> None:
        self.json_final = []


    def _montar_json_linear(self, dados):
        def concatenar_notas(notas):
            notas_finais = ''
            for nota in notas:
                notas_finais += ' ' + str(nota)
            return notas_finais

        for linha in dados:
            self.json_final.append({
                'id'        : linha['id'],
                'posicao'   : linha['posicao'],
                'indicador' : linha['indicador'],
                'classe'    : linha['classe'],
                'nota'      : concatenar_notas(linha['nota']),
            })

            if linha['children'] != None and len(linha['children']) > 0:
                self._montar_json_linear(linha['children'])
        return self.json_final


    def todos_por_pesquisa(self, id_pesquisa:int):
        response = IndicadorApi().todos_por_pesquisa(id_pesquisa)
        if response.status_code == 200:
            return self._montar_json_linear(response.json())
        return None