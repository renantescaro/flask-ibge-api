import json
from flask import Blueprint
from flask.templating import render_template
from flaskr.services.populacao_sv import PopulacaoSv
from flaskr.services.produto_sv import ProdutoSv

bp = Blueprint(
    'populacao',
    __name__,
    template_folder='populacao' )


class PopulacaoCtrl:
    @bp.route('/populacao', methods=['GET'])
    def todas_regioes():
        return render_template(
            'populacao/listagem.html',
            titulo = 'População de todas as Regiões',
            dados = json.dumps(PopulacaoSv().todas_regioes() ))