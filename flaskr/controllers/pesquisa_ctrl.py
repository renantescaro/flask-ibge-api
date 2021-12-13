import json
from flask import Blueprint, render_template

from flaskr.services.pesquisa_sv import PesquisaSv

bp = Blueprint(
    'pesquisa',
    __name__,
    template_folder='pesquisa' )


class PesquisaCtrl:
    @bp.route('/pesquisas', methods=['GET'])
    def pesquisas():
        return render_template(
            'pesquisas/listagem.html',
            titulo = 'Listagem Pesquisas',
            dados = json.dumps(PesquisaSv().todas()) )


    @bp.route('/pesquisas/<id>/nome', methods=['GET'])
    def nome_por_id(id:int):
        return json.dumps(
            {'nome' : PesquisaSv().nome_por_id(id)}
        )