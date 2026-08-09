import random 
from datetime import datetime
BOT_NAME = "NeoChat"

BOT_NAME = "NeoChat"
def get_greeting_response():
    greetings = [
        f"Hello, I'm {BOT_NAME}! How can I assist you today?",
        f"Hi there! I'm {BOT_NAME}, your friendly chatbot. What can I do for you?"
    ]
    return random.choice(greetings)
def get_time_response():
    current_time = datetime.now().strftime("%H:%M:%S")
    return f"The current time is {current_time}."

def get_bot_response(user_input):
    user_input = user_input.lower().strip()
    if "hello" in user_input or "hi" in user_input:
        return get_greeting_response()
    elif "time" in user_input:
        return get_time_response()
    elif"good morning" in user_input or "good afternoon" in user_input or "good evening" in user_input:
        return f"Good day! How can I help you?"
    elif"name" in user_input:
        return f"My name is {BOT_NAME}. I'm here to assist you with any questions you may have."
    elif"date" in user_input:
        current_date = datetime.now().strftime("%Y-%m-%d")
        return f"Today's date is {current_date}."
    #-------------AI/ML/DL TOPICS QUESTIONS----------------
    elif "ai" in user_input or "artificial intelligence" in user_input:
        return "Artificial Intelligence (AI) is the simulation of human intelligence in machines that are programmed to think and learn like humans."
    elif "ml" in user_input or "machine learning" in user_input:
        return "Machine Learning (ML) is a subset of AI that focuses on the development of algorithms that allow computers to learn from and make predictions or decisions based on data."
    elif "dl" in user_input or "deep learning" in user_input:
        return "Deep Learning (DL) is a subset of ML that uses neural networks with many layers (deep neural networks) to model complex patterns in data."
    elif "neural network" in user_input:
        return "A Neural Network is a series of algorithms that attempt to recognize underlying relationships in a set of data through a process that mimics the way the human brain operates."
    elif "natural language processing" in user_input or "nlp" in user_input:
        return "Natural Language Processing (NLP) is a field of AI that focuses on the interaction between computers and humans through natural language, enabling machines to understand, interpret, and respond to human language."
    elif "computer vision" in user_input:
        return "Computer Vision is a field of AI that enables computers to interpret and make decisions based on visual data from the world, such as images and videos."
    elif "reinforcement learning" in user_input:
        return "Reinforcement Learning (RL) is a type of machine learning where an agent learns to make decisions by taking actions in an environment to maximize cumulative reward."
    elif "supervised learning" in user_input:
        return "Supervised Learning is a type of machine learning where the model is trained on labeled data, meaning that each training example is paired with an output label."
    elif "unsupervised learning" in user_input:
        return "Unsupervised Learning is a type of machine learning where the model is trained on unlabeled data, meaning that the algorithm tries to find hidden patterns or intrinsic structures in the input data."
    elif"types opf supervised learning" in user_input:
        return "There are two main types of supervised learning: classification and regression. Classification is used when the output variable is a category, while regression is used when the output variable is a continuous value."
    #-------------DECODE LEARNING TOPICS QUESTIONS----------------
    elif "decode lab" in user_input:
        return "Decode Lab is a research initiative focused on advancing the field of deep learning and its applications."
    elif"what is internship" in user_input:
        return "An internship is a temporary position offered by an organization to provide practical experience in a particular field, often for students or recent graduates."


    elif"thank you" in user_input or "thanks" in user_input:
        return "You're welcome! If you have any more questions, feel free to ask."
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!" 
    elif"help" in user_input:
        return "Sure! I'm here to help. You can ask me about AI, ML, DL, or any other topic you're interested in."
    else:
        return "I'm sorry, I didn't understand that. Can you please try asking about AI, ML, DL, or any other topic you're interested in?"


def run_chatbot():
        print("=" * 55)
        print(f"Welcome to {BOT_NAME}! Type 'exit' to end the chat.")
        print("=" * 55)
        while True:
            user_input = input("You: ")
            if user_input.lower() == "exit":
                print("Exiting the chat. Goodbye!")
                break
            response = get_bot_response(user_input)
            print(f"{BOT_NAME}: {response}")
if __name__ == "__main__":
        run_chatbot()