# To-Do API (AI-1 starter)

A small to-do API written in Python with Flask. Data is kept in memory, so it resets when the server restarts.

## Setup

macOS / Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest                      # run the tests
flask --app app run         # start the server at http://127.0.0.1:5000
```

Windows (PowerShell): use `python -m venv .venv` and `.venv\Scripts\Activate.ps1`, then the same commands.

## Endpoints

| Method | Path | Body / query | Notes |
| --- | --- | --- | --- |
| `GET` | `/todos` | `?done=true\|false`, `?created_after=YYYY-MM-DD` | List todos, optionally filtered |
| `POST` | `/todos` | `{"title": "..."}` | Create a todo |
| `GET` | `/todos/<id>` | | Get one todo |
| `PATCH` | `/todos/<id>` | `{"title": "...", "done": true}` | Update title and/or done |
| `DELETE` | `/todos/<id>` | | Delete a todo |

Try it with curl:

```bash
curl -X POST localhost:5000/todos -H "Content-Type: application/json" -d '{"title": "Buy milk"}'
curl localhost:5000/todos
```

## Your task

1. Add an optional **due date** to todos. It can be set when a todo is created and changed with `PATCH`.
1. Add an endpoint that returns **overdue** todos.
1. Write tests for what you add.

Use your AI tool, and narrate as you work. Ask the interviewer any clarifying questions before you start prompting.
