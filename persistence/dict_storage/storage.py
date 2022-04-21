from ..model.user import new_user

def new_storage() -> dict:
    return {}

class DictUserStorage:

    def __init__(self):
        self.storage = {}
        self.last_used_id = 0
    
    def add_user(self, name: str, surname: str, age: int):
        user = new_user(self.last_used_id, name, surname, age)
        self.storage[self.last_used_id] = user
        self.last_used_id += 1

        return user
    
    def remove_user(self, id):
        try:
            del self.storage[id]
            return "sucess"
        except KeyError:
            return "failure"
    
    def update_user(self, id, name, surname, age):
        if id not in self.storage:
            return "failure"
        else:
            user = new_user(id, name, surname, age)
            self.storage[id] = user
            return "success"
    
    def get_user_by_id(self, id):
        return self.storage.get(id, None)
    
    def get_all_users(self):
        return self.storage
