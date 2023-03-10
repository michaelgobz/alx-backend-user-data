#!/usr/bin/env python3
"""
Class for the authentication module
"""
from typing import List, TypeVar

from flask import request


class Auth(object):
    """
    authentication base class
    """
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

    def authorization_header(self, req=None) -> str:
        """
        check for the auth headers
        Args:
            req:
        Returns: String header
        """
        if req is None:
            return None
        if not req.headers.get('Authorization'):
            return None
        return req.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        current users
        Args:
            request:
        Returns: None
        """
        return None
