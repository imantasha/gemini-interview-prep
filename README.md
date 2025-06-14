# gemini-interview-prep
#  Gemini-Powered Interview Prep Tool

This is an AI-powered tool that helps job seekers prepare for interviews by generating:
-  3 job-specific interview questions
- 1 sample answer
-  1 practical success tip

Built using:
- Google Gemini (`gemini-1.5-flash`)
- Python
- Gradio
- dotenv

###  How to Run

```bash
git clone https://github.com/imantasha/gemini-interview-prep.git
cd gemini-interview-prep
pip install -r requirements.txt

Create a .env file with your Gemini API key:

GEMINI_API_KEY=your-key-here

Then run:

python app.py
