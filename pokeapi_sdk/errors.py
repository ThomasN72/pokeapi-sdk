import requests


class SDKError(Exception):

    message: str
    status_code: int
    body: str
    raw_response: requests.Response

    def __init__(self, message: str, status_code: int, body: str, raw_response: requests.Response):
        self.message = message
        self.status_code = status_code
        self.body = body
        self.raw_response = raw_response

    def __str__(self):
        body = ""
        if len(self.body) > 0:
            body = f"\n{self.body}"

        return f"{self.message}: Status {self.status_code}{body}"


class PokeAPIError(Exception):
    """Custom exception for PokeAPI errors."""

    pass


class PokemonNotFoundError(SDKError):
    """Exception raised when a specific Pokémon is not found."""

    def __init__(self, message="Pokémon not found", status_code=404, body="", raw_response=None):
        super().__init__(message, status_code, body, raw_response)
