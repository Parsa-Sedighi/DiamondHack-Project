from flask import Flask, render_template
app = Flask(__name__)
# Define a route for the home page (root URL "/")
@app.route('/')
def home():
    # Render the HTML template located in the 'templates' folder
    # This will return the content of index.html
    return render_template('website.html')

# Check if the script is being run directly (and not imported as a module)
if __name__ == '__main__':
    # Start the Flask web server in debug mode (helps with automatic reloading and error messages)
    app.run(debug=True)
