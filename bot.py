import json
import difflib

def load_faqs():
    with open("faqs.json", "r") as f:
        return json.load(f)

def get_best_match(user_question, questions):
    matches = difflib.get_close_matches(user_question, questions, n=1, cutoff=0.5)
    return matches[0] if matches else None

def chatbot():
    faqs = load_faqs()
    questions = [faq["question"] for faq in faqs]

    print("🤖 FAQ Chatbot (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "exit":
            print("Bot: Goodbye!")
            break

        match = get_best_match(user_input, questions)

        if match:
            for faq in faqs:
                if faq["question"] == match:
                    print("Bot:", faq["answer"])
        else:
            print("Bot: Sorry, I don't understand that question.")

if __name__ == "__main__":
    chatbot()
