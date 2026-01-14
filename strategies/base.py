from abc import ABC, abstractmethod
from typing import Any

class EstrategiaTreino(ABC):
    @abstractmethod
    def treinar(self, dados) -> Any:
        pass
