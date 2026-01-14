from .base import EstrategiaTreino

class EstrategiaTreinoMock(EstrategiaTreino):
    def treinar(self, dados) -> str:
        return 'fake result'
