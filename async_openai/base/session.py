import abc
from typing import Final

from async_openai.base.openai import OpenAiAPIServer, PRODUCTION

DEFAULT_TIMEOUT: Final[float] = 60.0


class BaseSession(abc.ABC):
    def __init__(
        self,
        api: OpenAiAPIServer = PRODUCTION,
        timeout: float = DEFAULT_TIMEOUT,
    ) -> None:

        self.api = api
        self.timeout = timeout
