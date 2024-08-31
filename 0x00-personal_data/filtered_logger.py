#!/usr/bin/env python3

"""Using re.sub to redact messages"""

import re
from typing import List


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """Returns the provided log message obfuscated"""
    pattern = f"({'|'.join(fields)})=([^;]*)"
    return re.sub(pattern, r'\1=' + redaction, message)
