class TaskManager:
    def __init__(self):
        self.tasks = []
#função para criar uma tarefa
    def create_task(self, title, priority="Média"):
        """Cria uma nova tarefa (Create) """
        if not title:
            return "Erro: O título é obrigatório."
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "priority": priority,
            "urgent": True if priority == "Alta" else False,
            "status": "A Fazer"
        }
        self.tasks.append(task)
        return task
#função para listar as tarefas
    def get_all_tasks(self):
        """Lista todas as tarefas (Read) """
        return self.tasks
#funcao para completar o status da tarefa
    def complete_task(self, task_id):
        """Atualiza o status para Concluído (Update) """
        for task in self.tasks:
            if task["id"] == task_id:
                task["status"] = "Concluído"
                return True
        return False
#cria a função de remover a tarefa
    def delete_task(self, task_id):
        """Remove uma tarefa (Delete) """
        original_count = len(self.tasks)
        self.tasks = [t for t in self.tasks if t["id"] != task_id]
        return len(self.tasks) < original_count