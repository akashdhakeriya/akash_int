from transformers import pipeline

class AkashAI:
    def __init__(self):
        self.chatbot = pipeline(
            "text-generation",
            model="Qwen/Qwen2.5-0.5B-Instruct"
        )

    def ask(self, question):
        prompt = (
            "You are Akash AI, a helpful AI assistant. "
            "Answer the user clearly and accurately.\n\n"
            f"User: {question}\n"
            "Akash AI:"
        )

        response = self.chatbot(
            prompt,
            max_new_tokens=150
        )

        return response[0]["generated_text"]
