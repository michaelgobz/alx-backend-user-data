#!/usr/bin/env python3
"""
module that Implements the basic auth standard
"""
import base64
import typing

from api.v1.auth import BaseAuth
from models.user import User


class BasicAuth(BaseAuth):
    """
    class Basic Authentication
    """

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """ Base64 authorization

        Args:
            authorization_header:
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        base_val = authorization_header.split(' ')
        return base_val[1]

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """ decode base64 auth header

        Args:
            base64_authorization_header:
        """
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
        """ Extrac the user credentials

        Args:
            decoded_base64_authorization_header:
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        credentials = decoded_base64_authorization_header.split(':', 1)
        return credentials[0], credentials[1]

    def user_object_from_credentials(self, user_email: str, user_pwd: str) -> typing.TypeVar('User'):

        """ returns the User instance based on his email and password

        Args:
            user_email:
            user_pwd:
        """
        if user_email is None or not isinstance(user_email, str):
            return None
        if user_pwd is None or not isinstance(user_pwd, str):
            return None
        try:
            users = User.search({'email': user_email})
            for user in users:
                if user.is_valid_password(user_pwd):
                    return user
        except:
            return None

    def current_user(self, request=None) -> typing.TypeVar('User'):
        """ overloads Auth and retrieves the User instance for a request """
        try:
            header = self.authorization_header(request)
            base64Header = self.extract_base64_authorization_header(header)
            decodeValue = self.decode_base64_authorization_header(base64Header)
            credentials = self.extract_user_credentials(decodeValue)
            user = self.user_object_from_credentials(credentials[0],
                                                     credentials[1])
            return user
        except:
            return None
