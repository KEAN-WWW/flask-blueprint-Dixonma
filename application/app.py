from flask import Flask
from application.bp.homepage.homepage import homepage # Import Blueprint
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()

def init_app():
    """Initialize Flask app"""
    app = Flask(__name__, instance_relative_config=False)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
    migrate = Migrate(app, db)

    # Initialize Plugins
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprint
    app.register_blueprint(homepage, url_prefix="/")
    return app

# Correct indentation here
app = init_app()

if __name__ == "__main__":
    app.run(debug=True)
