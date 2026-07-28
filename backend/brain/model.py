from transformers import pipeline


class AkashAI:
    def __init__(self):
        self.chatbot = pipeline(
            "text-generation",
            model="Qwen/Qwen2.5-0.5B-Instruct",
            return_full_text=False
        )

        # Model ki default generation settings ko clean karo
        self.chatbot.model.generation_config.max_length = None
        self.chatbot.model.generation_config.max_new_tokens = 150
        self.chatbot.model.generation_config.do_sample = False
        self.chatbot.model.generation_config.temperature = None
        self.chatbot.model.generation_config.top_p = None
        self.chatbot.model.generation_config.top_k = None

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

        response = self.chatbot(prompt)

        return response[0]["generated_text"].strip()
