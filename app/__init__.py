from flask import Flask
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, BOOTSTRAP_SERVE_LOCAL
from flask_wtf.csrf import CSRFProtect
import mysql.connector

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        MYSQL_USER=DB_USERNAME,
        MYSQL_PASSWORD=DB_PASSWORD,
        MYSQL_DATABASE=DB_NAME,
        MYSQL_HOST=DB_HOST,
        #BOOTSTRAP_SERVE_LOCAL=BOOTSTRAP_SERVE_LOCAL
    )
    CSRFProtect(app)

    # Create a MySQL connection
    db = mysql.connector.connect(
        user=app.config['MYSQL_USER'],
        password=app.config['MYSQL_PASSWORD'],
        host=app.config['MYSQL_HOST'],
        database=app.config['MYSQL_DATABASE']
    )

    # Add the MySQL connection to the Flask app context
    app.config['MYSQL_DB'] = db

    # Create a cursor to execute MySQL queries
    #cursor = db.cursor()

    from .routes.college import college_bp as college_blueprint
    app.register_blueprint(college_blueprint, url_prefix='/college')

    from .routes.course import course_bp as course_blueprint
    app.register_blueprint(course_blueprint, url_prefix='/course')

    from .routes.student import student_bp as student_blueprint
    app.register_blueprint(student_blueprint, url_prefix='/student')

    from .routes.main import main_bp as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    return app