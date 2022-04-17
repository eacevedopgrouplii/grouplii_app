
from functools import lru_cache
from fastapi_mail import ConnectionConfig
from pathlib import Path
from . import config

@lru_cache()
def get_settings():
    return config.Settings()

conf = ConnectionConfig(
    MAIL_USERNAME = get_settings().MAIL_USERNAME,
    MAIL_PASSWORD = get_settings().MAIL_PASSWORD,
    MAIL_FROM = get_settings().MAIL_FROM,
    MAIL_PORT = get_settings().MAIL_PORT,
    MAIL_SERVER = get_settings().MAIL_SERVER,    
    MAIL_TLS = True,
    MAIL_SSL = False,
    TEMPLATE_FOLDER = Path(__file__).parent / 'templates'
)