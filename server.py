import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Access the API key
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')

# Validate and set the API key
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY not found in the environment. Please check your .env file.")

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")  # Use the appropriate Gemini Pro model


def generate_bio(name, profession, skills, tone):
    try:
        # Generate the appropriate prompt based on tone
        if tone.lower() == "casual":
            prompt = (
                f"Hey there! Meet {name}, a talented {profession} who’s passionate about {skills}. "
                f"They’re all about making things happen and having fun along the way!"
            )
        elif tone.lower() == "professional":
            prompt = (
                f"Write a professional introduction for LinkedIn for {name}, "
                f"a {profession}, skilled in {skills}. Keep it concise and formal."
            )
        elif tone.lower() == "enthusiastic":
            prompt = (
                f"Write an enthusiastic and energetic 'About Me' section for {name}, "
                f"a {profession}, highlighting their expertise in {skills} with a motivational tone."
            )
        else:
            prompt = (
                f"Write a {tone.lower()} personal introduction for LinkedIn for {name}, "
                f"a {profession}, skilled in {skills}. Keep it concise and engaging."
            )

        # Call the generate_content method
        response = model.generate_content(prompt)
        
        # Return the generated text
        return response.text

    except Exception as e:
        return f"An error occurred: {e}"
