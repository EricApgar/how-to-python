from typing import TYPE_CHECKING


__all__ = [
    'multiply',
    'square',
    'Math'
]


def __getattr__(name: str):
    if name == 'multiply':
        from .multiplication.helper import multiply
        return multiply
    elif name == 'square':
        from .exponents.helper import square
    elif name == 'Math':
        from .math import Math
    else:
        raise AttributeError(f'Module "lib_template" has no attribute {name!r}!')