import traceback


class CredentialsException(Exception):
    """Exception raised for credential errors.

    Attributes:
        message -- explanation of the error
        traceback -- traceback of the error
    """

    def __init__(self, message):
        self.message = message
        self.traceback = traceback.format_exc()
        super().__init__(f"{self.message}\n{self.traceback}")
