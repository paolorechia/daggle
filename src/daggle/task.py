from abc import abstractmethod
from typing import Any, Mapping, Optional


class Task:
    def __init__(self, name: Optional[str] = None) -> None:
        self.name = name

        if name is None:
            self.name = self.__class__.__name__

    @abstractmethod
    def run(self, context: Mapping[str, Any]) -> Mapping[str, Any]:
        pass
