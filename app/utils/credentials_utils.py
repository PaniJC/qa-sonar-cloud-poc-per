import os
from dotenv import load_dotenv

load_dotenv()

def get_credentials():
    return {
        "type": os.environ['G_TYPE'],
        "project_id": os.environ['G_PROJECT_ID'],
        "private_key_id": os.environ['G_PRIVATE_KEY_ID'],
        "private_key": os.environ['G_PRIVATE_KEY'],
        "client_email": os.environ['G_CLIENT_EMAIL'],
        "client_id": os.environ['G_CLIENT_ID'],
        "auth_uri": os.environ['G_AUTH_URI'],
        "token_uri": os.environ['G_TOKEN_URI'],
        "auth_provider_x509_cert_url": os.environ['G_AUTH_PROVIDER_X509_CERT_URL'],
        "client_x509_cert_url": os.environ['G_CLIENT_X509_CERT_URL'],
        "universe_domain": os.environ['G_UNIVERSE_DOMAIN']
    }