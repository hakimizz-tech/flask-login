import os

class BaseConfig:
    """Base configuration."""
    DEBUG = False
    TESTING = False
    SECRET_KEY = os.getenv('SECRET_KEY', '824f8f28506eefb2f26b69e0ed4a35b3exit')
    MONGODB_SETTINGS = {
        'host': 'mongodb://localhost:27017/default_db'  # Default database
    }

    def __repr__(self):
        return f"<{self.__class__.__name__}>"

class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG = True
    MONGODB_SETTINGS = {
        **BaseConfig.MONGODB_SETTINGS,  # Inherit base settings
        'db': 'user_auth_db',  # Override database name
        'host': 'mongodb://localhost:27017/user_auth_db'  # Override host
    }

class TestingConfig(BaseConfig):
    """Testing configuration."""
    DEBUG = True
    TESTING = True
    MONGODB_SETTINGS = {
        **BaseConfig.MONGODB_SETTINGS,  # Inherit base settings
        'db': 'user_auth_test_db',  # Override database name
        'host': 'mongodb://localhost:27017/user_auth_test_db'  # Override host
    }

class ProductionConfig(BaseConfig):
    """Production configuration."""
    DEBUG = False
    MONGODB_SETTINGS = {
        **BaseConfig.MONGODB_SETTINGS,  # Inherit base settings
        'db': 'user_auth_prod_db',  # Override database name
        'host': os.getenv('MONGODB_URI', 'mongodb://your_mongodb_host:27017/user_auth_prod_db')  # Use env variable for host
    }

def get_config_by_name(config_name):
    """Get config by name."""
    config_mapping = {
        'development': DevelopmentConfig,
        'production': ProductionConfig,
        'testing': TestingConfig,
    }
    # Default to DevelopmentConfig if config_name is not found
    return config_mapping.get(config_name, DevelopmentConfig)()