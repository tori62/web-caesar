from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>
    <html>
        <head>
            <style>
                form {{
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    broder-radius: 10px;
                }}

                textarea{{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }}
            </style>
        </head>
        <body>
            <form action="/" method="POST">
                <label for="rotate-by">
                    Rotate by:
                    <input type="text" name="rot" value=0>
                </lable>
                <br>
                <label>
                    <textarea name="text">{0}</textarea>
                </label>
                <br>
                <input type="submit" name="Submit Query"/>
            </form>
        </body>
    </html> 
"""

@app.route("/", methods=['GET'])
def index():
    return form.format('')

@app.route("/", methods=['POST'])
def encrypt():
    rotate = request.form['rot']
    rotate = int(rotate)
    text_input = request.form['text']
    response = rotate_string(text_input,rotate)
    return form.format(response)

app.run()
