import os
from pathlib import Path
from dotenv import load_dotenv


# Environmental variables
env_path = Path(__file__).resolve().parent.parent / '.env'
load_dotenv(dotenv_path=env_path)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY')
ENV = os.getenv('ENV')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_ROOT = Path(__file__).resolve().parent.parent / 'staticfiles'
STATIC_URL = 'static/'

if ENV == 'DEVELOPMENT':
    from .settings_dev import *
elif ENV == 'PRODUCTION':
    from .settings_prod import *
