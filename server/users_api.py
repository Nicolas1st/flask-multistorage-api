from flask import Blueprint, redirect, render_template, request

def new_users_api(path_to_register_api_on: str, template_folder_path: str, storage) -> Blueprint:
    # the handlers are defined inside to make the storage variable available to them
    # without making it global
    def add_user():
        if request.method == "GET":
            return render_template("create.html")
        else:
            name = request.form["name"]
            surname = request.form["surname"]
            age = int(request.form["age"])
            storage.add_user(name, surname, age)
            return redirect("/", 302)

    def remove_user(id):
        storage.remove_user(id)
        return redirect("/", 302)

    def update_user(id):
        if request.method == "GET":
            return render_template("update.html")
        else:
            name = request.form["name"]
            surname = request.form["surname"]
            age = int(request.form["age"])
            storage.update_user(id, name, surname, age)
            return redirect("/", 302)

    def get_user_by_id(id):
        return storage.get_user_by_id(id)

    def get_all_users():
        return render_template("users.html", users=storage.get_all_users().items())

    users_api = Blueprint('users_api', __name__, template_folder='templates_folder_path')

    if path_to_register_api_on.endswith("/"):
        path_to_register_api_on = path_to_register_api_on[:-1]

    # registering handlers
    users_api.add_url_rule(
        f"{path_to_register_api_on}/create/",
        view_func=add_user,
        methods=["POST", "GET"],
    )

    users_api.add_url_rule(
        f"{path_to_register_api_on}/<int:id>/remove/",
        view_func=remove_user,
        methods=["GET"],
    )

    users_api.add_url_rule(
        f"{path_to_register_api_on}/<int:id>/update/",
        view_func=update_user,
        methods=["POST", "GET"],
    )

    users_api.add_url_rule(
        f"{path_to_register_api_on}/<int:id>/",
        view_func=get_user_by_id,
        methods=["GET"],
    )

    users_api.add_url_rule(
        "/",
        view_func=get_all_users,
        methods=["GET"],
    )

    return users_api