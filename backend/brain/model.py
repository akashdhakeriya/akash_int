from transformers import pipeline


class AkashAI:
    def __init__(self):
        self.chatbot = pipeline(
            "text-generation",
            model="Qwen/Qwen2.5-0.5B-Instruct",
            return_full_text=False
        )

    def ask(self, question, knowledge=None):

        if knowledge:
            prompt = f"""
You are Akash AI.

Use ONLY the information provided in the Knowledge section.

Rules:
- Answer in simple natural Hinglish.
- Do not add facts that are not present in Knowledge.
- Do not change numbers or technical facts from Knowledge.
- Do not invent information.
- If the answer is not present in Knowledge, say:
"Mujhe is question ka answer meri current knowledge base mein nahi mila."
- Keep the answer concise.
- Do not repeat the question.
- Do not add a closing message.

Knowledge:
{knowledge}

User Question:
{question}

Answer:
"""
        else:
            prompt = f"""
You are Akash AI.

Answer the user clearly and accurately.
If the user writes in Hinglish, answer in simple natural Hinglish.
Do not invent facts.
Do not repeat the question.
Do not add a closing message.

User:
{question}

Answer:
"""

        response = self.chatbot(
            prompt,
            max_new_tokens=80,
            do_sample=False,
            return_full_text=False
        )

        return response[0]["generated_text"].strip()
