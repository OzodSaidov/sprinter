from email.mime.image import MIMEImage
from functools import lru_cache


@lru_cache()
def logo_data():
    with open('/home/ozod/PycharmProjects/sprinter/static/assets/images/brand_sprinter/Tagline_version_Dark.png',
              'rb') as f:
        l_data = f.read()
    logo = MIMEImage(l_data)
    logo.add_header('Content-ID', '<logo>')
    return logo
