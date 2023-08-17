#!/usr/bin/env python3
"""A function
"""


import bcrypt
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


from typing import Union


def _hash_password(password: str) -> str:
    """_summary_
    """
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    return hashed_password


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """_summary_
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> Union[None, User]:
        """_summary_
        """
        try:
            self._db.find_user_by(email=email)
        except NoResultFound:
            return self._db.add_user(email, _hash_password(password))

        else:
            raise ValueError('User {} already exists'.format(email))
