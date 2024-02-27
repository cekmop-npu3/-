from functools import partial
from typing import Any


class ReadOnly(type):

    class PreparedDict(dict):
        def __setitem__(self, key: str, value: Any) -> None:
            if not key.startswith('__'):
                setattr(ReadOnly, f'__{key}', value)
                setattr(ReadOnly, f'{key}', property(
                    fget=partial(ReadOnly.get_item, key),
                    fset=partial(ReadOnly.set_item, key)
                ))
            super().__setitem__(key, value)

    @staticmethod
    def get_item(key: str, _) -> Any:
        return getattr(ReadOnly, f'__{key}')

    @staticmethod
    def set_item(key: str, *_):
        raise AttributeError(f'Cannot reassign {key}')

    def __new__(mcs, name, bases, attrs):
        return super().__new__(mcs, name, bases, attrs)

    @classmethod
    def __prepare__(mcs, name, bases) -> PreparedDict:
        return mcs.PreparedDict()
