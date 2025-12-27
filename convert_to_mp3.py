from docx import Document
from gtts import gTTS
import os

print("=" * 80)
print("CONVERTING WORD DOCUMENT TO MP3 AUDIO")
print("=" * 80)
print()

# Load the Word document
doc_path = 'Apple_Financial_Analysis_Report.docx'
print(f"Loading document: {doc_path}")
doc = Document(doc_path)

# Extract all text from the document
print("Extracting text from document...")
full_text = ""
for para in doc.paragraphs:
    if para.text.strip():  # Only include non-empty paragraphs
        full_text += para.text + " "

# Clean up the text
full_text = full_text.replace('\n', ' ').replace('  ', ' ')

print(f"Total characters extracted: {len(full_text)}")
print()

# Convert text to speech
print("Converting text to speech (MP3)...")
print("Language: English (US)")
print()

try:
    # Create gTTS object with slow=False for faster playback
    tts = gTTS(text=full_text, lang='en', slow=False)
    
    # Save as MP3
    output_file = 'Apple_Financial_Analysis_Report.mp3'
    tts.save(output_file)
    
    print(f"✅ Successfully created: {output_file}")
    print()
    
    # Get file size
    file_size_mb = os.path.getsize(output_file) / (1024 * 1024)
    print(f"File size: {file_size_mb:.2f} MB")
    print()
    print("=" * 80)
    print("CONVERSION COMPLETE!")
    print("=" * 80)
    print(f"\nYour audio file is ready: {output_file}")
    print("You can play this file with any media player that supports MP3 format.")
    
except Exception as e:
    print(f"❌ Error converting to MP3: {e}")
    print("\nTroubleshooting: Make sure you have internet connection for Google Text-to-Speech")
