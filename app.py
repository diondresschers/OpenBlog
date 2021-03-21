from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request # To be able to request data via a form.
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # To suppress warnings in the CLI like "/home/dion/git/py/flask/OpenBlog/venv_openblog/lib/python3.7/site-packages/ADeprecationWarning: SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and will be disabled by default in the future.  Set it to True or False to suppress this warning.   'SQLALCHEMY_TRACK_MODIFICATIONS adds significant overhead and '
db = SQLAlchemy(app)
migrate = Migrate(app, db) # This prevents the error `KeyError: 'migrate` when starting `flask db init`

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)

@app.route('/')
def home():
    pagename = 'home'
    posts = BlogPost.query.all()
    return render_template('index.html', pagename=pagename, posts=posts)

@app.route('/about')
def about():
    pagename = 'about'
    return render_template('about.html', pagename=pagename)

@app.route('/contact')
def contact():
    pagename = 'contact'
    return render_template('contact.html', pagename=pagename)

@app.route('/post/<int:post_id>')
def post(post_id): # You also need to include the post_id here.
    pagename = 'pagename'
    post = BlogPost.query.filter_by(id=post_id).one()

    # date_posted = post.date_posted.strftime('%B, %d, %Y')
    return render_template('post.html', pagename=pagename, post=post, )

@app.route('/add_post')
def add_post():
    pagename = 'add post'
    return render_template('add_post.html', pagename=pagename)

@app.route('/submit_post', methods=["POST"])
def submit_post():
    title = request.form['title'] # Deze `request` is boven geimporteerd
    subtitle = request.form['subtitle']
    author = request.form['author']
    content = request.form['content']

    post = BlogPost(title=title, subtitle=subtitle, author=author, content=content, date_posted=datetime.now())
    db.session.add(post) # Voeg de data toe aan de database.
    db.session.commit() # Voer de wijzigingen door.

    return redirect(url_for('home'))    

if __name__ == '__main__':
    app.run(debug=True)



