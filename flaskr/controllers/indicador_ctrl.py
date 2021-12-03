import json
from flask import Blueprint, render_template
from flaskr.services.indicador_sv import IndicadorSv

bp = Blueprint(
    'indicador',
    __name__,
    template_folder='indicador' )


class IndicadorCtrl:
    @bp.route('/indicadores/pesquisa/<id_pesquisa>', methods=['GET'])
    def indicadores_por_pesquisa(id_pesquisa:int):
        return render_template(
            'indicador/listagem.html',
            titulo = 'Listagem Indicadores por Pesquisa',
            dados = json.dumps(IndicadorSv().todos_por_pesquisa(id_pesquisa)) )