from functools import lru_cache


class TokenValidationError(Exception):
    pass


@lru_cache()
def validate_token(token: str) -> bool:
    """
    Validate openAI token

    :param token:
    :return:
    """
    if not isinstance(token, str):
        raise TokenValidationError(
            f"Token is invalid! It must be 'str' type instead of {type(token)} type."
        )

    if any(x.isspace() for x in token):
        message = "Token is invalid! It can't contains spaces."
        raise TokenValidationError(message)

    return True