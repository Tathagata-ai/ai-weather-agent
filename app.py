import streamlit as st
from main import weather_agent

# Page config
st.set_page_config(
    page_title="AI Weather Agent",
    page_icon="🌦",
    layout="centered"
)

# Custom styling (🔥 makes it look premium)
st.markdown("""
    <style>
    .main {
        background-color: #0f172a;
    }
    .title {
        font-size: 40px;
        font-weight: bold;
    }
    .subtitle {
        color: #94a3b8;
        margin-bottom: 20px;
    }
    .card {
        background-color: #1e293b;
        padding: 20px;
        border-radius: 12px;
        margin-top: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title">🌦 AI Weather Agent</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Get intelligent weather insights powered by AI 🤖</div>', unsafe_allow_html=True)

# Input
city = st.text_input("📍 Enter a city")

# Button
if st.button("🔍 Get Weather Report"):
    if city:
        with st.spinner("Fetching weather and analyzing with AI..."):
            result = weather_agent(city)

        st.success("✅ Done!")

        # 🔥 Premium card UI for result
        st.markdown("### 🤖 AI Weather Report")
        st.markdown(f"""
        <div class="card">
            {result}
        </div>
        """, unsafe_allow_html=True)

    else:
        st.warning("⚠️ Please enter a city")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using OpenAI API + Streamlit")