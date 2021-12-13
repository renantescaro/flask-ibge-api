import requests
from requests.models import Response
from flaskr.utils.config import Config


class PesquisaApi:
    def __init__(self) -> None:
        self.url = f"{Config.get('URL_API_IBGE')}/v1/pesquisas"


    def todas(self) -> Response:
        return requests.get(url=self.url)


    def por_id(self, id:int) -> Response:
        return requests.get(url=f"{self.url}/{id}")