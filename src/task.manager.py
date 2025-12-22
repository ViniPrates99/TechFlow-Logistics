# Gerenciador de Tarefas para a TechFlow Solutions
class TaskManager:
    def __init__(self):
        # Lista que simula o banco de dados de entregas
        self.tasks = []

    def create_task(self, title, priority="Média"):
        """Adiciona uma nova tarefa de logística ao sistema"""
        if not title:
            return "Erro: O título da tarefa é obrigatório."
        
        task = {
            "id": len(self.tasks) + 1,
            "title": title,
            "priority": priority,
            "status": "A Fazer"
        }
        self.tasks.append(task)
        return task

    def get_all_tasks(self):
        """Retorna todas as tarefas cadastradas"""
        return self.tasks