from flask import Flask, request, jsonify, render_template
import markdown
import markdown.extensions.fenced_code

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    # display the contents of the README
    readme_file = open("README.md", "r")
    md_template_string = markdown.markdown(
        readme_file.read(), extensions=["fenced_code"]
    )

    return render_template('about.html') + md_template_string

# import declared routes - needs to be after the app page
import api

if __name__ == "__main__":
    app.run()