conversation_history = []


def add_user_message(message):
    conversation_history.append(
        {
            "role": "user",
            "content": message
        }
    )


def add_assistant_message(message):
    conversation_history.append(
        {
            "role": "assistant",
            "content": message
        }
    )


def get_history():

    history = ""

    for msg in conversation_history:

        history += f"{msg['role'].capitalize()}: {msg['content']}\n"

    return history