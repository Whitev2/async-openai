from dataclasses import dataclass


@dataclass(frozen=True)
class OpenAiAPIServer:
    """
    Base config for API Endpoints
    """

    base: str
    """Base URL"""

    images: str
    """Images URL"""

    embeddings: str
    """Embeddings URL"""

    @classmethod
    def from_base(cls, base: str) -> "OpenAiAPIServer":
        """
        Use this method to auto-generate OpenAiAPIServer instance from base URL

        :param base: Base URL
        :return: instance of :class:`OpenAiAPIServer`
        """
        base = base.rstrip("/")
        return cls(
            base=f"{base}/completions",
            images=f"{base}/images",
            embeddings=f"{base}/embeddings"
        )

    def api_url(self) -> str:
        return self.base

    def image_url(self) -> str:
        return self.images


# Main API server
PRODUCTION = OpenAiAPIServer.from_base("https://api.openai.com/v1")
