from django.db.models import Func
from dotenv import load_dotenv
import os

from sprinter_settings.settings import BASE_DIR

load_dotenv(dotenv_path=BASE_DIR / '.env')


class Round(Func):
    function = 'ROUND'
    if os.getenv('PRODUCTION') == 'TRUE':
        template = '%(function)s(%(expressions)s::numeric, 2)'
    else:
        template = '%(function)s(%(expressions)s, 2)'
