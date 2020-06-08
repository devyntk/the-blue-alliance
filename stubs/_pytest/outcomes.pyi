from typing import Any, NoReturn, Optional
from typing_extensions import Protocol as Protocol

TYPE_CHECKING: bool

class OutcomeException(BaseException):
    msg: Any = ...
    pytrace: Any = ...
    def __init__(self, msg: Optional[str]=..., pytrace: bool=...) -> None: ...

TEST_OUTCOME: Any

class Skipped(OutcomeException):
    __module__: str = ...
    allow_module_level: Any = ...
    def __init__(self, msg: Optional[str]=..., pytrace: bool=..., allow_module_level: bool=...) -> None: ...

class Failed(OutcomeException):
    __module__: str = ...

class Exit(Exception):
    msg: Any = ...
    returncode: Any = ...
    def __init__(self, msg: str=..., returncode: Optional[int]=...) -> None: ...

class _WithException:
    Exception: _ET = ...
    __call__: _F = ...

def exit(msg: str, returncode: Optional[int]=...) -> NoReturn: ...
def skip(msg: str=..., *, allow_module_level: bool=...) -> NoReturn: ...
def fail(msg: str=..., pytrace: bool=...) -> NoReturn: ...

class XFailed(Failed): ...

def xfail(reason: str=...) -> NoReturn: ...
def importorskip(modname: str, minversion: Optional[str]=..., reason: Optional[str]=...) -> Any: ...