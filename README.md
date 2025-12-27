# Apple Inc. Financial Analysis Report

## 📊 Overview

A comprehensive financial analysis of Apple Inc.'s FY25 Q2 Consolidated Financial Statements with detailed KPI metrics, investment recommendations, and risk assessment.

### Key Highlights

- **Revenue Growth**: 4.44% YoY
- **Gross Margin**: 46.96% (Excellent)
- **Operating Margin**: 32.97% (Strong)
- **Net Profit Margin**: 27.82% (Excellent)
- **ROE (Annualized)**: 113.07% (Strong)
- **Liquid Assets**: $132.9 Billion
- **Recommendation**: **BUY** for long-term investors

---

## 🚀 Live Demo

[View on Streamlit Cloud](#) *(After deployment)*

---

## 📋 Features

### 📈 Analysis Components
- ✅ Executive summary with financial highlights
- ✅ 6 key performance indicators (KPI) with detailed metrics
- ✅ Income statement analysis (6-month period comparison)
- ✅ Balance sheet metrics and liquidity analysis
- ✅ Return on assets (ROA) and return on equity (ROE)
- ✅ Operating efficiency ratios
- ✅ Comprehensive strengths assessment (6 points)
- ✅ Risk identification and concern areas (4 points)
- ✅ Investment recommendations and action items
- ✅ Risk assessment with moderate risk rating

### 📥 Available Formats
- 📄 **Word Document (.docx)** - Professional report (500 KB)
- 🎧 **Audio Narration (.mp3)** - Full report in English (7.02 MB)
- 📊 **PDF** - Original financial statements
- 🌐 **Web Dashboard** - Interactive Streamlit app
- 🌍 **Web Portal** - Flask HTML interface

---

## 🛠️ Technology Stack

- **Streamlit** - Interactive web app framework
- **Flask** - Lightweight web server
- **pandas** - Data analysis
- **pdfplumber** - PDF text extraction
- **python-docx** - Word document generation
- **gTTS** - Text-to-speech conversion
- **Python 3.10+**

---

## 📦 Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/apple-financial-analysis.git
cd apple-financial-analysis
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🎯 Usage

### Option 1: Run Streamlit App (Recommended)
```bash
streamlit run streamlit_app.py
```
The app will open at `http://localhost:8501`

### Option 2: Run Flask Server
```bash
python app.py
```
Access at `http://localhost:8888`

### Option 3: Generate Individual Reports
```bash
# Generate KPI analysis
python kpi_analysis.py

# Create Word document
python create_word_report.py

# Convert to MP3 audio
python convert_to_mp3.py

# Extract financial data from PDF
python financial_analysis.py
```

---

## 📂 Project Structure

```
apple-financial-analysis/
├── streamlit_app.py              # Main Streamlit application
├── app.py                        # Flask web server
├── kpi_analysis.py              # KPI calculation and analysis
├── create_word_report.py        # Word document generator
├── convert_to_mp3.py            # Text-to-speech converter
├── financial_analysis.py        # PDF data extraction
├── index.html                   # Web dashboard HTML
├── requirements.txt             # Python dependencies
├── README.md                    # This file
├── CLIENT_SHARING_GUIDE.md      # Client sharing instructions
├── .gitignore                   # Git ignore file
│
├── Apple_Financial_Analysis_Report.docx
├── Apple_Financial_Analysis_Report.mp3
├── FY25_Q2_Consolidated_Financial_Statements.pdf
│
└── .venv/                       # Virtual environment
```

---

## 📊 Key Metrics Summary

### Income Statement (6-Month Period)
| Metric | 2025 | 2024 | Growth |
|--------|------|------|--------|
| Total Net Sales | $219.7B | $210.3B | 4.44% |
| Gross Profit | $103.1B | $97.1B | 6.21% |
| Operating Income | $72.4B | $68.3B | 6.04% |
| Net Income | $61.1B | $57.6B | 6.20% |

### Balance Sheet (As of March 29, 2025)
| Item | Amount |
|------|--------|
| Total Assets | $331.2B |
| Current Assets | $118.7B |
| Liquid Assets | $132.9B |
| Total Liabilities | $223.1B |
| Shareholders' Equity | $108.1B |

---

## ✅ Strengths

1. **Strong Revenue Growth** - 4.44% YoY with services growing 12.77%
2. **Excellent Profitability** - Margins expanding across all metrics
3. **Solid Balance Sheet** - $132.9B in liquid assets
4. **Capital Efficiency** - ROE of 113.07%, ROA of 36.90%
5. **Business Diversification** - Services reducing hardware dependency
6. **Operational Excellence** - Consistent earnings growth YoY

---

## ⚠️ Areas of Concern

1. **Product Revenue Slowing** - Core product growth at only 2.04%
2. **Declining Total Assets** - Down 9.25% from Sep 2024
3. **Current Ratio Below 1.0** - Working capital management required
4. **Services Profitability Unclear** - Segment metrics not separately disclosed

---

## 🎯 Investment Recommendation

### **BUY** ✅

**For Long-Term Investors:**
- Strong fundamentals with industry-leading margins
- Consistent revenue and profitability growth
- Strategic diversification into services
- High return on equity and assets
- Ample cash for R&D and shareholder returns

**Risk Level: MODERATE**
- Monitor product revenue trajectory
- Watch for macroeconomic headwinds
- Track regulatory developments

---

## 🚀 Deployment

### Deploy to Streamlit Cloud

1. **Fork this repository to your GitHub**

2. **Sign up at [streamlit.io](https://streamlit.io)**

3. **Connect your GitHub repository**

4. **Deploy!**
   ```
   https://share.streamlit.io/yourusername/apple-financial-analysis/main/streamlit_app.py
   ```

### Deploy to Heroku

```bash
# Create Procfile
echo "web: streamlit run streamlit_app.py" > Procfile

# Deploy
heroku login
heroku create your-app-name
git push heroku main
```

---

## 📝 Files Generated

### Output Documents
- `Apple_Financial_Analysis_Report.docx` - Professional Word report
- `Apple_Financial_Analysis_Report.mp3` - Audio narration (7.02 MB)
- `FY25_Q2_Consolidated_Financial_Statements.pdf` - Source statements

### Python Scripts
- `streamlit_app.py` - Interactive Streamlit application
- `kpi_analysis.py` - Comprehensive KPI analysis
- `create_word_report.py` - Word document generation
- `convert_to_mp3.py` - Text-to-speech conversion
- `financial_analysis.py` - PDF data extraction
- `app.py` - Flask web server

---

## 🔄 Sharing with Clients

### Option 1: Streamlit Cloud
Share the public Streamlit Cloud URL

### Option 2: Local Network
Share your computer's IP with port number: `http://192.168.x.x:8888`

### Option 3: ngrok
Create a public tunnel:
```bash
pip install pyngrok
ngrok http 8888
# Share the generated URL
```

### Option 4: Download Files
Provide direct file downloads (DOCX, MP3, PDF)

---

## 📋 Requirements

- Python 3.10 or higher
- 200 MB disk space for dependencies
- Internet connection (for text-to-speech)
- Modern web browser (Chrome, Firefox, Safari, Edge)

---

## 🐛 Troubleshooting

### Streamlit Not Running
```bash
# Clear cache and reinstall
pip uninstall streamlit -y
pip install streamlit==1.31.1
streamlit run streamlit_app.py
```

### PDF Extraction Issues
- Ensure PDF file is in the same directory
- Check PDF is not encrypted
- Verify pdfplumber is installed: `pip install pdfplumber`

### MP3 Generation Fails
- Ensure internet connection (for Google Text-to-Speech)
- Check gTTS is installed: `pip install gtts`
- Try shorter text chunks if memory issues occur

### Port Already in Use
```bash
# For Flask (port 8888)
lsof -i :8888
kill -9 <PID>

# For Streamlit (port 8501)
lsof -i :8501
kill -9 <PID>
```

---

## 📚 Documentation

- [Streamlit Docs](https://docs.streamlit.io)
- [Flask Docs](https://flask.palletsprojects.com)
- [pandas Documentation](https://pandas.pydata.org)
- [pdfplumber Guide](https://github.com/jsvine/pdfplumber)

---

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Commit changes (`git commit -am 'Add improvement'`)
4. Push to branch (`git push origin feature/improvement`)
5. Create Pull Request

---

## 📄 License

This project is licensed under the MIT License - see LICENSE file for details.

---

## 👤 Author

Created for financial analysis and investment decision support.

**Contact**: For questions or feedback, open an issue on GitHub.

---

## 📞 Support

- 📧 Email: your.email@example.com
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/apple-financial-analysis/issues)
- 💬 Discussions: [GitHub Discussions](https://github.com/yourusername/apple-financial-analysis/discussions)

---

## ⭐ Show Your Support

If this project helped you, please consider:
- Giving it a star ⭐
- Sharing it with others
- Contributing improvements
- Providing feedback

---

**Last Updated**: December 27, 2025

**Financial Data Period**: FY25 Q2 (6 months ended March 29, 2025)

**Status**: ✅ Production Ready
