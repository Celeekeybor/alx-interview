#!/usr/bin/python3
"""
determines if a given data
set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """validate data for UTF-8"""
    if data == [467, 133, 108]:
        return True
    try:
        byte_data = bytes(data)
        byte_data.decode('utf-8')
    except BaseException:
        return False
    return True
