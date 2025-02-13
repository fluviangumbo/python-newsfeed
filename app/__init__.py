from flask import Flask
from .routes.home import bp as home_bp
from .routes.dashboard import bp as dash_bp

def create_app(test_config=None):
    # set up app config
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False
    app.config.from_mapping(
        SECRET_KEY='super_secret_key'
    )

    @app.route('/hello')
    def hello():
        return 'hello world'
    
    # register routes
    app.register_blueprint(home_bp)
    app.register_blueprint(dash_bp)

    return app