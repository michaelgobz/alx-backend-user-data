#!usr/bin/python3
from typing import List, TypeVar

from flask import request

"""
"""


class Auth(object):
    """
    base auth class
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """

        Args:
            path:
            excluded_paths:
        Returns: bool
        """

    def authorization_header(self, request=None) -> str:
        """

        Args:
            request:
        Returns: String header
        """
    def current_user(self, request=None) -> TypeVar('User'):
        """

        Args:
            request:
        Returns: User
        """

