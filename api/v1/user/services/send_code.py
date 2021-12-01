import os
import re
import uuid

import requests
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv
import random
import string

from requests.exceptions import ProxyError
from rest_framework.response import Response

load_dotenv()


def make_msg_id():
    left = ''.join(random.choice(string.ascii_lowercase) for _ in range(3))
    right = str(uuid.uuid4().node)
    return left + right


def send_code(recipient: str, text: str):
    is_email = re.findall(r'\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,6}', recipient)
    is_phone = re.findall(r'^[+]?998\d{9}$', recipient)
    if is_phone:
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
        if os.getenv("PRODUCTION") == 'TRUE':
            try:
                response = requests.post(os.getenv("BROKER_URL"),
                                         proxies=proxy,
                                         auth=HTTPBasicAuth(os.getenv("BROKER_USERNAME"),
                                                            os.getenv("BROKER_PASSWORD")),
                                         json=payload)
                return response
            except ProxyError as err:
                return Response({'error': {err}})
        else:
            response = requests.post(os.getenv("BROKER_URL"),
                                     auth=HTTPBasicAuth(os.getenv("BROKER_USERNAME"),
                                                        os.getenv("BROKER_PASSWORD")),
                                     json=payload)
            return response
    elif is_email:
        # send to email
        pass
