from langgraph.graph import StateGraph
from chains import (
    generate_swot, 
    generate_summary, 
    generate_competitor_insights, 
    generate_opportunities, 
    generate_action_plan
)
from mock_data import mock_competitors, mock_trends
from report_schema import build_report_schema
from db import save_report

def build_report(state: dict):
    # Generate analysis using LLM
    analysis = {
        "summary": generate_summary(state),
        "swot": generate_swot(state),
        "competitor_insights": generate_competitor_insights(state),
        "opportunities": generate_opportunities(state),
        "action_plan": generate_action_plan(state)
    }

    # Fetch other data
    competitors = mock_competitors()
    trends = mock_trends()
    
    # Prepare data for schema (handling missing keys from OnboardingInput)
    schema_data = {
        "business_name": state.get("idea", "My Startup"), # Use idea as fallback name
        "industry": state.get("idea", "General Interest"),
        "region": state.get("region", "Kerala"),
        "challenges": [
            "Customer Acquisition",
            "Funding",
            "Operational Efficiency",
            "Regulatory Compliance"
        ]
    }

    inspiration = "Success is not final, failure is not fatal: it is the courage to continue that counts."

    # Construct structured report
    report = build_report_schema(
        data=schema_data,
        analysis=analysis,
        competitors=competitors,
        trends=trends,
        inspiration=inspiration
    )

    save_report(state["user_id"], report)
    return report

graph = StateGraph(dict)
graph.add_node("generate_report", build_report)
graph.set_entry_point("generate_report")

onboarding_graph = graph.compile()
