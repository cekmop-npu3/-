from .ReadOnly import ReadOnly


class ApiUtils(metaclass=ReadOnly):
    textGenerate = 'https://shedevrum.ai/api/v1/texts/generate'
    discardText = 'https://shedevrum.ai/api/v1/texts/discard'
    textStatus = 'https://shedevrum.ai/api/v1/texts/status'
    imageGenerate = 'https://shedevrum.ai/api/v1/images/generate'
    imageGroup = 'https://shedevrum.ai/api/v1/imagegroup/'
    discardImageGroup = 'https://shedevrum.ai/api/v1/imagegroup/discard'
    publishImage = 'https://shedevrum.ai/api/v1/images/{{id}}/publish'
    upscaledStatus = 'https://shedevrum.ai/api/v1/upscaled_status/get'
    deletePost = 'https://shedevrum.ai/api/v1/posts/{{new_id}}/delete'
    requestHeaders = {
        'user-agent': 'Shedevrum/8.9.0 (Android 7.1.2; samsungSM-G955N)',
        'authorization': 'Oauth 1.1951414010.586436.1739972602.1708436602039.10061508.KLy1EPr8q1jQU_2T.wIxaZpirkHOe330'
                         'ZreM8J8VEbeMETcM8NoZ-J36cGXsM2pTcwT5gFyocwgqFqP83d0WZq8a7nGj2QSbFPJiLU0sQCBeghTGPL5iTTVvgpB'
                         'tNe5Gh.eryyCIvFyHemY2IUMjNUOA'
    }
    requestParams = {
        'appPlatform': 'android',
        'appVersion': '8009000',
        'appVersionName': '8.9.0',
        'uuid': 'f4490cd01602444596fbc67452118375',
        'did': 'e770252c03823edbc747d66cdb4684f5',
        'model': 'samsung SM-G955N',
        'osVersion': '7.1.2',
        'locale': 'ru-RU'
    }
