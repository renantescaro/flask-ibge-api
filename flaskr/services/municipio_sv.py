import json
from flaskr.apis.ibge.municipios_api import MunicipiosApi
from flaskr.utils.config import Config


class MunicipioSv:
    def __init__(self) -> None:
        self.caminho_json = Config.get('CAMINHO_JSONS')+str('distritos.json')


    def _ler_arquivo_local(self):
        arquivo = open(self.caminho_json, encoding='utf8')
        return json.load(arquivo)


    def _gravar_arquivo_local(self, municipios):
        with open(self.caminho_json, 'w') as f:
            f.write(municipios)


    # retorna todos municipios do ibge
    def nova_consulta(self):
        response = MunicipiosApi().todos()
        if response.status_code == 200:
            self._gravar_arquivo_local(json.dumps(response.json()))


    # retorna todos municipios do arquivo local
    def todos(self):
        return self._ler_arquivo_local()