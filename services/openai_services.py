# from openai import OpenAI
from groq import Groq
# get openai api key and model from config
# from config import OPENAI_API_KEY, OPENAI_MODEL
from config import GROQ_API_KEY, GROQ_MODEL

# client = OpenAI(api_key=OPENAI_API_KEY)
# client = Groq(api_key=OPENAI_API_KEY)   # Initialize Groq client with API key from config.
client = Groq(api_key=GROQ_API_KEY)   # Initialize Groq client with API key from config, which will be used for making requests to the Groq API for various operations in the application, such as vector database interactions and other AI-related tasks.

def get_completion(prompt):
    response = client.chat.completions.create(
        # model=OPENAI_MODEL,
        model=GROQ_MODEL,   # Use the Groq model specified in the config for generating completions, which allows us to leverage the capabilities of the Groq API for our application's needs.
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content

def get_qa_answer(resume_text, job_description, user_question):
    pass