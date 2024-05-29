from google.oauth2 import service_account
from googleapiclient.discovery import build

from app.utils.credentials_utils import get_credentials

def get_groups():
    """
    Get the groups from the Google Workspace Admin SDK.

    Returns:
        dict: A dictionary with the groups.
    """
    SCOPES = ['https://www.googleapis.com/auth/admin.directory.group']
    SERVICE_ACCOUNT_FILE = get_credentials()

    credentials = service_account.Credentials.from_service_account_info(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    service = build('admin', 'directory_v1', credentials=credentials)

    groups = service.groups().list().execute()

    return groups


def search_user_groups(user_email):
    """
    Search the groups that a user belongs to.

    Args:
        user_email (str): The user email.

    Returns:
        dict: A dictionary with the groups.
    """
    groups = get_groups()

    # ListOfGroups = filter(groups, lambda group: user_email in group['email'])
    # review this line

    print(groups)
    return {"groups": "groups"}
