#!/usr/bin/env python3

"""For basic authentication"""

import base64
from typing import TypeVar
from .auth import Auth
from ....models.user import User


class BasicAuth(Auth):
    """For basic authentication"""

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        """Returns the base64 part of the authorization header"""
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split(' ')[1]

    def decode_base64_authorization_header(
        self, base64_authorization_header: str
    ) -> str:
        """Returns the decoded value of the Base64 string"""
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None
        # should be valid Base64
        try:
            decoded = base64.b64decode(base64_authorization_header).decode(
                'utf-8'
            )
        except base64.binascii.Error:
            return None
        return decoded

    def extract_user_credentials(
        self, decoded_base64_authorization_header: str
    ) -> (str, str):
        """Extracts the users email and password from the
        authorization header
        """
        if decoded_base64_authorization_header is None:
            return None, None
        if not isinstance(decoded_base64_authorization_header, str):
            return None, None
        if ':' not in decoded_base64_authorization_header:
            return None, None
        return tuple(decoded_base64_authorization_header.split(':'))

    def user_object_from_credentials(
        self, user_email: str, user_pwd: str
    ) -> TypeVar('User'):
        """Returns a user object that matched the user_email, if they have a matching
        password as well. Returns None otherwise"""
        if user_email is None or (not isinstance(user_email, str)):
            return None
        if user_pwd is None or (not isinstance(user_pwd, str)):
            return None
        # find a user with this email
        users = User.search({'email': user_email})
        if not users:
            return None
        user = users[0]

        # check the password
        if not user.is_valid_password(user_pwd):
            return None

        return user
