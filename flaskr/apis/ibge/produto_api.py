import requests
from flaskr.utils.config import Config


class ProdutoApi:
    def __init__(self) -> None:
        self.url = Config.get('URL_API_IBGE') + str('/v1/produtos/')


    def todos(self):
        return requests.get(url=self.url)
    

    def de_estatistica(self):
        return requests.get(url=self.url + str('estatisticas'))


    def de_geociencia(self):
        return requests.get(url=self.url + str('geociencias'))