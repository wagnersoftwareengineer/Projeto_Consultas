import os

class Config:
    """Configurações gerais do projeto."""
    SECRET_KEY = os.getenv("SECRET_KEY", "chave_secreta_padrao")
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///consultas.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = os.getenv("DEBUG", True)


class DevelopmentConfig(Config):
    """Configurações específicas para desenvolvimento."""
    DEBUG = True
    SQLALCHEMY_ECHO = True  # Ativa logs das queries SQL para debugging


class ProductionConfig(Config):
    """Configurações específicas para produção."""
    DEBUG = False
    SQLALCHEMY_ECHO = False


# Mapeamento de configurações baseadas em ambiente
config_by_name = {
    "development": DevelopmentConfig,
    "production": ProductionConfig,
}
