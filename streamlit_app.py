import streamlit as st
import os
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="Apple Inc. Financial Analysis",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding-top: 1rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin: 0.5rem 0;
    }
    .highlight-box {
        background-color: #e8f0ff;
        border-left: 4px solid #667eea;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .risk-box {
        background-color: #fff3cd;
        border-left: 4px solid #ff9800;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    .success-box {
        background-color: #d4edda;
        border-left: 4px solid #28a745;
        padding: 1rem;
        border-radius: 0.5rem;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Get base directory
BASE_DIR = Path(__file__).parent

# ============ HEADER ============
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.title("📊 Apple Inc. Financial Analysis")
    st.subheader("FY25 Q2 Consolidated Financial Statements")
    st.caption("Comprehensive KPI Analysis & Investment Recommendations")

st.markdown("---")

# ============ SIDEBAR ============
with st.sidebar:
    st.header("📋 Navigation")
    page = st.radio(
        "Select a section:",
        ["📊 Overview", "📈 KPI Metrics", "💰 Financial Details", 
         "✅ Strengths", "⚠️ Concerns", "🎯 Recommendations", 
         "⚡ Risk Assessment", "📥 Downloads"]
    )
    
    st.markdown("---")
    st.markdown("**Report Details:**")
    st.caption("Company: Apple Inc.")
    st.caption("Period: FY25 Q2 (6 months ended March 29, 2025)")
    st.caption("Generated: December 27, 2025")

# ============ PAGE 1: OVERVIEW ============
if page == "📊 Overview":
    st.header("Executive Summary")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("""
        Apple Inc. demonstrates **strong financial performance** in FY25 Q2 with:
        
        - **4.44% YoY revenue growth** - solid business momentum
        - **Excellent profitability margins** - gross margin 46.96%, net margin 27.82%
        - **Strategic diversification** - services growing at 12.77%
        - **Robust balance sheet** - $132.9B in liquid assets
        - **High capital efficiency** - ROE of 113.07%
        """)
    
    with col2:
        st.metric("Revenue Growth", "4.44%", "+9.32M")
        st.metric("Net Income", "$61.1B", "6-Month")
        st.metric("Liquid Assets", "$132.9B", "Cash + Securities")
    
    st.markdown("---")
    
    st.subheader("🎯 Investment Recommendation")
    st.markdown("""
    <div class="success-box">
        <h3 style="margin: 0; color: #155724;">✅ BUY</h3>
        <p style="margin: 0.5rem 0 0 0; color: #155724;">Strong fundamentals with healthy profit margins, consistent revenue growth, and strategic diversification into services. Recommended for long-term investors at reasonable valuations.</p>
    </div>
    """, unsafe_allow_html=True)

# ============ PAGE 2: KPI METRICS ============
elif page == "📈 KPI Metrics":
    st.header("Key Performance Indicators")
    
    # Create KPI cards
    col1, col2, col3 = st.columns(3)
    
    kpis = [
        ("Revenue Growth", "4.44%", "Healthy"),
        ("Gross Margin", "46.96%", "Excellent"),
        ("Operating Margin", "32.97%", "Strong"),
        ("Net Profit Margin", "27.82%", "Excellent"),
        ("ROE (Annualized)", "113.07%", "Strong"),
        ("Debt-to-Equity", "2.06x", "Moderate"),
    ]
    
    # Display metrics
    for idx, (label, value, rating) in enumerate(kpis):
        col = [col1, col2, col3][idx % 3]
        with col:
            st.metric(label, value, rating)
    
    st.markdown("---")
    
    # KPI Table
    st.subheader("KPI Summary Table")
    
    kpi_data = {
        "Metric": [kpi[0] for kpi in kpis],
        "Value": [kpi[1] for kpi in kpis],
        "Rating": [kpi[2] for kpi in kpis]
    }
    
    import pandas as pd
    df_kpi = pd.DataFrame(kpi_data)
    st.dataframe(df_kpi, use_container_width=True)

# ============ PAGE 3: FINANCIAL DETAILS ============
elif page == "💰 Financial Details":
    st.header("Detailed Financial Analysis")
    
    tab1, tab2, tab3 = st.tabs(["Income Statement", "Balance Sheet", "Returns & Efficiency"])
    
    with tab1:
        st.subheader("Income Statement Metrics (6-Month Period)")
        st.caption("March 29, 2025 vs March 30, 2024")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Net Sales 2025", "$219.7B")
            st.metric("Total Net Sales 2024", "$210.3B")
            st.metric("Revenue Growth", "4.44%")
        
        with col2:
            st.metric("Product Revenue", "$166.7B")
            st.metric("Services Revenue", "$53.0B")
            st.metric("Product Growth", "2.04%")
        
        with col3:
            st.metric("Services Growth", "12.77%")
            st.metric("Gross Profit", "$103.1B")
            st.metric("Operating Income", "$72.4B")
        
        st.markdown("---")
        st.metric("Net Income (6M 2025)", "$61.1B", "+6.20% YoY")
    
    with tab2:
        st.subheader("Balance Sheet Metrics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.write("**Assets:**")
            st.metric("Total Assets", "$331.2B")
            st.metric("Current Assets", "$118.7B")
            st.metric("Liquid Assets", "$132.9B")
            st.metric("Cash & Equivalents", "$28.2B")
        
        with col2:
            st.write("**Liabilities & Equity:**")
            st.metric("Total Liabilities", "$223.1B")
            st.metric("Current Liabilities", "$144.6B")
            st.metric("Shareholders' Equity", "$108.1B")
            st.metric("Debt-to-Equity", "2.06x")
    
    with tab3:
        st.subheader("Return & Efficiency Metrics")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric("Return on Assets (ROA)", "36.90%", "Annualized")
            st.metric("Return on Equity (ROE)", "113.07%", "Annualized")
        
        with col2:
            st.metric("Asset Turnover", "0.66x")
            st.metric("R&D Expense Ratio", "7.66%")
            st.metric("SG&A Expense Ratio", "6.33%")

# ============ PAGE 4: STRENGTHS ============
elif page == "✅ Strengths":
    st.header("Key Strengths")
    
    strengths = [
        ("💪 Strong Revenue Growth", "4.44% YoY growth with services accelerating at 12.77%, demonstrating successful business diversification."),
        ("📈 Excellent Profitability", "Gross margin 46.96%, Operating margin 32.97%, Net margin 27.82% - all industry-leading with expansion YoY."),
        ("💰 Solid Balance Sheet", "$132.9B in liquid assets provides flexibility for R&D, dividends, and strategic investments."),
        ("⚡ Capital Efficiency", "ROE of 113.07% and ROA of 36.90% demonstrate exceptional shareholder value creation."),
        ("🎯 Business Diversification", "Services revenue at 12.77% growth provides earnings diversity and reduces hardware dependency."),
        ("🔧 Operational Excellence", "Operating income up 6.04% YoY, net income up 6.20%, showing consistent earnings growth."),
    ]
    
    for title, description in strengths:
        st.markdown(f"""
        <div class="success-box">
            <h4 style="margin: 0;">{title}</h4>
            <p style="margin: 0.5rem 0 0 0;">{description}</p>
        </div>
        """, unsafe_allow_html=True)

# ============ PAGE 5: CONCERNS ============
elif page == "⚠️ Concerns":
    st.header("Areas of Concern")
    
    concerns = [
        ("📉 Product Revenue Slowing", "Core product revenue growth at 2.04% suggests potential market saturation in hardware."),
        ("📊 Declining Total Assets", "Assets down 9.25% from Sep 2024 to Mar 2025, likely from capital redeployment."),
        ("💳 Current Ratio Below 1.0", "Current ratio of 0.82x indicates current liabilities exceed assets, though manageable with strong liquidity."),
        ("❓ Services Profitability Unclear", "While services growing at 12.77%, segment profitability not separately disclosed."),
    ]
    
    for title, description in concerns:
        st.markdown(f"""
        <div class="risk-box">
            <h4 style="margin: 0;">{title}</h4>
            <p style="margin: 0.5rem 0 0 0;">{description}</p>
        </div>
        """, unsafe_allow_html=True)

# ============ PAGE 6: RECOMMENDATIONS ============
elif page == "🎯 Recommendations":
    st.header("Investment Recommendations")
    
    st.markdown(f"""
    <div class="success-box">
        <h3 style="margin: 0; color: #155724;">✅ RECOMMENDATION: BUY</h3>
        <p style="margin: 0.5rem 0 0 0; color: #155724;">For long-term investors seeking quality, profitability, and growth with moderate risk.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.subheader("Action Items")
    
    actions = [
        "Compare P/E ratio with S&P 500 average (~20-22x) and industry peers",
        "Review Apple's latest quarterly guidance and management commentary",
        "Analyze segment performance (iPhone, Mac, Services, Wearables) separately",
        "Monitor product revenue trajectory for stabilization",
        "Track capital allocation (dividends, buybacks, R&D spending)",
        "Assess macroeconomic indicators for consumer spending impacts",
        "Monitor regulatory developments (antitrust, App Store)",
        "Compare margins with key competitors",
    ]
    
    for i, action in enumerate(actions, 1):
        st.write(f"{i}. {action}")
    
    st.markdown("---")
    
    st.subheader("Investment Thesis")
    
    thesis_points = {
        "Operational Excellence": "Expanding margins despite slower growth",
        "Business Diversification": "Services at 12.77% growth reduces hardware dependency",
        "Capital Efficiency": "ROE 113.07% shows exceptional capital deployment",
        "Financial Strength": "$132.9B liquid assets supports operations & returns",
        "Competitive Moat": "Strong brand, loyal customer base, ecosystem lock-in",
    }
    
    for key, value in thesis_points.items():
        st.write(f"**{key}**: {value}")

# ============ PAGE 7: RISK ASSESSMENT ============
elif page == "⚡ Risk Assessment":
    st.header("Risk Assessment")
    
    st.markdown(f"""
    <div class="risk-box">
        <h3 style="margin: 0;">Overall Risk Level: MODERATE</h3>
        <p style="margin: 0.5rem 0 0 0;">Apple demonstrates strong fundamentals but faces macro headwinds and market maturity risks.</p>
    </div>
    """, unsafe_allow_html=True)
    
    risk_factors = {
        "Product Market Maturity": "Product growth at 2.04% suggests potential saturation",
        "Macroeconomic Sensitivity": "Consumer discretionary spending vulnerable to downturns",
        "Currency Risk": "Significant international revenue exposure",
        "Regulatory Risk": "Antitrust investigations and App Store policy challenges",
        "Competitive Pressure": "Intense competition from Samsung, Google, Amazon, etc.",
    }
    
    for risk, detail in risk_factors.items():
        st.warning(f"**{risk}**: {detail}")

# ============ PAGE 8: DOWNLOADS ============
elif page == "📥 Downloads":
    st.header("Download Financial Analysis Reports")
    
    st.info("🎉 All files are ready to download and share with clients!")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.subheader("📄 Word Document")
        st.write("Professional report with complete analysis, KPIs, strengths, concerns, and recommendations.")
        
        docx_path = BASE_DIR / "Apple_Financial_Analysis_Report.docx"
        if docx_path.exists():
            with open(docx_path, "rb") as file:
                st.download_button(
                    label="Download DOCX",
                    data=file,
                    file_name="Apple_Financial_Analysis_Report.docx",
                    mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
                    key="docx_download"
                )
            st.success(f"✓ Ready ({os.path.getsize(docx_path) / (1024*1024):.2f} MB)")
        else:
            st.error("File not found")
    
    with col2:
        st.subheader("🎧 Audio Report")
        st.write("Complete financial analysis narrated in English. Listen while commuting!")
        
        mp3_path = BASE_DIR / "Apple_Financial_Analysis_Report.mp3"
        if mp3_path.exists():
            with open(mp3_path, "rb") as file:
                st.download_button(
                    label="Download MP3",
                    data=file,
                    file_name="Apple_Financial_Analysis_Report.mp3",
                    mime="audio/mpeg",
                    key="mp3_download"
                )
            st.success(f"✓ Ready ({os.path.getsize(mp3_path) / (1024*1024):.2f} MB)")
        else:
            st.error("File not found")
    
    with col3:
        st.subheader("📊 Original PDF")
        st.write("FY25 Q2 Consolidated Financial Statements with source data.")
        
        pdf_path = BASE_DIR / "FY25_Q2_Consolidated_Financial_Statements.pdf"
        if pdf_path.exists():
            with open(pdf_path, "rb") as file:
                st.download_button(
                    label="Download PDF",
                    data=file,
                    file_name="FY25_Q2_Consolidated_Financial_Statements.pdf",
                    mime="application/pdf",
                    key="pdf_download"
                )
            st.success(f"✓ Ready")
        else:
            st.error("File not found")

# ============ FOOTER ============
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #666;">
    <p><strong>Apple Inc. Financial Analysis Report</strong></p>
    <p>Period: FY25 Q2 (6 months ended March 29, 2025)</p>
    <p>Source: FY25 Q2 Consolidated Financial Statements | Generated: December 27, 2025</p>
</div>
""", unsafe_allow_html=True)
