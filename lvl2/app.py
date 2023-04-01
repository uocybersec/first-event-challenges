import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
    <form action="/find" method="POST">
        <label>Text:</label><br>
        <textarea type="text" name="textToSearch"></textarea><br><br>
        <label>Word(s) to find: <input type="text" name="textToFind"></label><br>
        <input type="submit" value="Submit">
    </form>
    '''

@app.route('/find', methods=['POST'])
def find():
    text = request.form['textToSearch']
    to_find = request.form['textToFind']


    linux_command = f'echo "{text}" | grep -i "{to_find}"' # create the linux command to find the specific word(s) in the text provided
    result = subprocess.run(linux_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True) # run the linux command on the server

    if result.returncode != 0: # if there was an error when the linux command was executed
        print(result.stderr)
        return 'Could not find the word you gave me!', 500
    
    return result.stdout.decode('utf-8') # return the output of the ran linux command

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
