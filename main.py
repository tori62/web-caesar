from flask import Flask

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
    <!DOCTYPE html>
    <html>
        <head>
            <style>
                form {
                    background-color: #eee;
                    padding: 20px;
                    margin: 0 auto;
                    width: 540px;
                    font: 16px sans-serif;
                    broder-radius: 10px;
                }

                textarea{
                    margin: 10px 0;
                    width: 540px;
                    height: 120px;
                }
            </style>
        </head>
        <body>
            <form action="/secret-code" method=["POST"]
                <label for="rotate-by">
                    Rotate by:
                    <input type="text" name="rot" value=0>
                </lable>
                <br>
                <label>
                    <textarea name="textarea"></textarea>
                </label>
                <br>
                <input type="submit" name="Submit Query"/>
        </body>
    </html> """

@app.route("/secret-code", methods=['GET'])
def index():
    return form

app.run()

#@app.route("/secret-code", methods=['POST'])
#def index():
#    return form

app.run()