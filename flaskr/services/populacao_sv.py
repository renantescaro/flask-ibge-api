from requests.models import Response
from flaskr.apis.ibge.populacao_api import PopulacaoApi


class PopulacaoSv:
    def __init__(self) -> None:
        self.id_norte = 1
        self.id_nordeste = 2
        self.id_sudeste = 3
        self.id_sul = 4
        self.id_centro_oeste = 5


    def _tratamento_retorno(self, response: Response):
        if response.status_code == 200:
            return response.json()
        return None


    def todas_regioes(self):
        return [
            {'regiao':'brasil',   'dados':self.brasil()},
            {'regiao':'norte',    'dados':self.norte()},
            {'regiao':'nordeste', 'dados':self.nordeste()},
            {'regiao':'sul',      'dados':self.sul()},
            {'regiao':'sudeste',  'dados':self.sudeste()} ]


    def brasil(self):
        return self._tratamento_retorno(
            PopulacaoApi().brasil() )


    def norte(self):
        return self._tratamento_retorno(
            PopulacaoApi().regiao(self.id_norte) )


    def nordeste(self):
        return self._tratamento_retorno(
            PopulacaoApi().regiao(self.id_nordeste) )


    def sudeste(self):
        return self._tratamento_retorno(
            PopulacaoApi().regiao(self.id_sudeste) )


    def sul(self):
        return self._tratamento_retorno(
            PopulacaoApi().regiao(self.id_sul) )


    def centro_oeste(self):
        return self._tratamento_retorno(
            PopulacaoApi().regiao(self.id_centro_oeste) )