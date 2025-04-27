# coding: utf-8

import logging

import pytest
from fastapi.testclient import TestClient

import manage


@pytest.fixture
def logger():

    return logging.getLogger(__name__)


@pytest.fixture(scope="session")
def client():

    with TestClient(manage.app) as client:
        yield client


@pytest.fixture(scope="function", autouse=True)
def _auto_debug_true():
    from setting import Setting
    debug = Setting.DEBUG
    Setting.DEBUG = True
    try:
        yield
    finally:
        Setting.DEBUG = debug


@pytest.fixture()
def debug_false():
    from setting import Setting
    debug = Setting.DEBUG
    Setting.DEBUG = False
    try:
        yield
    finally:
        Setting.DEBUG = debug
