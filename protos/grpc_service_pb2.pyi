from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Long(_message.Message):
    __slots__ = ("n",)
    N_FIELD_NUMBER: _ClassVar[int]
    n: int
    def __init__(self, n: _Optional[int] = ...) -> None: ...

class String(_message.Message):
    __slots__ = ("n",)
    N_FIELD_NUMBER: _ClassVar[int]
    n: str
    def __init__(self, n: _Optional[str] = ...) -> None: ...

class LongBatch(_message.Message):
    __slots__ = ("n1", "n2", "n3", "n4", "n5", "n6", "n7", "n8")
    N1_FIELD_NUMBER: _ClassVar[int]
    N2_FIELD_NUMBER: _ClassVar[int]
    N3_FIELD_NUMBER: _ClassVar[int]
    N4_FIELD_NUMBER: _ClassVar[int]
    N5_FIELD_NUMBER: _ClassVar[int]
    N6_FIELD_NUMBER: _ClassVar[int]
    N7_FIELD_NUMBER: _ClassVar[int]
    N8_FIELD_NUMBER: _ClassVar[int]
    n1: int
    n2: int
    n3: int
    n4: int
    n5: int
    n6: int
    n7: int
    n8: int
    def __init__(self, n1: _Optional[int] = ..., n2: _Optional[int] = ..., n3: _Optional[int] = ..., n4: _Optional[int] = ..., n5: _Optional[int] = ..., n6: _Optional[int] = ..., n7: _Optional[int] = ..., n8: _Optional[int] = ...) -> None: ...

class Void(_message.Message):
    __slots__ = ()
    def __init__(self) -> None: ...
