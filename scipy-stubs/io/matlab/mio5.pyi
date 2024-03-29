# Stubs for scipy.io.matlab.mio5 (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from .byteordercodes import native_code, swapped_code
from .mio5_params import MDTYPES, MatlabFunction, MatlabObject, NP_TO_MTYPES, NP_TO_MXTYPES, mclass_info, miCOMPRESSED, miINT8, miMATRIX, miUINT32, miUTF8, mxCELL_CLASS, mxCHAR_CLASS, mxDOUBLE_CLASS, mxOBJECT_CLASS, mxSPARSE_CLASS, mxSTRUCT_CLASS
from .mio5_utils import VarReader5
from .miobase import MatFileReader, MatReadError, MatReadWarning, MatWriteError, arr_dtype_number, arr_to_chars, docfiller, matdims, read_dtype
from .streams import ZlibInputStream
from typing import Any, Optional

class MatFile5Reader(MatFileReader):
    uint16_codec: Any = ...
    _file_reader: Any = ...
    _matrix_reader: Any = ...
    def __init__(self, mat_stream: Any, byte_order: Optional[Any] = ..., mat_dtype: bool = ..., squeeze_me: bool = ..., chars_as_strings: bool = ..., matlab_compatible: bool = ..., struct_as_record: bool = ..., verify_compressed_data_integrity: bool = ..., uint16_codec: Optional[Any] = ...) -> None: ...
    def guess_byte_order(self): ...
    def read_file_header(self): ...
    def initialize_read(self) -> None: ...
    def read_var_header(self): ...
    def read_var_array(self, header: Any, process: bool = ...): ...
    def get_variables(self, variable_names: Optional[Any] = ...): ...
    def list_variables(self): ...

def varmats_from_mat(file_obj: Any): ...

class EmptyStructMarker: ...

def to_writeable(source: Any): ...

NDT_FILE_HDR: Any
NDT_TAG_FULL: Any
NDT_TAG_SMALL: Any
NDT_ARRAY_FLAGS: Any

class VarWriter5:
    mat_tag: Any = ...
    file_stream: Any = ...
    unicode_strings: Any = ...
    long_field_names: Any = ...
    oned_as: Any = ...
    _var_name: Any = ...
    _var_is_global: bool = ...
    def __init__(self, file_writer: Any) -> None: ...
    def write_bytes(self, arr: Any) -> None: ...
    def write_string(self, s: Any) -> None: ...
    def write_element(self, arr: Any, mdtype: Optional[Any] = ...) -> None: ...
    def write_smalldata_element(self, arr: Any, mdtype: Any, byte_count: Any) -> None: ...
    def write_regular_element(self, arr: Any, mdtype: Any, byte_count: Any) -> None: ...
    _mat_tag_pos: Any = ...
    def write_header(self, shape: Any, mclass: Any, is_complex: bool = ..., is_logical: bool = ..., nzmax: int = ...) -> None: ...
    def update_matrix_tag(self, start_pos: Any) -> None: ...
    def write_top(self, arr: Any, name: Any, is_global: Any) -> None: ...
    def write(self, arr: Any): ...
    def write_numeric(self, arr: Any) -> None: ...
    def write_char(self, arr: Any, codec: str = ...): ...
    def write_sparse(self, arr: Any) -> None: ...
    def write_cells(self, arr: Any) -> None: ...
    def write_empty_struct(self) -> None: ...
    def write_struct(self, arr: Any) -> None: ...
    def _write_items(self, arr: Any) -> None: ...
    def write_object(self, arr: Any) -> None: ...

class MatFile5Writer:
    file_stream: Any = ...
    do_compression: Any = ...
    unicode_strings: Any = ...
    global_vars: Any = ...
    long_field_names: Any = ...
    oned_as: Any = ...
    _matrix_writer: Any = ...
    def __init__(self, file_stream: Any, do_compression: bool = ..., unicode_strings: bool = ..., global_vars: Optional[Any] = ..., long_field_names: bool = ..., oned_as: str = ...) -> None: ...
    def write_file_header(self) -> None: ...
    def put_variables(self, mdict: Any, write_header: Optional[Any] = ...) -> None: ...
