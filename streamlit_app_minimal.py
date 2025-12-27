import streamlit as st

# Page configuration - MUST be first
st.set_page_config(
    page_title="Apple Financial Analysis",
    page_icon="📊",
    layout="wide"
)

# ============ HEADER ============
st.title("📊 Apple Inc. Financial Analysis")
st.subheader("FY25 Q2 Consolidated Financial Statements")
st.caption("Comprehensive KPI Analysis & Investment Recommendations")
st.divider()

# ============ SIDEBAR NAVIGATION ============
with st.sidebar:
    st.header("📋 Navigation")
    page = st.radio(
        "Select Section:",
        [
            "📊 Overview",
            "📈 KPI Metrics",
            "💰 Financial Details",
            "✅ Strengths",
            "⚠️ Concerns",
            "🎯 Recommendations",
            "⚡ Risk Assessment",
            "📥 Downloads"
        ]
    )
    
    st.divider()
    st.markdown("**Report Details:**")
    st.caption("Company: Apple Inc.")
    st.caption("Period: FY25 Q2 (6M ended Mar 29, 2025)")
    st.caption("Date: December 27, 2025")

# ============ PAGE: OVERVIEW ============
if page == "📊 Overview":
    st.header("Executive Summary")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        Apple demonstrates **strong financial performance** in FY25 Q2:
        
        - 📈 **4.44% YoY Revenue Growth** - solid momentum
        - 💰 **Excellent Margins** - Gross 46.96%, Net 27.82%
        - 🎯 **Services Acceleration** - 12.77% growth
        - 💵 **Strong Balance Sheet** - $132.9B liquid assets
        - ⚡ **High Efficiency** - 113.07% ROE
        """)
    
    with col2:
        st.metric("Revenue Growth", "4.44%")
        st.metric("Net Income", "$61.1B")
        st.metric("Liquidity", "$132.9B")
    
    st.divider()
    st.success("✅ **RECOMMENDATION: BUY** - For long-term investors at reasonable valuations")

# ============ PAGE: KPI METRICS ============
elif page == "📈 KPI Metrics":
    st.header("Key Performance Indicators")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Revenue Growth", "4.44%", "Healthy")
        st.metric("Operating Margin", "32.97%", "Strong")
    
    with col2:
        st.metric("Gross Margin", "46.96%", "Excellent")
        st.metric("Net Margin", "27.82%", "Excellent")
    
    with col3:
        st.metric("ROE (Ann.)", "113.07%", "Strong")
        st.metric("Debt-to-Equity", "2.06x", "Moderate")

# ============ PAGE: FINANCIAL DETAILS ============
elif page == "💰 Financial Details":
    st.header("Detailed Financial Analysis")
    
    tab1, tab2, tab3 = st.tabs(["Income Statement", "Balance Sheet", "Returns"])
    
    with tab1:
        st.subheader("Income Statement (6-Month Period)")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Sales 2025", "$219.7B")
            st.metric("Sales 2024", "$210.3B")
        with col2:
            st.metric("Products", "$166.7B")
            st.metric("Services", "$53.0B")
        with col3:
            st.metric("Gross Profit", "$103.1B")
            st.metric("Operating Income", "$72.4B")
    
    with tab2:
        st.subheader("Balance Sheet")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Assets", "$331.2B")
            st.metric("Current Assets", "$118.7B")
            st.metric("Liquid Assets", "$132.9B")
        with col2:
            st.metric("Total Liabilities", "$223.1B")
            st.metric("Shareholders' Equity", "$108.1B")
            st.metric("Cash", "$28.2B")
    
    with tab3:
        st.subheader("Return Metrics")
        col1, col2 = st.columns(2)
        with col1:
            st.metric("ROA (Ann.)", "36.90%")
            st.metric("ROE (Ann.)", "113.07%")
        with col2:
            st.metric("R&D Ratio", "7.66%")
            st.metric("SG&A Ratio", "6.33%")

# ============ PAGE: STRENGTHS ============
elif page == "✅ Strengths":
    st.header("Key Strengths")
    
    strengths = [
        ("💪 Strong Growth", "4.44% YoY with services at 12.77%"),
        ("📈 Excellent Margins", "Gross 46.96%, Operating 32.97%, Net 27.82%"),
        ("💰 Strong Liquidity", "$132.9B in liquid assets"),
        ("⚡ Capital Efficiency", "ROE 113.07%, ROA 36.90%"),
        ("🎯 Diversification", "Services reducing hardware dependency"),
        ("🔧 Excellence", "Operating income +6.04% YoY, Net income +6.20%"),
    ]
    
    for title, desc in strengths:
        st.info(f"**{title}**\n{desc}")

# ============ PAGE: CONCERNS ============
elif page == "⚠️ Concerns":
    st.header("Areas of Concern")
    
    concerns = [
        ("📉 Product Growth Slowing", "Core products at only 2.04% growth"),
        ("📊 Declining Assets", "Down 9.25% from Sep 2024"),
        ("💳 Current Ratio < 1.0", "At 0.82x but manageable"),
        ("❓ Services Profitability", "Segment data not disclosed"),
    ]
    
    for title, desc in concerns:
        st.warning(f"**{title}**\n{desc}")

# ============ PAGE: RECOMMENDATIONS ============
elif page == "🎯 Recommendations":
    st.header("Investment Recommendations")
    
    st.success("✅ **BUY RECOMMENDATION** - For long-term investors")
    
    st.subheader("Action Items")
    actions = [
        "Compare P/E with S&P 500 (20-22x)",
        "Monitor product revenue trajectory",
        "Track services profitability",
        "Review quarterly guidance",
        "Analyze segment performance",
        "Assess macro headwinds",
        "Monitor regulatory risks",
        "Compare with competitors",
    ]
    for i, action in enumerate(actions, 1):
        st.markdown(f"{i}. {action}")
    
    st.subheader("Investment Thesis")
    thesis = {
        "Operational Excellence": "Margins expanding despite slower growth",
        "Diversification": "Services growth reduces hardware dependency",
        "Capital Efficiency": "113.07% ROE shows excellent deployment",
        "Financial Strength": "$132.9B supports operations and returns",
        "Competitive Moat": "Strong brand, ecosystem, customer loyalty",
    }
    for key, value in thesis.items():
        st.markdown(f"**{key}**: {value}")

# ============ PAGE: RISK ASSESSMENT ============
elif page == "⚡ Risk Assessment":
    st.header("Risk Assessment")
    
    st.warning("**Overall Risk: MODERATE**")
    
    risks = {
        "Product Maturity": "2.04% growth suggests potential saturation",
        "Economic Sensitivity": "Consumer discretionary spending risk",
        "Currency Risk": "Significant international presence",
        "Regulatory Risk": "Antitrust and App Store challenges",
        "Competition": "Intense from Samsung, Google, Amazon",
    }
    
    for risk, detail in risks.items():
        st.markdown(f"⚠️ **{risk}**: {detail}")

# ============ PAGE: DOWNLOADS ============
elif page == "📥 Downloads":
    st.header("Download Financial Reports")
    
    st.success("✅ All reports are ready!")
    
    st.info("""
    ### Available Documents:
    
    **1. Word Document** - Apple_Financial_Analysis_Report.docx
    - Professional formatted report
    - Complete KPI analysis
    - Investment recommendations
    - Risk assessment
    
    **2. Audio Report** - Apple_Financial_Analysis_Report.mp3
    - Full analysis narrated in English
    - 7+ minutes of content
    - Perfect for listening on-the-go
    
    **3. PDF** - FY25_Q2_Consolidated_Financial_Statements.pdf
    - Original financial statements
    - Complete balance sheet and income statement
    
    ### How to Access:
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.link_button(
            "📂 View Files on GitHub",
            "https://github.com/euglentmena-netizen/AI-Bot",
            use_container_width=True
        )
    with col2:
        st.link_button(
            "📥 Clone Repository",
            "https://github.com/euglentmena-netizen/AI-Bot.git",
            use_container_width=True
        )
    
    st.divider()
    st.markdown("""
    ### Direct File Access:
    ```bash
    git clone https://github.com/euglentmena-netizen/AI-Bot.git
    cd AI-Bot
    # All files are available in the repository
    ```
    """)

# ============ FOOTER ============
st.divider()
st.markdown("""
<div style="text-align: center; color: #666; font-size: 0.9em;">
    <p><strong>Apple Inc. Financial Analysis</strong></p>
    <p>Period: FY25 Q2 (6 months ended March 29, 2025)</p>
    <p>Repository: <a href="https://github.com/euglentmena-netizen/AI-Bot" target="_blank">GitHub - euglentmena-netizen/AI-Bot</a></p>
</div>
""", unsafe_allow_html=True)
