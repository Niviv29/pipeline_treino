# Pipeline de treino com Strategy e Template Method
Este projeto visa construir uma pipeline de treinamento usando Programação Orientada a Objetos com foco no design e **não** exatamente em modelos específicos de Machine Learning.

Objetificando a procura por:

- Mudanças em estratégias sem quebra do código
- Fluxo consistente
- Projeto sem necessidade de dados reais

A arquitetura se dá pelas bases:

1. Comportamento variável:
    Define o contrato e possibilita a mudança de comportamento sem a necessidade de interferir na pipeline.
 - 'TreinoRapido' e 'TreinoCompleto' são os exemplos utilizados

2. Fluxo invariável:
   Foco na pipeline base, garantindo consistência e inviabilizando a quebra do fluxo pré estabelecido.

4. Injeção de Dependência:
    A estratégia é baseada no construtor, facilitando testes.



