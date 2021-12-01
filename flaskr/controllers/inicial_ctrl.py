from flask import render_template, jsonify, Blueprint

bp = Blueprint(
    'inical',
    __name__,
    template_folder='templates' )


class LogCtrl:
    @bp.route('/', methods=['GET'])
    def inicial_template():
        return render_template(
            'inicial.html',
            titulo = 'inicial' )