# === modules/referrals.py ===

from database import users, referrals_db

def register_referral(user_id, referrer_id):
    if user_id == referrer_id:
        return False
    if referrals_db.find_one({"user": user_id}):
        return False

    referrals_db.insert_one({"user": user_id, "referrer": referrer_id})
    users.update_one(
        {"user_id": int(referrer_id)},
        {"$inc": {"balance": 0.05}},  # مكافأة الإحالة
        upsert=True
    )
    return True
