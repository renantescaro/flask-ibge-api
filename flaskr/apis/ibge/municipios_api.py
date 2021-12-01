import requests
from flaskr.utils.config import Config


class MunicipiosApi:
    def __init__(self) -> None:
        self.url = Config.get('URL_API_IBGE') + str('/v1/localidades/municipios/')


    def todos(self):
        return requests.get(url=self.url)