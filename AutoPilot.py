import nltk
from nltk.chat.util import Chat, reflections

class CanadaChat(Chat):
    def __init__(self):
        # Define a list of patterns and responses for the AI to match and respond to
        patterns = [
            (r'hi|hello', ['Hi there!', 'Hello!', 'Hi!']),
            (r'what is the capital of canada\?', ['The capital of Canada is Ottawa.']),
            (r'what are the provinces of canada\?', ['The provinces of Canada are Alberta, British Columbia, Manitoba, New Brunswick, Newfoundland and Labrador, Nova Scotia, Ontario, Prince Edward Island, Quebec, and Saskatchewan.']),
            (r'what is the population of canada\?', ['The population of Canada is approximately 38 million people.']),
            (r'what is the national animal of canada\?', ['The national animal of Canada is the beaver.']),
            (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Bye!'])
        ]
        # Initialize the Chat superclass with the patterns and a reflection dictionary
        super().__init__(patterns, reflections)
        self.name = '0AutoPilot0'
        
    def greet(self):
        print("Hello, my name is " + self.name + " and I'm here to answer your questions about Canada.")
        
# Create an instance of the CanadaChat class and start the conversation
autopilot = CanadaChat()
autopilot.greet()
autopilot.converse()
