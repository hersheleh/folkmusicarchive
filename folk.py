from flask import Flask, render_template, redirect


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/song_editor')
def song_editor():
    return render_template('song_editor.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
