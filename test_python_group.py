# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_python_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="Testgroup", header="Jjsdf", footer="Ijsdjhfjdhb"))
    app.logout()

def test_python_empty_group(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
