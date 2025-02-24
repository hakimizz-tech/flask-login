import unittest
import json

from app.modules.reset_password.controller import Reset_passwordController


def test_index():
    reset_password_controller = Reset_passwordController()
    result = reset_password_controller.index()
    assert result == {'message': 'Hello, World!'}
