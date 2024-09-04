#!/usr/bin/env python3

"""For basic authentication"""

import base64
from .auth import Auth


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
