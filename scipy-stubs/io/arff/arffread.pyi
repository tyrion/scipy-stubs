# Stubs for scipy.io.arff.arffread (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class ArffError(IOError): ...
class ParseArffError(ArffError): ...

class MetaData:
    name: Any = ...
    _attributes: Any = ...
    _attrnames: Any = ...
    def __init__(self, rel: Any, attr: Any) -> None: ...
    def __repr__(self): ...
    def __iter__(self): ...
    def __getitem__(self, key: Any): ...
    def names(self): ...
    def types(self): ...

def loadarff(f: Any): ...
