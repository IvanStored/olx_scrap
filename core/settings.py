import os


BASEDIR = os.path.abspath(os.path.dirname(__file__))
DB_NAME = "users.db"
DB_DIRECTORY = "db/"


def create_path_to_db():
    PATH_TO_DB_DIRECTORY = os.path.abspath(
        os.path.join(os.getcwd(), BASEDIR, DB_DIRECTORY)
    )
    if not os.path.exists(PATH_TO_DB_DIRECTORY):
        os.mkdir(PATH_TO_DB_DIRECTORY)


class Config(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + DB_NAME
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "secretkey"
