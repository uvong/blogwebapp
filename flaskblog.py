from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm  
app = Flask(__name__)

app.config['SECRET_KEY'] = '1104570453007afbe0960d9f562a001f'

posts = [
    {
        'author': 'Uyen Vong',
        'title': 'Blog Project Day 1',
        'content': 'Getting started with a very basic web app that routes to the home page and the about page.',
        'date_posted': 'June 19, 2021',
    },
    {
        'author': 'Uyen Vong',
        'title': 'Blog Project Day 2',
        'content': 'Created home, about, and layout HTML templates along with a main CSS static file.',
        'date_posted': 'June 20, 2021',
    }
]

@app.route("/")
@app.route("/home")
def home():
    #posts=posts will allow HTML files to reference dictionary dataset
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)