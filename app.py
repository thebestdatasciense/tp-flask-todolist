from flask import Flask, render_template, request, redirect, url_for , flash

app = Flask(__name__)

tasks = [
    {"id": 1, "title": "Acheter du pain", "done": False},
    {"id": 2, "title": "Réviser Flask", "done": True},
]

_next_id = max(task["id"] for task in tasks) + 1 if tasks else 1

def get_next_id():
    global _next_id
    nid = _next_id
    _next_id += 1
    return nid

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title", "").strip()
    if not title:
        return redirect(url_for("index"))
    priority = request.form.get("priority", "normale")
    new_task = {"id": get_next_id(), "title": title, "done": False, "priority": priority}
    tasks.append(new_task)
    return redirect(url_for("index"))


@app.route("/done/<int:task_id>")
def done(task_id):
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            break
    return redirect(url_for("index"))

@app.route("/delete/<int:task_id>", methods=["POST"])
def delete(task_id):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return redirect(url_for("index"))

@app.route("/edit/<int:task_id>", methods=["GET", "POST"])
def edit(task_id):
    task = tasks[task_id]

    if request.method == "POST":
        # Mise à jour de la tâche
        task["title"] = request.form.get("title")
        task["priority"] = request.form.get("priority")

        flash("Tâche mise à jour avec succès !")
        return redirect(url_for("home"))

    # Affichage du formulaire d’édition
    return render_template("edit.html", task=task, task_id=task_id)


if __name__ == "__main__":
    app.run(debug=True)
