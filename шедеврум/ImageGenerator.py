from asyncio import sleep, TaskGroup
from json import loads
from aiofiles import open as asyncOpen
from os import path, mkdir
from aiohttp import ClientSession

from Utils import ApiUtils, PublishStatus, UpscaledImage, PendingImages


class ImageGenerator:
    @staticmethod
    async def _discardImageGroup() -> None:
        async with ClientSession() as session:
            async with session.delete(
                url=ApiUtils.discardImageGroup,
                params=ApiUtils.requestParams,
                headers=ApiUtils.requestHeaders
            ) as _:
                return

    @staticmethod
    async def _publishImage(image_id: str) -> PublishStatus:
        async with ClientSession() as session:
            async with session.put(
                url=ApiUtils.publishImage.replace('{{id}}', image_id),
                params=ApiUtils.requestParams,
                json={
                    'tags': []
                },
                headers=ApiUtils.requestHeaders
            ) as response:
                return loads(await response.text())

    @staticmethod
    async def _getImageBytes(url: str) -> bytes:
        async with ClientSession() as session:
            async with session.get(
                url=url,
                headers=ApiUtils.requestHeaders
            ) as response:
                return await response.read()

    @staticmethod
    async def _deleteImage(new_id: str) -> None:
        async with ClientSession() as session:
            async with session.delete(
                url=ApiUtils.deletePost.replace('{{new_id}}', new_id),
                params=ApiUtils.requestParams,
                headers=ApiUtils.requestHeaders
            ) as _:
                return

    async def _getUpscaledImage(self, new_id: str) -> UpscaledImage:
        async with ClientSession() as session:
            async with session.post(
                url=ApiUtils.upscaledStatus,
                params=ApiUtils.requestParams,
                json={
                    'ids': [new_id]
                },
                headers=ApiUtils.requestHeaders
            ) as response:
                await sleep(1)
                return image if (image := loads(await response.text()).get('posts')[0]).get('status') == 'ready' else await self._getUpscaledImage(new_id)

    async def _upscaleImage(self, image_id: str) -> None:
        if not path.exists('images'):
            mkdir('images')
        async with asyncOpen(f'images/{(new_id := (await self._publishImage(image_id)).get("imageID"))}.png', 'wb') as file:
            await file.write(await self._getImageBytes((await self._getUpscaledImage(new_id)).get('url')))
        await self._deleteImage(new_id)

    async def _startImageGeneration(self, prompt: str) -> None:
        await self._discardImageGroup()
        async with ClientSession() as session:
            async with session.post(
                    url=ApiUtils.imageGenerate,
                    params=ApiUtils.requestParams,
                    json={
                        'params': {
                            'prompt': prompt
                        }
                    },
                    headers=ApiUtils.requestHeaders
            ) as _:
                return

    async def _getPreviews(self) -> PendingImages:
        async with ClientSession() as session:
            async with session.get(
                url=ApiUtils.imageGroup,
                params=ApiUtils.requestParams,
                headers=ApiUtils.requestHeaders
            ) as response:
                await sleep(1)
                print(await response.text())
                return r if (r := loads(await response.text())).get('status') == 'pending' else await self._getPreviews()

    async def generateImages(self, prompt: str):
        await self._startImageGeneration(prompt)
        async with TaskGroup() as tg:
            [tg.create_task(self._upscaleImage(image.get('id'))) for image in (await self._getPreviews()).get('images')]
