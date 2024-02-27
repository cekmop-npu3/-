from typing import TypedDict, Literal


__all__ = (
    'UpscaledImage',
    'PublishStatus',
    'PendingImages',
    'TextStatus'
)


class Params(TypedDict):
    prompt: str
    seed: int
    is_experiment: bool


class AttachedImage(TypedDict):
    id: str
    imageURL: str


class TextStatus(TypedDict):
    attachedImages: list[AttachedImage]
    censored: bool
    deprecated: str
    id: str
    maintenanceInProgress: bool
    params: Params
    status: Literal['pending', 'enqueued']
    text: str
    time: int
    title: str


class PendingImage(TypedDict):
    censored: bool
    id: str
    previewURL: str
    status: Literal['pending', 'enqueued']
    url: str


class PendingImages(TypedDict):
    id: str
    images: list[PendingImage]
    params: Params
    status: Literal['pending', 'enqueued']
    time: int
    deprecated: str
    maintenanceInProgress: bool


class PublishUser(TypedDict):
    avatarURL: str
    blockedByMe: bool
    blockedMe: bool
    displayName: str
    id: str
    links: list
    nick: str
    shareLink: str
    subscribed: bool
    verified: bool


class PublishedImage(TypedDict):
    commentsBranchID: str
    commentsCount: int
    createdAt: int
    id: str
    imageStatus: Literal['upscaling', 'ready']
    kind: str
    liked: bool
    likes: int
    params: Params
    pinned: bool
    postURL: str
    status: Literal['upscaling', 'ready']
    tags: list
    translatedPrompt: str
    url: str
    user: PublishUser


class PublishStatus(TypedDict):
    image: PublishedImage
    imageID: str


class UpscaledImage(TypedDict):
    id: str
    kind: str
    status: Literal['upscaling', 'ready']
    url: str
