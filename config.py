import os
_basedir = os.path.abspath(os.path.dirname(__name__))
DEBUG = True
SQLALCHEMY_DATABASE_URI = "postgresql://nikonikoni:niko1324@localhost:5432/Sberbank"
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "need to change it..."
LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
