#!/usr/bin/env python3

"""Using re.sub to redact messages"""

import re
from typing import List

def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """Returns the provided log message obfuscated"""
    for field in fields:
        for part in message.split(separator):
            if part.startswith(field):
                message = re.sub(part.split('=')[1], redaction, message)
    return message
