from llm import run_llm

def generate_swot(user_data: dict) -> str:
    prompt = f"""
    You are a startup analyst.

    Generate a SWOT analysis for:
    Startup Idea: {user_data['idea']}
    Target Users: {user_data['target_users']}
    Region: {user_data['region']}

    Keep it concise and structured.
    """
    return run_llm(prompt)
