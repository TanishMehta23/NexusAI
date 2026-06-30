from database.conversations import (
    save_message,
    get_all_messages,
)


def add_user_message(message: str):
    save_message("user", message)


def add_assistant_message(message: str):
    save_message("assistant", message)


def get_history():

    messages = get_all_messages()

    history = ""

    for role, message in messages:
        history += f"{role.capitalize()}: {message}\n"

    return history