import requests

from ddtrace import tracer
from exceptions.Credentials_execptions import CredentialsException
from utils.logger_util import log_info, log_error, log_warning

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
        log_info("Verifying token.")
        response = requests.get(
            f"https://oauth2.googleapis.com/tokeninfo?access_token={token}"
        )

        log_info(f"Token verification response: {response.json()}")
        if response.status_code == 200:
            json = response.json()
            if json["email"].endswith("@valere.io") and int(json["expires_in"]) > 0:
                return json
        log_warning("Invalid token.")
        raise CredentialsException("Invalid token.")
    except ValueError:
        log_error("Error in to request the token.")
        raise CredentialsException("Invalid token.")
