#!/usr/bin/env python3
"""Auth class
"""


from typing import List, TypeVar
from flask import Flask, request


class Auth:
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """_summary_
        """
        return False

    def authorization_header(self, request=None) -> str:
        """_summary_
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """_summary_
        """
        return None
