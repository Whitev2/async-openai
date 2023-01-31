<hr/>

![Typing SVG](https://readme-typing-svg.herokuapp.com?font=Fira+Code&size=40&pause=1000&color=373737&background=91C5F4&center=true&vCenter=true&multiline=true&width=1080&height=80&lines=Python+async+module+for+OpenAI)
<hr/>

### Installation - pip install ai-openchat


## Chat

1. Example #1 Chat:

``` python
import asyncio

from ai_openchat import Model, AsyncOpenAI


async def chat():
    openai_client = AsyncOpenAI(token='API-KEY')
    resp = await openai_client.generate_message('Your request?', Model().chat())
    print(resp)


if __name__ == '__main__':
    asyncio.run(chat())
```

2. Example #2 Movie to Emoji:
``` python
import asyncio

from ai_openchat import Model, AsyncOpenAI


async def movie_to_emoji():
    openai_client = AsyncOpenAI(token='API-KEY')
    resp = await openai_client.generate_message('Convert movie titles into emoji.\n\n'
                                            'Back to the Future: 👨👴🚗🕒 \n'
                                            'Batman: 🤵🦇 \n'
                                            'Transformers: 🚗🤖 \n'
                                            'Star Wars:', Model().movie_to_emoji())
    print(resp)
    # ⭐️⚔️


if __name__ == '__main__':
    asyncio.run(movie_to_emoji())


```

3. Example #3 Custom chat

``` python
import asyncio

from ai_openchat import Model, AsyncOpenAI


async def custom_chat():
    
    custom_model = Model(
        model="code-davinci-002",
        temperature=0,
        max_tokens=100,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        stop=["You:"]
    )

    openai_client = AsyncOpenAI(token='API-KEY')
    resp = await openai_client.generate_message('Hello!', custom_model)
    print(resp)


if __name__ == '__main__':
    asyncio.run(custom_chat())
```

## Image

1. Generate Image

``` python
import asyncio

from ai_openchat import ImageModel, AsyncOpenAI


async def image_generator():
    openai_client = AsyncOpenAI(token='API-KEY')
    resp = await openai_client.generate_image('Captain America', ImageModel().image())
    print(resp)


if __name__ == '__main__':
    asyncio.run(image_generator())
```

2. Generate custom Image


``` python
import asyncio

from ai_openchat import ImageModel, AsyncOpenAI


async def image_generator():

    custom_model = ImageModel(n=1, size="1024x1024")

    openai_client = AsyncOpenAI(token='API-KEY')
    resp = await openai_client.generate_image('Captain America', custom_model)
    print(resp)


if __name__ == '__main__':
    asyncio.run(image_generator())
```


<hr/>
This project is an attempt to make an asynchronous library for convenient OpenAI management.
You can check out the rest of the models here: https://beta.openai.com/examples.


## Technologies
- Python >= 3.8;
- aiohttp >= 3.8
