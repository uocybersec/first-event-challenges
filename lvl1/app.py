import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <h1>VSauce Quotes</h1>
    <p>You can choose from 3 text files which contain VSauce quotes.</p>
    <p>quote1.txt, quote2.txt, and quote3.txt</p>
    <form action="/read" method="POST">
        <label>Quote file to read: <input type="text" name="quote"/></label><br>
        <input type="submit" value="Read quote"/>
    </form>
    '''

@app.route('/read', methods=['POST'])
def read():
    selected_quote = request.form['quote']

    linux_command = f'cat quotes/{selected_quote}' # create the linux command to find the specific word(s) in the text provided
    result = subprocess.run(linux_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) # run the linux command on the server

    if result.returncode != 0: # if there was an error when the linux command was executed
        return result.stderr, 500
    
    return result.stdout.decode('utf-8') # return the output of the ran linux command

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
