#!/usr/bin/env python3
"""A function
"""


import bcrypt


def _hash_password(password: str) -> bytes:
    """_summary_
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password
