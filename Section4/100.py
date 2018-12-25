# Web app that lets user submit a username and a password.
# The app checks if the username exists and the password satisfies conditions
# from ex.81

from flask import Flask, render_template_string, request


app = Flask(__name__)
html_string = """
                    <div class='form'>
                        <form action='/' method='POST'>
                            <input type='text' name='username' placeholder='Username'>
                            <br>
                            <input type='password' name='password' placeholder='Password'>
                            <br>
                            <button type='submit'>Submit</button>
                        </form>
                    </div>

"""


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        print(username)
        with open("users.txt", "r") as file:
            users = file.readlines()
            users = [user.strip("\n") for user in users]
            if username in users:
                return 'Username exists!'

        password = request.form['password']
        if any(char.isdigit() for char in password) and any(char.isupper() for char in password)\
        and len(password) >= 5:
            return 'Success!'

        if not any(char.isdigit() for char in password):
            return 'Password should contain at least one number!'
        if not any(char.isupper() for char in password):
            return 'Password should contain at least one uppercase!'
        if len(password) < 5:
            return 'Password should be at least 5 characters long!'

    else:
        return render_template_string(html_string)


if __name__ == '__main__':
    app.run(debug=True)
