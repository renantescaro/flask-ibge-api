from flaskr.apis.ibge.pesquisa_api import PesquisaApi


class PesquisaSv:
    def todas(self):
        response = PesquisaApi().todas()
        if response.status_code == 200:
            return response.json()
        return None