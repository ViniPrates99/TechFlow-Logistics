from src.task_manager import TaskManager

def test_criacao_tarefa_sucesso():
    manager = TaskManager()
    tarefa = manager.create_task("Entrega Urgente - Rota 01")
    assert tarefa["title"] == "Entrega Urgente - Rota 01"
    assert tarefa["status"] == "A Fazer"

def test_erro_tarefa_sem_titulo():
    manager = TaskManager()
    erro = manager.create_task("")
    assert erro == "Erro: O título da tarefa é obrigatório."