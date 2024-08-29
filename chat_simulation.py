from transformers import GPT2LMHeadModel, GPT2Tokenizer

class ChatSimulation:
    def __init__(self,api_key):
        self.tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
        self.model = GPT2LMHeadModel.from_pretrained('gpt2')

    def generate_response(self, text, sentiment):
        prompt = f"A live chat participant just said: '{text}'. Respond like a friendly and engaging viewer, considering the sentiment is {sentiment}. the language is portuguese"
        inputs = self.tokenizer(prompt, return_tensors='pt')
        outputs = self.model.generate(
            inputs['input_ids'],
            max_length=100,  # Aumentar o comprimento máximo se necessário
            num_return_sequences=1,
            temperature=0.5,  # Ajustar a temperatura para controlar a criatividade
            pad_token_id=self.tokenizer.eos_token_id
        )
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response

# Exemplo de uso
if __name__ == "__main__":
    chat_simulation = ChatSimulation()
    text = "Como você está?"
    sentiment = "happy"
    response = chat_simulation.generate_response(text, sentiment)
    print(f"Resposta Simulada: {response}")
