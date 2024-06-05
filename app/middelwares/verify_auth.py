import requests
from exceptions.exceptions import CredentialsException


def verify_auth(token):
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
        response = requests.get(
            f"https://oauth2.googleapis.com/tokeninfo?access_token={token}"
        )

        if response.status_code == 200:
            json = response.json()
            if json["email"].endswith("@valere.io") and int(json["expires_in"]) > 0:
                print(json)
                return json
        raise CredentialsException("Invalid token.")
    except ValueError:
        raise CredentialsException("Invalid token.")
