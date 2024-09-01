#!/usr/bin/env python3

"""Encrypts a password using bcrypt"""

import bcrypt

def hash_password(password: str) -> bytes:
    """Salts, hashes and returns the hashed version of the provided password"""
    as_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()  # salt
    hashed_pwd = bcrypt.hashpw(as_bytes, salt)
    return hashed_pwd
