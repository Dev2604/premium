from pymongo import MongoClient
from config import MONGO

appdb = MongoClient(MONGO)
db = appdb.main
users = db.users

def already_db(user_id):
        user = users.find_one({"user_id" : str(user_id)})
        if not user:
            return False
        return True

def add_user(user_id):
    in_db = already_db(user_id)
    if in_db:
        return
    return users.insert_one({"user_id": str(user_id)})
  
def all_users():
    user = users.find({})
    usrs = len(list(user))
    return usrs
