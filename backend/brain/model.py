from transformers import pipeline, GenerationConfig


class AkashAI:
    def __init__(self):
        self.chatbot = pipeline(
            "text-generation",
            model="Qwen/Qwen2.5-0.5B-Instruct",
            return_full_text=False
        )

        self.generation_config = GenerationConfig(
            max_new_tokens=150,
            do_sample=False
        )

    def ask(self, question):
        prompt = (
            "You are Akash AI.\n"
            "Answer the user's question clearly and accurately.\n"
            "If the user asks in Hinglish, answer in natural simple Hinglish.\n"
            "Do not invent facts.\n"
            "Do not repeat the question.\n"
            "Do not add greetings or closing messages.\n\n"
            f"User: {question}\n"
            "Answer:"
        )

        response = self.chatbot(
            prompt,
            generation_config=self.generation_config
        )

        return response[0]["generated_text"].strip()
