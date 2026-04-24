import sys
from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)

# --- CONFIGURATION ---
# If your GitHub URL is https://<username>.github.io/<repo>/, 
# set this to '/<repo>'
app.config['FREEZER_BASE_URL'] = '/' 
app.config['FREEZER_DESTINATION'] = 'build'

# --- ROUTES ---
@app.route('/')
def home():
    # You can return raw HTML or use render_template if you have an index.html
    return """
    <html>
        <head>
            <title>My Python Site</title>
            <style>
                body { font-family: sans-serif; text-align: center; padding: 50px; }
                .card { border: 1px solid #ddd; padding: 20px; border-radius: 10px; }
            </style>
        </head>
        <body>
            <div class="card">
                <h1>Deployment Successful</h1>
                <p>This site was built with Python & Flask.</p>
                <small>Managed via GitHub Actions & Pages</small>
            </div>
        </body>
    </html>
    """

# --- MAIN EXECUTION ---
freezer = Freezer(app)

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        # Run 'python app.py build' to generate the static site
        print("Freezing the site into the /build folder...")
        freezer.freeze()
    else:
        # Run 'python app.py' to test locally
        print("Starting local development server...")
        app.run(debug=True)
