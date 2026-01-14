from .base import PipelineBase

class PipelineConcreto(PipelineBase):
    def validar(self, dados):
        if dados is None:
            raise ValueError("Dados inválidos")
        if not isinstance(dados, dict):
            raise TypeError("Dados devem ser um dicionário")

    def processar(self, dados):
        return dados.copy()
