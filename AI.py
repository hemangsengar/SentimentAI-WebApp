from secret_settings import GOOGLE_API_KEY
import google.generativeai as genai




genai.configure(api_key=GOOGLE_API_KEY)

def generate_text(prompt):
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text
