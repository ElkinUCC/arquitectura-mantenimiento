import os
from pathlib import Path
from flask import Flask
from dotenv import load_dotenv
from .extensiones import db

def create_app():
    # 1. Configuración de rutas y variables de entorno
    root = Path(__file__).resolve().parents[2]
    load_dotenv(root / 'backend' / '.env')
    
    # 2. Inicialización de la aplicación Flask
    app = Flask(
        __name__, 
        static_folder=str(root / 'frontend'),
        static_url_path=''
    )
    
    # 3. Configuración de la base de datos
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///mantenimiento.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    
    # 4. Registro de Blueprints (rutas)
    from .ordenes.controladores import bp
    app.register_blueprint(bp)
    
    # 5. Definición de rutas básicas
    @app.get('/')
    def inicio():
        return app.send_static_file('index.html')
    
    @app.get('/health')
    def salud():
        return {'status': 'ok'}, 200
    
    # 6. Retorno de la instancia de la app
    return app