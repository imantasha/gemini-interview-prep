import os
import gradio as gr
from dotenv import load_dotenv
import google.generativeai as genai

# Load your Gemini API key from .env
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

# Configure Gemini with your API key
genai.configure(api_key=api_key)

# Use the Gemini 1.5 Flash model (fast & free)
model = genai.GenerativeModel("gemini-2.0-flash")

# Main function to generate interview prep
def generate_interview_prep(role):
    prompt = f"""
You are a Google-level interviewer preparing candidates for the job role: {role}.

Please provide:
1. Three real-world interview questions for this role
2. One sample answer
3. One practical interview tip

Respond clearly and in numbered format.
"""
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f" Error: {e}"

# Gradio UI
demo = gr.Interface(
    fn=generate_interview_prep,
    inputs=gr.Textbox(label="Enter Job Role", placeholder="e.g., Prompt Engineer"),
    outputs=gr.Textbox(label="AI Interview Prep"),
    title=" Gemini-Powered Interview Prep",
    description="Enter a job title to receive 3 questions, a sample answer, and one practical tip.",
    article=" Made with ❤️ by Mantasha Idrisi • GitHub: [imantasha](https://github.com/imantasha) • Portfolio: [imantasha.github.io](https://imantasha.github.io)"
)

# Launch the app
if __name__ == "__main__":
    demo.launch()
