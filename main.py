from strategies.mock import EstrategiaTreinoMock
from pipeline.concreto import PipelineConcreto

def main():
    dados = {"x": 1, "y": 2}
    estrategia = EstrategiaTreinoMock()
    pipeline = PipelineConcreto(estrategia)

    resultado = pipeline.executar(dados)
    print(resultado)

if __name__ == "__main__":
    main()
