from flask import Flask, render_template, request, redirect, url_for
import os
app = Flask(__name__)
name = os.environ["NAME"]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form['data']
        with open('data/data.txt', 'a+') as f:
            f.write(data + '\n')
        return redirect(url_for("index")) 
    with open('data/data.txt', 'a+') as f:
        f.seek(0)
        data = f.read()
    return render_template('index.html', data=data, name=name)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")