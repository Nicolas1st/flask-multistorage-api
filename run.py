from flask import Flask
from persistence.dict_storage.storage import DictUserStorage
from server.users_api import new_users_api

if __name__ == "__main__":
    storage = DictUserStorage()
    users_api = new_users_api("/users", "templates", storage)

    app = Flask(__name__)
    app.register_blueprint(users_api)

    app.run()