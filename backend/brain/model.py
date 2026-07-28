def ask(self, question):
    prompt = (
        "You are Akash AI, a helpful AI assistant.\n"
        "Rules:\n"
        "1. Answer clearly and accurately.\n"
        "2. If the user writes in Hinglish, answer in natural simple Hinglish.\n"
        "3. If the user writes in English, answer in English.\n"
        "4. Do not invent facts.\n"
        "5. Keep the answer concise and directly answer the question.\n"
        "6. Do not add unnecessary emojis or repeated closing messages.\n\n"
        f"User: {question}\n"
        "Akash AI:"
    )

    response = self.chatbot(
        prompt,
        max_new_tokens=150
    )

    return response[0]["generated_text"]
