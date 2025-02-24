
from mongoengine.connection import connect

def initialize_db(app):
    # Connect to MongoDB using the Flask app's configuration
    connect(
        db=app.config['MONGODB_SETTINGS']['db'],
        host= 'localhost',
        port = 27017,
        uuidRepresentation='standard',
    )
 