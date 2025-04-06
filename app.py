from flask import Flask, render_template, request, jsonify, send_from_directory
import os
import re
import subprocess
from ManimTest.manimations import manimCaller  # Adjusted import path to match new project folder structure
import google.generativeai as genai

app = Flask(__name__, static_folder='static') # Serve static files from 'static'
                                              # May need to be addressed as it doesn't do anything for now.

# Configure Google Gemini API
# /!\ Do NOT pass key through production!
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")
if not GOOGLE_API_KEY:
    print("Warning: GOOGLE_API_KEY environment variable not set.")
else:
    genai.configure(api_key=GOOGLE_API_KEY)
    model = genai.GenerativeModel('gemini-2.0-flash')

@app.route('/')
def index():
    return render_template('web.html')

@app.route('/process_equation', methods=['POST'])
def process_equation():
    equation = request.form.get('equation')
    if not equation:
        return render_template('web.html', error="Please enter an equation.")

    # --- Template Matching (Example for y = mx + b) ---
    linear_match = re.match(r'^y\s*=\s*(-?\d+(\.\d*)?)x\s*([+-]\s*(-?\d+(\.\d*)))?$', equation)
    if linear_match:
        try:
            m_str = linear_match.group(1)
            b_str_signed = linear_match.group(3)
            b_str_unsigned = linear_match.group(4)
            sign = 1
            if b_str_signed and '-' in b_str_signed:
                sign = -1
            b_str = b_str_unsigned if b_str_unsigned else "0"
            m = float(m_str)
            b = float(b_str) * sign

            # Call manimCaller for linear equation template
            output_video_path = os.path.join('manimations', 'media', 'videos', 'linearEqInstance.mp4') # Adjust as needed
            manimCaller.manimLinearEq("y", m, b)
            video_url = f"/static/videos/linearEqInstance.mp4" # Serve from static/videos
            return render_template('web.html', video_url=video_url)

        except Exception as e:
            return render_template('web.html', error=f"Error processing linear equation: {e}")

    # --- Gemini Processing (If there's no match to a predefined template) ---
    elif GOOGLE_API_KEY:
        prompt = f"""Generate a Manim video that describes the steps to solving the following mathematical equation: {equation}."""
        try:
            response = model.generate_content(prompt)
            gemini_output = response.text.strip()

            # Save Gemini's code
            gemini_file_path = os.path.join('manimations', 'Instances', 'generated_equation.py')
            with open(gemini_file_path, "w") as f:
                f.write(gemini_output)

            # Run Manim
            scene_name_match = re.search(r"class\s+(\w+)\s*\(\s*Scene\s*\)", gemini_output)
            scene_name = scene_name_match.group(1) if scene_name_match else "GeneratedScene"
            manim_output_path = os.path.join('manimations', 'media', 'videos', 'generated_equation.mp4') # Adjust
            manimCaller.run_manim_scene(gemini_file_path, scene_name, quality='pl') # You might want higher quality later
            video_url = f"/static/videos/generated_equation.mp4" # Serve from static/videos
            return render_template('web.html', video_url=video_url)

        except Exception as e:
            return render_template('web.html', error=f"Error with Gemini or Manim: {e}")

    else:
        return render_template('web.html', error="No template matched and Gemini API key is not configured.")

# Serve static videos (create a 'videos' folder inside 'static')
@app.route('/static/videos/<path:filename>')
def serve_static_video(filename):
    return send_from_directory(os.path.join('static', 'videos'), filename)

if __name__ == '__main__':
    app.run(debug=True)
