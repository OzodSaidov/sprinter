import os
import re
import uuid

import requests
from django.core.mail import EmailMultiAlternatives
from django.utils.html import strip_tags
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import random
import string

from requests.exceptions import ProxyError
from rest_framework.response import Response

load_dotenv()


def make_msg_id():
    left = ''.join(random.choice(string.ascii_lowercase) for i in range(3))
    right = str(uuid.uuid4().node)
    return left + right


def send_code(recipient: str, text: str):
    response = {'Error': 'The input data is incorrect'}
    if re.findall(r'^+?998\d{9}$', recipient):  # Send to phone
        message_id = make_msg_id()
        originator = "3700"
        payload = {
            "messages": [
                {
                    "recipient": recipient,
                    "message-id": message_id,
                    "sms": {
                        "originator": originator,
                        "content": {
                            "text": text
                        }
                    }
                }
            ]
        }
        http_proxy = os.getenv('HTTP_PROXY')
        proxy = {"http": http_proxy}
        if os.getenv("PRODUCTION"):
            try:
                response = requests.post(os.getenv("BROKER_URL"),
                                         proxies=proxy,
                                         auth=HTTPBasicAuth(os.getenv("BROKER_USERNAME"),
                                                            os.getenv("BROKER_PASSWORD")),
                                         json=payload)
            except ProxyError as err:
                return Response({'error': {err}})
        else:
            response = requests.post(os.getenv("BROKER_URL"),
                                     auth=HTTPBasicAuth(os.getenv("BROKER_USERNAME"),
                                                        os.getenv("BROKER_PASSWORD")),
                                     json=payload)
    elif re.findall(r'\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,6}', recipient):  # Send to email
        html_content = ''
        plain_content = strip_tags(html_content)
        email = EmailMultiAlternatives(
            subject='That’s your subject',
            body=plain_content,
            from_email=os.getenv('EMAIL_HOST'),
            to=[recipient],
        )
        email.attach_alternative(html_content, 'text/html')
        return email.send()

    return response
