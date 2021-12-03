from flask import Flask
from flaskr.controllers.inicial_ctrl import bp as bp_inicial
from flaskr.controllers.produto_ctrl import bp as bp_produto
from flaskr.controllers.populacao_ctrl import bp as bp_populacao
from flaskr.controllers.municipio_ctrl import bp as bp_municipio
from flaskr.controllers.pesquisa_ctrl import bp as bp_pesquisa
from flaskr.controllers.indicador_ctrl import bp as bp_indicador


def create_app(test_config=None):
    app = Flask(
        __name__,
        static_url_path = '/static',
        static_folder   = 'static',
        instance_relative_config = True )

    app.config.from_mapping(
        SECRET_KEY   = 'super secret key',
        SESSION_TYPE = 'filesystem',
        JSONIFY_PRETTYPRINT_REGULAR = False )


    # adicionar rotas
    app.register_blueprint(bp_inicial)
    app.register_blueprint(bp_produto)
    app.register_blueprint(bp_populacao)
    app.register_blueprint(bp_municipio)
    app.register_blueprint(bp_pesquisa)
    app.register_blueprint(bp_indicador)
    return app