from google.adk.tools.tool_context import ToolContext

from .session_manager import (
    load_session,
    update_session,
    save_user_session,
    get_user_session
)


def get_current_session_id(tool_context: ToolContext) -> str:
    """Get the current ADK session ID."""
    return tool_context._invocation_context.session.id


def save_trip_information(
    key: str,
    value: str,
    tool_context: ToolContext
) -> dict:
    """Save travel information to the current user's session."""

    session_id = get_current_session_id(tool_context)

    updated_data = update_session(
        session_id=session_id,
        key=key,
        value=value
    )

    return {
        "success": True,
        "message": f"{key} saved successfully.",
        "session_id": session_id,
        "session": updated_data
    }


def load_trip_information(
    tool_context: ToolContext
) -> dict:
    """Load travel information from the current session."""

    session_id = get_current_session_id(tool_context)

    data = load_session(session_id)

    return {
        "success": True,
        "session_id": session_id,
        "session": data
    }


def register_user(
    user_id: str,
    tool_context: ToolContext
) -> dict:
    """Connect a user ID to the current ADK session."""

    session_id = get_current_session_id(tool_context)

    save_user_session(
        user_id=user_id,
        session_id=session_id
    )

    return {
        "success": True,
        "message": "User session registered successfully.",
        "user_id": user_id,
        "session_id": session_id
    }


def restore_user_session(user_id: str) -> dict:
    """Find and load a user's previous travel session."""

    session_id = get_user_session(user_id)

    if not session_id:
        return {
            "success": False,
            "message": "No previous session found.",
            "session": {}
        }

    data = load_session(session_id)

    return {
        "success": True,
        "message": "Previous session restored successfully.",
        "user_id": user_id,
        "session_id": session_id,
        "session": data
    }
