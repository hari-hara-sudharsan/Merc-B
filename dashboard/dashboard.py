import streamlit as st
import plotly.express as px
import requests

st.set_page_config(page_title="AI Business Assistant", layout="wide")

st.title("📊 AI Business Intelligence Dashboard")

# --- Fetch report ---
user_id = st.number_input("Enter User ID", min_value=1)

if st.button("Load Report"):
    report = requests.get(f"http://localhost:8000/report/{user_id}").json()

    # --- Executive Summary ---
    st.subheader("Executive Summary")
    st.write(report["executive_summary"])

    # --- SWOT ---
    st.subheader("SWOT Analysis")
    st.text(report["swot"])

    # --- Trends ---
    st.subheader("Trends & Opportunities")
    trends = report["trends_and_opportunities"]["trends"]
    fig = px.line(y=list(range(len(trends))), x=trends, title="Trend Growth")
    st.plotly_chart(fig)

    # --- Competitors ---
    st.subheader("Competitors")
    for c in report["market_and_competitors"]["competitors"]:
        st.markdown(f"**{c['name']}** – {c['strength']}")

    # --- Challenges ---
    st.subheader("Key Challenges")
    for ch in report["challenges"]:
        with st.expander(ch["name"]):
            st.write(ch["insight"])
            st.success(ch["recommendation"])

    # --- Inspiration ---
    st.subheader("Inspiration Near You ❤️")
    for i in report["inspiration"]:
        st.info(f"**{i['name']}**\n\n{i['story']}\n\nLesson: {i['lesson']}")
