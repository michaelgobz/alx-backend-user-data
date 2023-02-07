#!usr/bin/python3
import base64
import typing

from api.v1.auth import BaseAuth

"""

"""


class BasicAuth(BaseAuth):
    """
    Basic Authentication
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ Base64 authorization"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        base_val = authorization_header.split(' ')
        return base_val[1]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        try:
            base64encode = base64_authorization_header.encode('utf-8')
            base64decode = base64.b64encode(base64encode)
            return base64decode.decode('utf-8')

        except"Not valid Base64 encode":
            return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str) -> typing.Tuple[str, str]:
        """"""
        if decoded_base64_authorization_header is None:
            return None,None
        if not isinstance(decoded_base64_authorization_header, str):
            return None,None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        credentials = decoded_base64_authorization_header.split(':', 1)
        return credentials[0], credentials[1]


