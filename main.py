# Hugging Face ke InferenceClient ko import kar rahe hain
# Iska use Hugging Face model ko API ke through call karne ke liye hoga
from huggingface_hub import InferenceClient

# .env file se secret/API key load karne ke liye
from dotenv import load_dotenv

# Environment variables access karne ke liye
import os


# .env file ke variables ko load karta hai
load_dotenv()


# .env file se HF_TOKEN naam ki value read kar rahe hain
HF_TOKEN = os.getenv("HF_TOKEN")


# Hugging Face ka client create kar rahe hain
# token = hamara Hugging Face API token
# provider = jis inference provider ke through model run hoga
client = InferenceClient(
    token=HF_TOKEN,
    provider="featherless-ai"
)


# User se flashcards ka topic pooch rahe hain
# Example: Python, Data Structures, DBMS
topic = input("Enter topic: ")


# User se pooch rahe hain ki kitne flashcards chahiye
# int() input ko number/integer me convert karta hai
count = int(input("How many flashcards: "))


# Hugging Face model ko request bhej rahe hain
response = client.chat.completions.create(

    # Ye batata hai ki kaunsa Hugging Face model use karna hai
    model="google/gemma-2-2b-it",

    # Model ko instruction/prompt bhej rahe hain
    messages=[
        {
            # User ka message hai
            "role": "user",

            # f-string ki help se topic aur count ko prompt me insert kar rahe hain
            "content": f"""
Create {count} flashcards about {topic}.

Format:
Q: question
A: answer

Keep the answers short and easy to understand.
"""
        }
    ],

    # Model maximum kitne tokens generate kar sakta hai
    max_tokens=500
)


# Model ke response me se actual generated text print kar rahe hain
print(response.choices[0].message.content)