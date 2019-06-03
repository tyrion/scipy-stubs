# Stubs for scipy.io.matlab.mio4 (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .mio_utils import chars_to_strings, squeeze_element
from .miobase import MatFileReader, arr_dtype_number, arr_to_chars, convert_dtypes, docfiller, matdims, read_dtype
from typing import Any, Optional

SYS_LITTLE_ENDIAN: Any
miDOUBLE: int
miSINGLE: int
miINT32: int
miINT16: int
miUINT16: int
miUINT8: int
mdtypes_template: Any
np_to_mtypes: Any
mxFULL_CLASS: int
mxCHAR_CLASS: int
mxSPARSE_CLASS: int
order_codes: Any
mclass_info: Any

class VarHeader4:
    is_logical: bool = ...
    is_global: bool = ...
    name: Any = ...
    dtype: Any = ...
    mclass: Any = ...
    dims: Any = ...
    is_complex: Any = ...
    def __init__(self, name: Any, dtype: Any, mclass: Any, dims: Any, is_complex: Any) -> None: ...

class VarReader4:
    file_reader: Any = ...
    mat_stream: Any = ...
    dtypes: Any = ...
    chars_as_strings: Any = ...
    squeeze_me: Any = ...
    def __init__(self, file_reader: Any) -> None: ...
    def read_header(self): ...
    def array_from_header(self, hdr: Any, process: bool = ...): ...
    def read_sub_array(self, hdr: Any, copy: bool = ...): ...
    def read_full_array(self, hdr: Any): ...
    def read_char_array(self, hdr: Any): ...
    def read_sparse_array(self, hdr: Any): ...
    def shape_from_header(self, hdr: Any): ...

class MatFile4Reader(MatFileReader):
    _matrix_reader: Any = ...
    def __init__(self, mat_stream: Any, *args: Any, **kwargs: Any) -> None: ...
    def guess_byte_order(self): ...
    dtypes: Any = ...
    def initialize_read(self) -> None: ...
    def read_var_header(self): ...
    def read_var_array(self, header: Any, process: bool = ...): ...
    def get_variables(self, variable_names: Optional[Any] = ...): ...
    def list_variables(self): ...

def arr_to_2d(arr: Any, oned_as: str = ...): ...

class VarWriter4:
    file_stream: Any = ...
    oned_as: Any = ...
    def __init__(self, file_writer: Any) -> None: ...
    def write_bytes(self, arr: Any) -> None: ...
    def write_string(self, s: Any) -> None: ...
    def write_header(self, name: Any, shape: Any, P: Any = ..., T: Any = ..., imagf: int = ...) -> None: ...
    def write(self, arr: Any, name: Any): ...
    def write_numeric(self, arr: Any, name: Any) -> None: ...
    def write_char(self, arr: Any, name: Any) -> None: ...
    def write_sparse(self, arr: Any, name: Any) -> None: ...

class MatFile4Writer:
    file_stream: Any = ...
    oned_as: Any = ...
    _matrix_writer: Any = ...
    def __init__(self, file_stream: Any, oned_as: Optional[Any] = ...) -> None: ...
    def put_variables(self, mdict: Any, write_header: Optional[Any] = ...) -> None: ...
