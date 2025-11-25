# === modules/withdraw.py ===

import requests
from config import BINANCE_API_KEY, BINANCE_SECRET, PAYEER_API_KEY, PAYEER_ACCOUNT
from database import users

def request_withdraw(user_id, amount, method, address):
    if method == "payeer":
        return withdraw_payeer(user_id, amount, address)
    elif method == "binance":
        return withdraw_binance(user_id, amount, address)

def withdraw_payeer(user_id, amount, address):
    users.update_one({"user_id": user_id}, {"$inc": {"balance": -amount}})
    return True

def withdraw_binance(user_id, amount, address):
    users.update_one({"user_id": user_id}, {"$inc": {"balance": -amount}})
    return True
