from velyx._core import hello_from_bin
from velyx.app.service import MemoryService

# Public alias used in documentation examples
velyxService = MemoryService


def _rust_entry() -> str:
    return hello_from_bin()
