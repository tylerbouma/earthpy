from flask import Flask, request, jsonify, render_template
import markdown
import markdown.extensions.fenced_code
from visualisation import read_mongo
from forms import TranscriptSearchForm

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    search = TranscriptSearchForm(request.form)
    if request.method == 'POST':
        return search_results(search)
    return render_template('index.html', form=search)
    #df = read_mongo('BBCE', 'Transcriptions', 'Tigers')
    #return render_template('index.html', tables=[df.to_html(classes='data', index=False)])

@app.route('/results')
def search_results(search):
    results = []
    search_string = search.data['search']

    if search.data['search'] == '':
        qry = db_session.query(Title)
        results = query.all()

    if not results:
        flash('No results found!')
        return redirect('/')
    else:
        # display results
        return render_template('results.html', results=results)

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