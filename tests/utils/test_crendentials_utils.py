import os

from app.utils.credentials_utils import get_credentials

def test_get_credentials():
    credentials = get_credentials()
    assert type(credentials) == dict
    assert type(credentials["type"]) == str
    assert credentials["type"] == os.environ["G_TYPE"]
