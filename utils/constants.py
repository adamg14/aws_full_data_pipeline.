import configparser
import os

parser = configparser.ConfigParser()

parser.read(os.path.join(os.path.dirname(__file__), '../config/config.conf'))

REDDIT_SECRET_KEY = parser.get("api_keys", "secret_key")
REDDIT_CLIENT = parser.get("api_keys", "client_id")
REDDIT_USER_AGENT = "script:adam_etl:v1.0 (by /u/14adam)"

DATABASE_HOST = parser.get("database_credentials", "database_host")
DATABASE_NAME = parser.get("database_credentials", "database_name")
DATABASE_PORT = parser.get("database_credentials", "database_port")
DATABASE_USERNAME = parser.get("database_credentials", "database_username")
DATABASE_PASSWORD = parser.get("database_credentials", "database_password")

REDDIT_POST_FIELDS = (
    'id',
    'url',
    'title',
    'score',
    'num_comments',
    'author',
    'created_utc'
)