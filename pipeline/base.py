from abc import ABC, abstractmethod
from strategies.base import EstrategiaTreino

class PipelineBase(ABC):
    def __init__(self, estrategia: EstrategiaTreino):
        self._estrategia = estrategia

    def executar(self, dados):
        self.validar(dados)
        dados_processados = self.processar(dados)
        return self._estrategia.treinar(dados_processados)

    @abstractmethod
    def validar(self, dados):
        pass

    @abstractmethod
    def processar(self, dados):
        pass
