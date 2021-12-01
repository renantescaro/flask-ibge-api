import requests
from flaskr.utils.config import Config


class PopulacaoApi:
    def __init__(self) -> None:
        self.url = Config.get('URL_API_IBGE') + str('/v1/projecoes/populacao/')


    def brasil(self):
        return requests.get(url=self.url)


    def regiao(self, id_regiao:int):
        return requests.get(url=self.url + str(id_regiao))