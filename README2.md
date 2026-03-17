Requisitos Funcionais:
RF01: O sistema deve validar se a lista de notas do aluno está vazia ou corrompida.
RF02: O sistema deve calcular a média das notas válidas de cada aluno.
RF03: O sistema deve identificar alunos em situação de Recuperação.
RF04: O sistema deve identificar o "Top Student".
RF05: O sistema deve gerar um relatório final em formato ".txt".

Requisitos Não-Funcionais:
RNF01: O sistema deve ser desenvolvido em Python utilizando listas e tuplas.
RNF02: O código deve ser modularizado, dividido entre os arquivos: "main.py" e "processamento.py".
RNF03: O sistema deve possuir tratamento de erros básico.

Regras de Negócio:
RN01: Um aluno é considerado em "Recuperação" se a sua média final for menor que 7.0.
RN02: A estrutura de entrada deve seguir o padrão: "Lista de Tuplas [("Nome", [notas])]".

---

Mapa de Empatia:

O que pensam e sentem?
Sentem insegurança com dados errados e frustração com o tempo gasto em tarefas manuais. Desejam uma visão funcional e rápida do cenário.

O que escutam?
Reclamações sobre a dificuldade de tomar decisões pedagógicas sem dados rápidos.

O que veem?
Listas de notas vazias, incompletas ou corrompidas, chegando de maneiras diferentes.

O que falam e fazem?
Gastam muito tempo processando notas aluno por aluno manualmente e cometem erros nesse retrabalho.

Dores: Atrasos, retrabalho, risco de falhas e falta de padronização nas informações.
Ganhos: Automação na identificação de alunos em recuperação/destaque e código modular fácil de dar manutenção.
