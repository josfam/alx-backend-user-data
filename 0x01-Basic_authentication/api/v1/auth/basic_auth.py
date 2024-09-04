#!/usr/bin/env python3

"""For basic authentication"""

from .auth import Auth


class BasicAuth(Auth):
    """For basic authentication"""

    def extract_base64_authorization_header(
        self, authorization_header: str
    ) -> str:
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header.split(' ')[1]
