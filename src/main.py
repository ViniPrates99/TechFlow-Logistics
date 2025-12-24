from src.task_manager import TaskManager

print("="*30)
print(" SISTEMA LOGÍSTICO TECHFLOW ")
print("="*30)

def main():
    manager = TaskManager()
    print("--- TechFlow Logistics System ---")
    
    # Simulando uso do sistema para o vídeo
    manager.create_task("Entrega Rota Sul", "Média")
    manager.create_task("Medicamentos Urgentes", "Alta") # Mudança de escopo
    
    print("\nLista de Tarefas:")
    for t in manager.get_all_tasks():
        urgente = "[URGENTE]" if t["urgent"] else ""
        print(f"{t['id']}. {t['title']} - {t['status']} {urgente}")

if __name__ == "__main__":
    main()