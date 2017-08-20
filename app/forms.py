from flask_wtf import FlaskForm
from wtforms import StringField, SelectMultipleField, widgets
from wtforms.validators import DataRequired

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()

class UserPreferences(FlaskForm):
    research_areas = [
            ('ML', 'Machine Learning'),
            ('OPT', 'Optimization'),
            ('GR', 'Graph Theory'),
            ('SC', 'Smart Cities'),
            ('BE', 'Bioethanol')]
    name = StringField('Nome', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    areas_of_interest = MultiCheckboxField('Áreas de interesse', validators=[DataRequired()], choices=research_areas)

