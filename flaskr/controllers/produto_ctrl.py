import json
from flask import Blueprint
from flask.templating import render_template
from flaskr.services.produto_sv import ProdutoSv

bp = Blueprint(
    'produto',
    __name__,
    template_folder='produto' )


class ProdutoCtrl:
    @bp.route('/produtos', methods=['GET'])
    def todos():
        return render_template(
            'produtos/listagem.html',
            titulo = 'Listagem Produtos',
            dados = json.dumps(ProdutoSv().todos()) )


    @bp.route('/produtos/estatistica', methods=['GET'])
    def estatistica():
        return render_template(
            'produtos/listagem.html',
            titulo = 'Listagem Produtos de Estatistica',
            dados = json.dumps(ProdutoSv().de_estatistica()) )


    @bp.route('/produtos/geociencia', methods=['GET'])
    def geociencia():
        return render_template(
            'produtos/listagem.html',
            titulo = 'Listagem Produtos de Geociencia',
            dados = json.dumps(ProdutoSv().de_geociencia()) )