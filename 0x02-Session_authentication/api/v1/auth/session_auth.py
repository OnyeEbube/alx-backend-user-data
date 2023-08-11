#!/usr/bin/env python3
"""
A class
"""


from .auth import Auth

from models.user import User
from uuid import uuid4


class SessionAuth(Auth):
    """
    Inherits from Auth
    """
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """_summary_
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None

        id = uuid4()
        self.user_id_by_session_id[str(id)] = user_id
        return str(id)
