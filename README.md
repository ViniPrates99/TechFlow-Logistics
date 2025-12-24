# TechFlow Solutions - Gerenciamento de Logística Ágil

## Como Executar
1. Clone o repositório.
2. Instale as dependências: `pip install pytest`.
3. Execute o sistema: `python main.py`.
4. Execute os testes: `pytest`.

## 1. Objetivo do Projeto
Este sistema foi desenvolvido para uma startup de logística com o intuito de acompanhar o fluxo de trabalho em tempo real, priorizar tarefas críticas e monitorar o desempenho da equipe[cite: 7].

## 2. Escopo do Software
O sistema permite o gerenciamento de tarefas (CRUD), onde gestores e motoristas podem organizar as demandas de entrega[cite: 6, 48].

## 3. Metodologia Adotada
Utilizamos a metodologia ágil **Kanban**, focando no fluxo contínuo e na visualização clara do status de cada tarefa através das colunas: A Fazer, Em Progresso e Concluído[cite: 13, 42].

## HISTÓRICO DE MUDANÇAS
DATA: 23/12/2025

**SOLICITAÇÃO:** Adição de nível de prioridade para entregas urgentes.
**JUSTIFICATIVA:** Após feedback da startup de logística, identificou-se a necessidade de destacar entregas de alta prioridade (como medicamentos ou itens perecíveis) para otimizar a triagem no armazém
**Impacto:** Alteração na classe `TaskManager` e criação de novo card no Kanban