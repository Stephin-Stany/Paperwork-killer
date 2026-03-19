from dotenv import load_dotenv
import os

load_dotenv(".env")

print(os.getenv("OPENAI_API_KEY"))