class SimpleChatApp:
    def __init__(self):
        self.messages = []

    def send_message(self, user, message):
        self.messages.append(f"{user}: {message}")

    def display_messages(self):
        for message in self.messages:
            print(message)

# Example usage:
if __name__ == "__main__":
    chat_app = SimpleChatApp()

    while True:
        user_input = input("Type your message (or 'exit' to quit): ")

        if user_input.lower() == 'exit':
            break

        chat_app.send_message("You", user_input)
        chat_app.display_messages()
