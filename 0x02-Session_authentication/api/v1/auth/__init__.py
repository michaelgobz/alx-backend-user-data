#!/usr/bin/env python3
"""
Auth is the base class init
"""
from api.v1.auth.auth import Auth
from api.v1.auth.session_auth import SessionAuth


BaseAuth = Auth
SessionAuthBase = SessionAuth
