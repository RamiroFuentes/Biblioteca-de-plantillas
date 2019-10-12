from flask import Flask
from flask import render_template

app = Flask(__name__ )

@app.route('/')
def notFound():
    title = "Team"
    return render_template('/index.html',title=title)

if __name__ == '__main__':
    app.run(debug=True,port=5000)