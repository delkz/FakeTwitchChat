import openai

class ChatSimulation:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_response(self, text, sentiment):
        prompt = f"A live chat participant just said: '{text}'. The sentiment score is {sentiment}. Respond like a viewer in a fun, engaging way."
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",  # ou "gpt-4" se você tiver acesso
            messages=[
                {"role": "system", "content": "You are a friendly twitch chat viewer."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=50,
            temperature=0.7
        )
        return response.choices[0].message['content'].strip()
