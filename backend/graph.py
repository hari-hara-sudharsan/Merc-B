from langgraph.graph import StateGraph
from chains import generate_swot
from mock_data import mock_competitors, mock_trends
from scraper import fetch_business_news
from db import save_report

def build_report(state: dict):
    report = {
        "swot": generate_swot(state),
        "competitors": mock_competitors(),
        "trends": mock_trends(),
        "news": fetch_business_news(),
        "challenges": [
            "Funding",
            "Talent acquisition",
            "Scaling",
            "Regulatory compliance",
            "Marketing reach",
            "Customer retention",
            "Tech debt",
            "Competition"
        ]
    }

    save_report(state["user_id"], report)
    return report

graph = StateGraph(dict)
graph.add_node("generate_report", build_report)
graph.set_entry_point("generate_report")

onboarding_graph = graph.compile()
