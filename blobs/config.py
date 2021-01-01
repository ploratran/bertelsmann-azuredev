import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'

    SQL_SERVER = os.environ.get('SQL_SERVER') or 'udacity-server123.database.windows.net'
    SQL_DATABASE = os.environ.get('SQL_DATABASE') or 'udacity-db'
    SQL_USER_NAME = os.environ.get('SQL_USER_NAME') or 'uadmin'
    SQL_PASSWORD = os.environ.get('SQL_PASSWORD') or 'mimimama0129@'
    SQLALCHEMY_DATABASE_URI = 'mssql+pyodbc://' + SQL_USER_NAME + '@' + SQL_SERVER + ':' + SQL_PASSWORD + '@' + SQL_SERVER + ':1433/' + SQL_DATABASE + '?driver=ODBC+Driver+17+for+SQL+Server'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    BLOB_ACCOUNT = os.environ.get('BLOB_ACCOUNT') or 'udacity123'
    BLOB_STORAGE_KEY = os.environ.get('BLOB_STORAGE_KEY') or 'j7gozl06UxzYpMbNdddhI8MnzpqcW6s8AW717Xw4sA7FV3XF9nsQDWjqeVfN2rclVuKkcy1k14YjxzbCmWlZOg=='
    BLOB_CONTAINER = os.environ.get('BLOB_CONTAINER') or 'images'
