# Placeholder for upcoming equation templates (y=mx+b, etc.)
from flask import Flask, render_template, request
 import google.generativeai as genai
 import os

 app = Flask(__name__)

 # Configure Google Gemini API
 GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
 if not GOOGLE_API_KEY:
     print("Warning: GOOGLE_API_KEY environment variable not set. Gemini functionality will not work.")

 genai.configure(api_key=GOOGLE_API_KEY)
 model = genai.GenerativeModel('gemini-pro')

 # Define a route for the home page (root URL "/")
 @app.route('/')
 def home():
  return render_template('website.html')

 # New route to handle the equation submission and prepare the prompt
 @app.route('/prepare_prompt', methods=['POST'])
 def prepare_prompt():
  equation = request.form.get('equation')

  if not equation:
   return render_template('website.html', error="Please enter an equation.")

  # Prepare the prompt for Gemini
  prepared_prompt = f"""
Generate Manim code to visualize the following mathematical equation:

{equation}

Please provide the Manim code as a complete Python script, including necessary imports.
Consider how to best represent this equation visually, potentially using graphs, animations, or other relevant Manim objects.
If the equation represents a function, consider showing its graph over a reasonable domain.
Add comments to explain the different parts of the Manim code.
"""

  # Render the template with the received equation and prepared prompt
  return render_template('website.html', received_equation=equation, prepared_prompt=prepared_prompt)

 # Check if the script is being run directly
 if __name__ == '__main__':
  app.run(debug=True)
