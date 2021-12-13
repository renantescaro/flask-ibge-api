import json
from flask import Blueprint, render_template
from flaskr.services.indicador_sv import IndicadorSv
from flaskr.services.pesquisa_sv import PesquisaSv

bp = Blueprint(
    'indicador',
    __name__,
    template_folder='indicador' )


class IndicadorCtrl:
    @bp.route('/indicadores/pesquisa/<id_pesquisa>', methods=['GET'])
    def indicadores_por_pesquisa(id_pesquisa:int):
        nome_pesquisa = PesquisaSv().nome_por_id(id_pesquisa)
        return render_template(
            'indicador/listagem.html',
            titulo = f"Indicadores da Pesquisa {id_pesquisa} - {nome_pesquisa}",
            id_pesquisa = id_pesquisa,
            dados = json.dumps(IndicadorSv().todos_por_pesquisa(id_pesquisa)) )