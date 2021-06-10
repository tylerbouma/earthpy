from wtforms import Form, StringField, SelectField

class TranscriptSearchForm(Form):
    choices = [('title', 'title')]
    select = SelectField('Search for transcripts:', choices=choices)
    search = StringField('')