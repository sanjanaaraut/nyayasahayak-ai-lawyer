# llm_helper.py — Swappable AI Model Wrapper
from google import genai
from google.genai import types


def ask_ai(
    user_prompt: str,
    system_prompt: str,
    api_key: str,
    model_name: str = "gemini-3.8-flash",
) -> str:
    """
    Single-turn AI call for case analysis and drafting.
    Swap 'model_name' or replace the client here to use any other model/API.
    """
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=model_name,
        contents=user_prompt,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.2,
        ),
    )
    return response.text


def roleplay_ai(
    chat_history: list,
    system_prompt: str,
    api_key: str,
    model_name: str = "gemini-3.8-flash",
) -> str:
    """
    Multi-turn AI call for the 'Practice Arguing' mode.
    chat_history format: [{"role": "user" | "assistant", "content": "..."}]
    """
    client = genai.Client(api_key=api_key)
    formatted_contents = []
    for msg in chat_history:
        role = "model" if msg["role"] == "assistant" else "user"
        formatted_contents.append(
            types.Content(
                role=role,
                parts=[types.Part.from_text(text=msg["content"])],
            )
        )

    response = client.models.generate_content(
        model=model_name,
        contents=formatted_contents,
        config=types.GenerateContentConfig(
            system_instruction=system_prompt,
            temperature=0.4,
        ),
    )
    return response.text