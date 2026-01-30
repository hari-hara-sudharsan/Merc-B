def build_report_schema(data, analysis, competitors, trends, inspiration):
    return {
        "meta": {
            "business_name": data["business_name"],
            "industry": data["industry"],
            "region": data["region"]
        },

        "executive_summary": analysis["summary"],

        "swot": analysis["swot"],

        "market_and_competitors": {
            "competitors": competitors,
            "insights": analysis["competitor_insights"]
        },

        "trends_and_opportunities": {
            "trends": trends,
            "profit_opportunities": analysis["opportunities"]
        },

        "challenges": [
            {
                "name": c,
                "insight": f"Impact analysis for {c}",
                "recommendation": f"Suggested strategy to handle {c}"
            }
            for c in data["challenges"]
        ],

        "inspiration": inspiration,

        "action_plan": analysis["action_plan"]
    }
