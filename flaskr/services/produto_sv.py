from requests.models import Response
from flaskr.apis.ibge.produto_api import ProdutoApi


class ProdutoSv:
    def _tratamento_retorno(self, response: Response):
        if response.status_code == 200:
            return response.json()
        return None


    def todos(self):
        return self._tratamento_retorno(
            ProdutoApi().todos() )


    def de_geociencia(self):
        return self._tratamento_retorno(
            ProdutoApi().de_geociencia() )


    def de_estatistica(self):
        return self._tratamento_retorno(
            ProdutoApi().de_estatistica() )