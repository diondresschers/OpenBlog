Maak github repo met naam `openblog

$ mkdir `openblog`

$ python3 -m venv venv_openblog

$ PS1='\W $ '

$ source venv_openblog/bin/activate

)$ python3 -m pip install flask

)$ python3 -m pip freeze > requirements.txt

echo "# OpenBlog" >> README.md
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:diondresschers/OpenBlog.git
git push -u origin main

touch hello_world.py

Voeg toe aan `hello_world.py`

```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return('Hello World!')

if __name__ == '__main__':
    app.run(debug=True)
```

)$ flask run

)$ flask

)$ export FLASK_APP=hello_world.py

)$ flask run

)$ python3 -m pip install flask-sqlalchemy

