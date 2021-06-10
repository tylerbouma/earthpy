from wtforms import Form, StringField, SelectField

class TranscriptSearchForm(Form):
    choices = [('Title', 'Title'),
               ('Text', 'Text')]
    select = SelectField('Search for transcripts:', choices=choices)
    search = StringField('')