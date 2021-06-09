from flask import Flask, request, jsonify, render_template
import markdown
import markdown.extensions.fenced_code
from visualisation import read_mongo

app = Flask(__name__)

@app.route('/')
def index():
    df = read_mongo()
    return render_template('index.html', tables=[df.to_html(classes='data')], titles=df.columns.values)

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