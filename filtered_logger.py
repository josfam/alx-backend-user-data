#!/usr/bin/env python3

import re

def filter_datum(fields, redaction, message, separator):
    """Returns the provided log message obfuscated"""
    for field in fields:
        for part in message.split(separator):
            if part.startswith(field):
                message = re.sub(part.split('=')[1], redaction, message)
    return message
