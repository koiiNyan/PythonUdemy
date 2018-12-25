# Program that asks the user to submit a text through a web app.

from flask import Flask, render_template_string, request

app = Flask(__name__)
html_string = """
                    <div class='form'>
                        <form action='/' method='POST'>
                            <input type='text' name='text' placeholder='Enter text here'>
                            <br>
                            <button type='submit'>Submit</button>
                        </form>
                    </div>

"""


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        with open('user_text_flask.txt', 'a') as file:
            file.write(text + '\n')

        return render_template_string(html_string)

    else:
        return render_template_string(html_string)


if __name__ == '__main__':
    app.run(debug=True)
