from google import genai

from config.settings import GEMINI_API_KEY
from prompts.system_prompt import SYSTEM_PROMPT
from memory.conversation import get_history

client = genai.Client(api_key=GEMINI_API_KEY)


def ask_gemini(prompt: str) -> str:

    history = get_history()

    full_prompt = f"""
{SYSTEM_PROMPT}

Conversation History:
{history}

User:
{prompt}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=full_prompt,
    )

    return response.text