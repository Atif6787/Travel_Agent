import json
from pathlib import Path


SESSION_DIR = Path("sessions")
SESSION_DIR.mkdir(exist_ok=True)

USER_MAP_FILE = SESSION_DIR / "user_sessions.json"


def get_session_file(session_id: str) -> Path:
    return SESSION_DIR / f"{session_id}.json"


def save_session(session_id: str, data: dict):
    file_path = get_session_file(session_id)

    with open(file_path, "w", encoding="utf-8-sig") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


def load_session(session_id: str) -> dict:
    file_path = get_session_file(session_id)

    if not file_path.exists():
        return {}

    with open(file_path, "r", encoding="utf-8-sig") as file:
        return json.load(file)


def session_exists(session_id: str) -> bool:
    return get_session_file(session_id).exists()


def update_session(session_id: str, key: str, value: str):
    data = load_session(session_id)

    data[key] = value

    save_session(session_id, data)

    return data


def save_user_session(user_id: str, session_id: str):
    """Connect a user to their session ID."""

    if USER_MAP_FILE.exists():
        with open(USER_MAP_FILE, "r", encoding="utf-8-sig") as file:
            users = json.load(file)
    else:
        users = {}

    users[user_id] = session_id

    with open(USER_MAP_FILE, "w", encoding="utf-8-sig") as file:
        json.dump(users, file, indent=4)


def get_user_session(user_id: str):
    """Get the previous session ID for a user."""

    if not USER_MAP_FILE.exists():
        return None

    with open(USER_MAP_FILE, "r", encoding="utf-8-sig") as file:
        users = json.load(file)

    return users.get(user_id)
