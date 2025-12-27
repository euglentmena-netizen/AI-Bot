from flask import Flask, render_template_string, send_file, jsonify
import os
from pathlib import Path

app = Flask(__name__)

# Get the current directory
BASE_DIR = Path(__file__).parent.absolute()

# Load HTML template
with open(os.path.join(BASE_DIR, 'index.html'), 'r') as f:
    html_template = f.read()

@app.route('/')
def index():
    """Serve the main HTML page"""
    return render_template_string(html_template)

@app.route('/download/docx')
def download_docx():
    """Download Word document"""
    try:
        file_path = os.path.join(BASE_DIR, 'Apple_Financial_Analysis_Report.docx')
        if os.path.exists(file_path):
            return send_file(
                file_path,
                as_attachment=True,
                download_name='Apple_Financial_Analysis_Report.docx',
                mimetype='application/vnd.openxmlformats-officedocument.wordprocessingml.document'
            )
        else:
            return jsonify({"error": "File not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/download/mp3')
def download_mp3():
    """Download MP3 audio"""
    try:
        file_path = os.path.join(BASE_DIR, 'Apple_Financial_Analysis_Report.mp3')
        if os.path.exists(file_path):
            return send_file(
                file_path,
                as_attachment=True,
                download_name='Apple_Financial_Analysis_Report.mp3',
                mimetype='audio/mpeg'
            )
        else:
            return jsonify({"error": "File not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/download/pdf')
def download_pdf():
    """Download PDF (original financial statements)"""
    try:
        file_path = os.path.join(BASE_DIR, 'FY25_Q2_Consolidated_Financial_Statements.pdf')
        if os.path.exists(file_path):
            return send_file(
                file_path,
                as_attachment=True,
                download_name='FY25_Q2_Consolidated_Financial_Statements.pdf',
                mimetype='application/pdf'
            )
        else:
            return jsonify({"error": "File not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/files-info')
def files_info():
    """Get information about available files"""
    files = {
        'docx': {
            'name': 'Apple_Financial_Analysis_Report.docx',
            'description': 'Professional Word document with complete analysis',
            'exists': os.path.exists(os.path.join(BASE_DIR, 'Apple_Financial_Analysis_Report.docx'))
        },
        'mp3': {
            'name': 'Apple_Financial_Analysis_Report.mp3',
            'description': 'Audio narration of the financial analysis',
            'exists': os.path.exists(os.path.join(BASE_DIR, 'Apple_Financial_Analysis_Report.mp3'))
        },
        'pdf': {
            'name': 'FY25_Q2_Consolidated_Financial_Statements.pdf',
            'description': 'Original financial statements',
            'exists': os.path.exists(os.path.join(BASE_DIR, 'FY25_Q2_Consolidated_Financial_Statements.pdf'))
        }
    }
    return jsonify(files)

if __name__ == '__main__':
    print("=" * 80)
    print("FINANCIAL ANALYSIS REPORT - WEB SERVER")
    print("=" * 80)
    print()
    print("🌐 Starting Flask web server...")
    print()
    print("📌 LOCAL ACCESS:")
    print("   🔗 http://localhost:8888")
    print()
    print("📌 TO SHARE WITH CLIENTS:")
    print("   1. Find your computer's IP address:")
    print("      - Mac/Linux: Open Terminal and run: ipconfig getifaddr en0")
    print("      - Then share: http://YOUR_IP_ADDRESS:8888")
    print()
    print("   2. Use ngrok for public link (install: pip install ngrok):")
    print("      - Run: ngrok http 8888")
    print("      - Share the generated public URL")
    print()
    print("   3. Deploy to cloud (Heroku, AWS, etc.) for permanent link")
    print()
    print("📥 AVAILABLE FILES:")
    print("   ✓ Word Document (.docx) - Complete analysis report")
    print("   ✓ Audio File (.mp3) - Narrated in English")
    print("   ✓ PDF - Original financial statements")
    print()
    print("=" * 80)
    print("Press Ctrl+C to stop the server")
    print("=" * 80)
    print()
    
    app.run(debug=True, host='0.0.0.0', port=8888)
