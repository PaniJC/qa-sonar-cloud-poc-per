import requests
import logging
from ddtrace import tracer
from exceptions.Credentials_execptions import CredentialsException
from utils.logger_util import log_info, log_error, log_warning


FORMAT = ('%(asctime)s %(levelname)s [%(name)s] [%(filename)s:%(lineno)d] '
          '[dd.service=%(dd.service)s dd.env=%(dd.env)s dd.version=%(dd.version)s dd.trace_id=%(dd.trace_id)s dd.span_id=%(dd.span_id)s] '
          '- %(message)s')
logging.basicConfig(format=FORMAT)
log = logging.getLogger(__name__)
log.level = logging.INFO

@tracer.wrap() 
def verify_auth(token: str):
    """
    Verifies the authenticity of a token by making a request to the Google OAuth2 API.

    Args:
        token (str): The access token to be verified.

    Returns:
        dict: A dictionary containing the result of the token verification. If the token
        is valid and belongs to an email ending with "@valere.io", the dictionary will
        have the key "isValid" set to True. Otherwise, if the token is invalid,
        the dictionary will have the key "error" set to "Invalid token.".

    Raises:
        None

    """
    try:
        log.info('Init the function verify_auth')
        response = requests.get(
            f"https://oauth2.googleapis.com/tokeninfo?access_token={token}"
        )

        log.info('Response from Google OAuth2 API: %s', response)
        if response.status_code == 200:
            json = response.json()
            if json["email"].endswith("@valere.io") and int(json["expires_in"]) > 0:
                return json
        
        raise CredentialsException("Invalid token.")
    except ValueError:
        
        raise CredentialsException("Invalid token.")
