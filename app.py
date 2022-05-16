from flask import Flask, render_template
import utils


writers = utils.get_writers_list("static/writers.json")

app = Flask(__name__)
app.debug = True


@app.route('/')
def index():
    return render_template('index.html', writers=writers)


if __name__ == '__main__':
     app.run()

