from app import app
from app import controller
from flask import request, render_template

i = 0
add_task = 0
del_task = 0

@app.route ('/', methods=['GET'])
def route_index():
    return render_template("home.html",
                           title="EPyTodo")

@app.route ('/register', methods=['POST'])
def route_register():
    global i
    i = 1
    return render_template("register.html",
                            title="EPyTodo")

@app.route ('/login', methods=['POST'])
def route_login():
    global i
    i = 2
    return render_template("connect.html",
                           title="EPyTodo")

@app.route('/user', methods=['GET'])
def route_user():
    access = 0
    result = request.args
    if i == 1:
        access = controller.register_action(result)
    elif i == 2:
        access = controller.login_action(result)
    if access == 1:
        return render_template("main_page.html",
                            title="EPyTodo")
    else:
        return render_template("home.html",
                                title="EPyTodo")


@app.route('/task', methods=['GET'])
def route_task():
    global add_task
    global del_task
    all_task = None
    if add_task == 1:
        result = request.args
        controller.add_task(result)
        add_task = 0
    if del_task == 1:
        result = request.args
        controller.del_task(result)
        del_task = 0
    all_task = controller.get_all_task()
    return render_template("all_task.html",
                            title="EPyTodo",
                            task=all_task)

@app.route('/add', methods=['POST'])
def route_taskadd():
    global add_task
    add_task = 1
    return render_template("add_task.html",
                            title="EPyTodo")

@app.route('/id', methods=['GET'])
def route_id():
    return render_template("update_task.html",
                            title="EPyTodo")

@app.route('/del', methods=['POST'])
def route_del():
    global del_task
    del_task = 1
    all_task = controller.get_all_task()
    return render_template("del_task.html",
                            title="EPyTodo",
                            task=all_task)

@app.route('/signout', methods=['POST'])
def route_signout():
    return render_template("signout.html",
                           title="EPyTodo")