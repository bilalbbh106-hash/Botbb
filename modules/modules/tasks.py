# === modules/tasks.py ===

from database import tasks_db, users

def create_task(task_type, reward, data):
    tasks_db.insert_one({
        "type": task_type,
        "reward": reward,
        "data": data,
        "active": True
    })

def complete_task(user_id, task_id):
    users.update_one(
        {"user_id": user_id},
        {"$inc": {"balance": 0.02}}
    )
