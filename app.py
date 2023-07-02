from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import streamlit as st

# Create a ChatBot instance
chatbot = ChatBot('MyChatBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the English corpus
trainer.train('chatterbot.corpus.english')

def get_response(user_input):
    # Get a response from the chatbot based on user input
    response = chatbot.get_response(user_input)
    return str(response)

def main():
    st.title("ChatterBot")
    st.write("Welcome! Start chatting with the chatbot.")

    user_input = st.text_input("User Input:")
    submit_button = st.button("Submit")

    if submit_button:
        bot_response = get_response(user_input)
        st.write("Bot Response:", bot_response)

if __name__ == "__main__":
    main()
