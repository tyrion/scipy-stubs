# Stubs for scipy._lib.six (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

import __builtin__
from typing import Any, Optional

__author__: str
__version__: str
PY3: Any
string_types: Any
integer_types: Any
class_types: Any
text_type = str
binary_type = bytes
MAXSIZE: Any
text_type = unicode
binary_type = str

class X:
    def __len__(self): ...

def _add_doc(func: Any, doc: Any) -> None: ...
def _import_module(name: Any): ...

reduce: Any
zip: Any
xrange: Any
builtins = __builtin__
_meth_func: str
_meth_self: str
_func_code: str
_func_defaults: str
_iterkeys: str
_itervalues: str
_iteritems: str
advance_iterator = next
next = advance_iterator

def get_unbound_function(unbound: Any): ...
Iterator = object

def callable(obj: Any): ...

class Iterator:
    def next(self): ...
callable = callable
get_method_function: Any
get_method_self: Any
get_function_code: Any
get_function_defaults: Any

def iterkeys(d: Any): ...
def itervalues(d: Any): ...
def iteritems(d: Any): ...
def b(s: Any): ...
def u(s: Any): ...
def int2byte(i: Any): ...

int2byte: Any
StringIO: Any
BytesIO: Any
int2byte = chr
exec_: Any

def reraise(tp: Any, value: Any, tb: Optional[Any] = ...) -> None: ...

print_: Any

def with_metaclass(meta: Any, base: Any = ...): ...
