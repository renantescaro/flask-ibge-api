import json
from flask import Blueprint, render_template, redirect, url_for
from flaskr.services.municipio_sv import MunicipioSv

bp = Blueprint(
    'municipio',
    __name__,
    template_folder='municipio' )


class MunicipioCtrl:
    @bp.route('/municipios', methods=['GET'])
    def listagem():
        return render_template(
            'municipios/listagem.html',
            titulo = 'Listagem Municipios',
            dados = json.dumps(MunicipioSv().todos()) )


    @bp.route('/municipios/nova-consulta', methods=['GET'])
    def nova_consulta():
        MunicipioSv().nova_consulta()
        return redirect(url_for('municipio.listagem'))