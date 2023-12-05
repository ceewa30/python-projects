import openai 

class Chatbot:
    def __init__(self):
        openai.api_key = "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"

    def get_response(self, user_input):
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_input,
            max_tokens=4000,
            temperature=0.5
        ).choices[0].text
        return response
    

if __name__ == "__main__":
    chatbot = Chatbot()
    response = chatbot.get_response("Write a joke about birds.")
    print(response)