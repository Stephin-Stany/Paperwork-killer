import ollama

def extract_json(text):

    prompt = f"""
    Extract structured data from the text below.

    Return ONLY valid JSON.

    Fields:
    name
    passport_number
    date_of_birth
    country

    TEXT:
    {text}
    """

    response = ollama.chat(
        model='llama3',
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response['message']['content']