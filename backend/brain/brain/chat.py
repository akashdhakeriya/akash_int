from model import AkashAI

ai = AkashAI()

print("Akash AI is ready!")

while True:
    question = input("You: ")

    if question.lower() == "exit":
        print("Akash AI: Goodbye!")
        break

    answer = ai.ask(question)

    print("\nAkash AI:", answer)
    print()
