import requests
from flaskr.utils.config import Config


class IndicadorApi:
    def __init__(self) -> None:
        self.url = Config.get('URL_API_IBGE') + str('/v1/pesquisas/')


    def todos_por_pesquisa(self, id_pesquisa:int):
        endpoint = self.url+str(id_pesquisa)+'/indicadores/'
        return requests.get(url=endpoint)