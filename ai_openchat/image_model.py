class ImageModel:
    def __init__(
            self,
            prompt: str = None,
            n: int = None,
            size: str = None,

    ):
        self.size = size
        self.n = n
        self.prompt: str = prompt

    def image(self):
        self.size = "1024x1024"
        self.n = 1
        return self
