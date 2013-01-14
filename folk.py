from flask import Flask, render_template, redirect

app = Flask(__name__)

app.jinja_env.add_extension('pyjade.ext.jinja.PyJadeExtension')

@app.route('/')
def index():
    return render_template('home.jade')

@app.route('/song')
def song_editor():
    return render_template('song.jade')

@app.route('/browse')
def browse():
    return render_template('browse.jade')

@app.route('/discuss')
def discuss():
    return render_template('discuss.jade')

if __name__ == '__main__':
    app.debug = True
    app.run()
