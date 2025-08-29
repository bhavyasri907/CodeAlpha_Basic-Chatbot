def get_chatbot_response(user_input):
    user_input=user_input.lower()
    if user_input=="hello":
        return "Hi👋"
    elif user_input == "how are you":
        return "I'm fine, Thanks!😊"
    elif user_input == "bye":
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."
def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input=input("You: ")
        response=get_chatbot_response(user_input)
        print("Chatbot:",response)
        if user_input.lower()=="bye":
            break
chatbot()