#!/usr/bin/env python3

"""Using re.sub to redact messages"""

import re
import logging
from typing import List, Tuple

PII_FIELDS: Tuple[str] = ('email', 'phone', 'ssn', 'password', 'name')


class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Formats the provided record while redacting information in the
        fields
        """
        record.msg = filter_datum(
            self.fields, self.REDACTION, record.msg, self.SEPARATOR
        )
        return super().format(record)


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """Returns the provided log message obfuscated"""
    pattern = f"({'|'.join(fields)})=([^;]*)"
    return re.sub(pattern, r'\1=' + redaction, message)


def get_logger() -> logging.Logger:
    """Returns a logger object"""
    logger = logging.Logger(name='user_data', level=logging.INFO)
    logger.propagate = False
    stream_handler = logging.StreamHandler(
        RedactingFormatter(list(PII_FIELDS))
    )
    logger.addHandler(stream_handler)
    return logger
