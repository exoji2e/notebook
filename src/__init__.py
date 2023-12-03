__all__ = [
    "datastructures",
    "misc",
]
import os as _os


for _s in ('datastructures', 'graphs', 'misc'):
    __path__.append(_os.path.join(_os.path.dirname(__file__), _s))