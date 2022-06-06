from flask import Flask, render_template, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import SubmitField, StringField, EmailField, TextAreaField
from wtforms.validators import DataRequired, Email


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')


app = Flask(__name__)
app.config['SECRET_KEY']  = '0376d95da44eb531d87de1a5f9c07775'
bootstrap = Bootstrap(app)


@app.route('/', methods=['POST', 'GET'])
def home():
    form = ContactForm()
    if form.validate_on_submit():
        flash('Message Received', 'info')
        return redirect(url_for('home'))
    return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)