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

def generate_summary(user_data: dict) -> str:
    prompt = f"""
    You are a startup analyst.

    Write a concise 1-sentence executive summary for:
    Startup Idea: {user_data['idea']}
    Target Users: {user_data['target_users']}
    Region: {user_data['region']}
    """
    return run_llm(prompt).strip()

def generate_competitor_insights(user_data: dict) -> str:
    prompt = f"""
    You are a market researcher.

    Provide a concise insight (1 sentence) about competitors for:
    Industry/Idea: {user_data['idea']}
    Region: {user_data['region']}

    Focus on what they might be lacking.
    """
    return run_llm(prompt).strip()

def generate_opportunities(user_data: dict) -> str:
    prompt = f"""
    You are a business strategist.

    Identify one key growth opportunity (1 sentence) for:
    Startup Idea: {user_data['idea']}
    Region: {user_data['region']}
    """
    return run_llm(prompt).strip()

def generate_action_plan(user_data: dict) -> list:
    prompt = f"""
    You are a startup mentor.

    List 3 specific, actionable steps for this startup:
    Startup Idea: {user_data['idea']}
    Region: {user_data['region']}

    Format: return ONLY the steps, separated by newlines. No numbering.
    """
    response = run_llm(prompt)
    steps = [line.strip() for line in response.split('\n') if line.strip()]
    return steps[:3]  # Ensure at most 3 steps
