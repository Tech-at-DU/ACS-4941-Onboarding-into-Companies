"""A small to-do API.

Run with: flask --app app run
"""

from flask import Flask, jsonify, request

import dates


def create_app():
    app = Flask(__name__)
    app.config["TODOS"] = {}
    app.config["NEXT_ID"] = 1

    def serialize(todo):
        return {**todo, "created_at": todo["created_at"].isoformat()}

    def find(todo_id):
        return app.config["TODOS"].get(todo_id)

    @app.get("/todos")
    def list_todos():
        todos = list(app.config["TODOS"].values())

        done = request.args.get("done")
        if done is not None:
            want_done = done.lower() == "true"
            todos = [t for t in todos if t["done"] == want_done]

        created_after = request.args.get("created_after")
        if created_after:
            cutoff = dates.parse_date(created_after)
            todos = [t for t in todos if t["created_at"] > cutoff]

        return jsonify([serialize(t) for t in todos])

    @app.post("/todos")
    def create_todo():
        data = request.get_json(silent=True) or {}
        title = (data.get("title") or "").strip()
        if not title:
            return jsonify({"error": "title is required"}), 400

        todo_id = app.config["NEXT_ID"]
        app.config["NEXT_ID"] += 1
        todo = {"id": todo_id, "title": title, "done": False, "created_at": dates.today()}
        app.config["TODOS"][todo_id] = todo
        return jsonify(serialize(todo)), 201

    @app.get("/todos/<int:todo_id>")
    def get_todo(todo_id):
        todo = find(todo_id)
        if todo is None:
            return jsonify({"error": "not found"}), 404
        return jsonify(serialize(todo))

    @app.patch("/todos/<int:todo_id>")
    def update_todo(todo_id):
        todo = find(todo_id)
        if todo is None:
            return jsonify({"error": "not found"}), 404

        data = request.get_json(silent=True) or {}
        if "title" in data:
            title = (data["title"] or "").strip()
            if not title:
                return jsonify({"error": "title cannot be empty"}), 400
            todo["title"] = title
        if "done" in data:
            if not isinstance(data["done"], bool):
                return jsonify({"error": "done must be true or false"}), 400
            todo["done"] = data["done"]
        return jsonify(serialize(todo))

    @app.delete("/todos/<int:todo_id>")
    def delete_todo(todo_id):
        if app.config["TODOS"].pop(todo_id, None) is None:
            return jsonify({"error": "not found"}), 404
        return "", 204

    return app


app = create_app()
