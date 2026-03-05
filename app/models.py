from dataclasses import dataclass
from typing import Optional


@dataclass
class Actor:
    id: Optional[int]  # noqa: VNE003 required by task
    first_name: str
    last_name: str
