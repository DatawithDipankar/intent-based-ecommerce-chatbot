from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def talk(query):
    completion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a casual conversational assistant. "
                    "Keep responses short (1-2 sentences). "
                    "Do not explain that you are a language model. "
                    "Keep tone natural and friendly."
                )
            },
            {"role": "user", "content": query}
        ],
        model=os.environ['GROQ_MODEL'],
        temperature=0.7,
        max_tokens=300
    )

    return completion.choices[0].message.content.strip()
