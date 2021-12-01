import requests
from flaskr.utils.config import Config


class PesquisaApi:
    def __init__(self) -> None:
        self.url = Config.get('URL_API_IBGE') + str('/v1/pesquisas')


    def todas(self):
        return requests.get(url=self.url)