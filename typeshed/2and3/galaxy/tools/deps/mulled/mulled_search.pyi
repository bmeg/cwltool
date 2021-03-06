# Stubs for galaxy.tools.deps.mulled.mulled_search (Python 3.4)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

requests = ...  # type: Any
Schema = ...  # type: Any
TEXT = ...  # type: Any
STORED = ...  # type: Any
create_in = ...  # type: Any
QueryParser = ...  # type: Any
QUAY_API_URL = ...  # type: str

class QuaySearch:
    index = ...  # type: Any
    organization = ...  # type: Any
    def __init__(self, organization) -> None: ...
    def build_index(self): ...
    def search_repository(self, search_string, non_strict): ...
    def get_additional_repository_information(self, repository_string): ...

def main(argv: Optional[Any] = ...): ...
