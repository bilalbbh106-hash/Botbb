# === modules/antifraud.py ===

from database import users

def check_user_legit(user_id):
    user = users.find_one({"user_id": user_id})

    if not user:
        return False

    if user.get("fake", False):
        return False

    return True
