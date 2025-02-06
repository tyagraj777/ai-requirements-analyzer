import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def analyze_requirements(requirements_text):
    """Uses GPT-4 to analyze requirements and suggest improvements."""
    prompt = f"""
    You are an AI expert in software requirement analysis. Given the following project requirements:

    {requirements_text}

    Identify missing details, vague statements, and contradictions. Suggest improvements and clarify ambiguous parts.
    Also, generate user stories based on the requirements.
    """
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response["choices"][0]["message"]["content"]
