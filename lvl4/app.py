from flask import Flask, request
from codecs import encode

app = Flask(__name__)

# on url / the following HTML is rendered
@app.route('/')
def login():
    return '''
        <form action="/attempt-login" method="POST">
            <label>Username: <input type="text" name="username"></label><br>
            <label>Password: <input type="password" name="password"></label><br>
            <input type="submit" value="Login">
        </form>
    '''

# when a request to the url /attempt-login is sent, check if the inputted username and password are valid. 
@app.route('/attempt-login', methods=['POST'])
def login_submit():
    username = request.form['username']
    password = request.form['password']

    password = encode(password, 'rot_13') # encodes the password in ROT13: https://en.wikipedia.org/wiki/ROT13

    if username == "geegee" and password == "supersecretpassword": # if the login is successful, give the user the flag.
        with open('flag.txt', mode='r') as flag:
            flag_value = flag.read()
            return f'''
                <div style="font-family: arial;">
                    <h1 style="color: green;">ACCESS GRANTED!</h1>
                    <p>Here is the flag:</p>
                    <pre>{flag_value}</pre>
                </div>
            '''
    else: # if the login is not successful, return "ACCESS DENIED"
        return "<h1 style='font-family: arial; color: red;'>ACCESS DENIED</h1>" 

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
