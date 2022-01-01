from rest_framework.request import Request

from sprinter_settings import settings


def get_image_endpoint(request: Request) -> str:
    return "%s://%s%s" % (request.scheme, request.get_host(), settings.MEDIA_URL)
