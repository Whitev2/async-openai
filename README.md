<hr/>

![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=40&pause=1000&color=373737&background=91C5F4&center=true&vCenter=true&multiline=true&width=1080&height=80&lines=Python+async+module+for+OpenAI)
<hr/>

## Technologies
- Python >= 3.8;
- aiohttp >= 3.8


## quick start

1. Example #1 Chat:

``` python
import asyncio

from async_openai import AsyncOpenAI
from async_openai.base.model import Model


async def chat():
    openai_client = AsyncOpenAI(token='API-KEY')
    resp = await openai_client.send_message('Your request?', Model().chat())
    print(resp)


if __name__ == '__main__':
    asyncio.run(chat())
```

2. Example #2 Movie to Emoji:
``` python
import asyncio

from async_openai import AsyncOpenAI
from async_openai.base.model import Model


async def chat():
    openai_client = AsyncOpenAI(token='API-KEY')
    resp = await openai_client.send_message('Convert movie titles into emoji.\n\n'
                                            'Back to the Future: 👨👴🚗🕒 \n'
                                            'Batman: 🤵🦇 \n'
                                            'Transformers: 🚗🤖 \n'
                                            'Star Wars:', Model().movie_to_emoji())
    print(resp)
    # ⭐️⚔️


if __name__ == '__main__':
    asyncio.run(chat())


```

<hr/>
This project is an attempt to make an asynchronous library for convenient OpenAI management.
You can check out the rest of the models here: https://beta.openai.com/examples.

I continue to develop it and will soon add image generation

