#!/usr/bin/env python3
"""
Class for the authentication module
"""
from typing import List, TypeVar

from flask import request
import os


class Auth(object):
    """
    authentication base class
    """
    @staticmethod
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        require authorization
        Args:
            path:
            excluded_paths:
        Returns: bool
        """
        if path is None or excluded_paths is None or not len(excluded_paths):
            return True

        if path[-1] != '/':
            path += '/'
        for i in excluded_paths:
            if i.endswith('*'):
                if path.startswith(i[:1]):
                    return False
            if path in excluded_paths:
                return False
            else:
                return True

    @staticmethod
    def authorization_header(self, request=None) -> str:
        """
        check for the auth headers
        Args:
            request:
        Returns: String header
        """
        if request is None:
            return None
        if not request.headers.get('Authorization'):
            return None
        return request.headers.get('Authorization')

    @staticmethod
    def current_user(request=None) -> TypeVar('User'):
        """
        current users
        Args:
            request:
        Returns: None
        """
        return None
    
    def session_cookie(self, request=None):
        if request is None:
            return None
        else:
            _my_session_id  = os.getenv('SESSION_NAME')
            return request.cookies.get(_my_session_id)
