from flask import Flask
from config import DB_USERNAME, DB_PASSWORD, DB_NAME, DB_HOST, SECRET_KEY, BOOTSTRAP_SERVE_LOCAL
from flask_wtf.csrf import CSRFProtect
from mysql.connector import connect

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=SECRET_KEY,
        MYSQL_USER=DB_USERNAME,
        MYSQL_PASSWORD=DB_PASSWORD,
        MYSQL_DATABASE=DB_NAME,
        MYSQL_HOST=DB_HOST,
        BOOTSTRAP_SERVE_LOCAL=BOOTSTRAP_SERVE_LOCAL
    )
    CSRFProtect(app)
    
    # Centralized database connection
    app.db_connection = connect(
        user=DB_USERNAME,
        password=DB_PASSWORD,
        host=DB_HOST,
        database=DB_NAME
    )

    from .routes.college import college_bp as college_blueprint
    app.register_blueprint(college_blueprint, url_prefix='/college')

    from .routes.course import course_bp as course_blueprint
    app.register_blueprint(course_blueprint, url_prefix='/course')

    from .routes.student import student_bp as student_blueprint
    app.register_blueprint(student_blueprint, url_prefix='/student')

    from .routes.main import main_bp as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/')

    return app