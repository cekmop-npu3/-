from asyncio import sleep
from aiohttp import ClientSession
from json import loads

from Utils import ApiUtils, TextStatus


class TextGenerator:
    @staticmethod
    async def _discardText() -> None:
        async with ClientSession() as session:
            async with session.delete(
                    url=ApiUtils.discardText,
                    params=ApiUtils.requestParams,
                    headers=ApiUtils.requestHeaders
            ) as _:
                return

    async def generateText(self, prompt: str):
        await self._discardText()
        async with ClientSession() as session:
            async with session.post(
                url=ApiUtils.textGenerate,
                params=ApiUtils.requestParams,
                json={
                    'params': {
                        'prompt': prompt
                    }
                },
                headers=ApiUtils.requestHeaders
            ) as _:
                return (await self._getText()).get('text')

    async def _getText(self) -> TextStatus:
        async with ClientSession() as session:
            async with session.get(
                url=ApiUtils.textStatus,
                params=ApiUtils.requestParams,
                headers=ApiUtils.requestHeaders
            ) as response:
                await sleep(1)
                return r if (r := loads(await response.text())).get('status') == 'pending' else await self._getText()
