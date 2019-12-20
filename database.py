from orator import DatabaseManager, Model
import settings
from os import environ

config = {
    'mysql': {
        'driver': 'postgres',
        'host': environ.get('DB_HOST'),
        'database': environ.get('DB_NAME'),
        'user': environ.get('DB_USER'),
        'password': environ.get('DB_PASSWORD'),
        'prefix': ''
    }
}

db = DatabaseManager(config)
Model.set_connection_resolver(db)