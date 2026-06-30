from database.connection import get_connection


def save_message(role: str, message: str):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO conversations (role, message)
        VALUES (%s, %s)
        """,
        (role, message),
    )

    conn.commit()

    cursor.close()
    conn.close()


def get_all_messages():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT role, message
        FROM conversations
        ORDER BY id;
        """
    )

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows


def clear_conversations():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM conversations;
        """
    )

    conn.commit()

    cursor.close()
    conn.close()