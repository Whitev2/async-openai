import json
from typing import Optional

from .image_model import ImageModel
from .aiiohttp import AiohttpSession
from .model import Model
from .session import BaseSession
from .token import validate_token


class AsyncOpenAI:
    def __init__(self, token: str, session: Optional[BaseSession] = None) -> None:

        validate_token(token)

        if session is None:
            session = AiohttpSession()

        self.session = session
        self.__token = token

    @property
    def token(self) -> str:
        return self.__token

    async def generate_message(self, message, model: Model):
        session = await self.session.create_session()
        url = self.session.api.api_url()
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + self.__token}
        model.prompt = message

        payload = json.dumps(model.__dict__)

        try:
            async with session.post(url, data=payload, headers=headers) as resp:
                return await resp.json()
        finally:
            await session.close()

    async def generate_image(self, message, model: ImageModel):
        session = await self.session.create_session()
        url = self.session.api.image_url() + '/generations'
        headers = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + self.__token}
        model.prompt = message

        payload = json.dumps(model.__dict__)

        try:
            async with session.post(url, data=payload, headers=headers) as resp:
                return await resp.json()
        finally:
            await session.close()
