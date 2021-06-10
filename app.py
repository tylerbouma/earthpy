from flask import Flask, request, jsonify, render_template, flash, redirect
import markdown
import markdown.extensions.fenced_code
from visualisation import read_mongo
from forms import TranscriptSearchForm
import config

app = Flask(__name__)
app.secret_key = config.SECRET_KEY

@app.route('/', methods=['GET', 'POST'])
def index():
    search = TranscriptSearchForm(request.form)
    print(search)
    if request.method == 'POST':
        return search_results(search)
    return render_template('index.html', form=search)
    #df = read_mongo('BBCE', 'Transcriptions', 'Tigers')
    #

@app.route('/results')
def search_results(search):
    search_string = search.data['search']
    df = read_mongo('BBCE', 'Transcripts', str(search_string))

    if search.data['search'] == '':
        # returns dataframe with first 10 lines of the database
        # df = read_mongo('BBCE', 'Transcripts')
        return render_template('results.html', tables=[df.to_html(classes='data', index=False)])
    if df.empty:
        flash('No results found!')
        return redirect('/')
    else:
        # df = read_mongo('BBCE', 'Transcripts', search_string)
        # display results
        return render_template('results.html', tables=[df.to_html(classes='data', index=False)])

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