from flaskr.apis.ibge.pesquisa_api import PesquisaApi


class PesquisaSv:
    def todas(self):
        response = PesquisaApi().todas()
        if response.status_code == 200:
            return response.json()
        return None


    def por_id(self, id:int):
        response = PesquisaApi().por_id(id)
        if response.status_code == 200:
            return response.json()
        return None


    def nome_por_id(self, id:int) -> str:
        pesquisa = self.por_id(id)
        if pesquisa is None: return ''
        return pesquisa['nome']