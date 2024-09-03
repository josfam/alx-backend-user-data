#!/usr/bin/env python3

"""For api authentication purposes"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Template for all authentication systems to be implemented"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Checks whether the provided path requires authentication"""
        if path is None:
            return True
        if excluded_paths is None or (not excluded_paths):
            return True
        if f"{path.rstrip('/')}/" in excluded_paths:
            return False
        return False

    def authorization_header(self, request=None) -> str:
        """For handling the authorization header"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns the current user"""
        return None
