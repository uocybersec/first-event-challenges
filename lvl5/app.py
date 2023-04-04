from flask import Flask, request

app = Flask(__name__)


def encrypt(vault_code, key): # vault_code is a list of integers, and key is an integer
    encrypted_vault_code = []

    for digit in vault_code:
        enc_digit = digit * key
        encrypted_vault_code.append(enc_digit)

    return encrypted_vault_code


@app.route('/')
def index():
    with open('encrypted_code.txt', mode='r') as encrypted_code:
        return f'''
        <h1>Vault Lock</h1>
        <p>ENCRYPTED vault code:<p>
        <pre>{encrypted_code.read()}</pre><br>
        <form action="/attempt-unlock" method="POST">
            <label>Code (seperate each number by a single space): <input type="text" name="code"/></label><br>
            <label>Key: <input type="text" name="key"/></label><br>
            <input type="submit" value="[Unlock Vault]"/>
        </form>
        '''

@app.route('/attempt-unlock', methods=['POST'])
def unlock():
    with open('encrypted_code.txt', mode='r') as code:
        try:
            inputted_code = request.form['code']
            inputted_code = [int(c) for c in inputted_code.split(' ')] # convert the inputted code into a list of integers

            inputted_key = int(request.form['key'])
            if inputted_key < 2:
                return '<p>The key must be 2 or greater.</p>'

            code_to_match = code.readline()

            encrypted_inputted_code = encrypt(inputted_code, inputted_key)
            encrypted_inputted_code = ' '.join([str(c) for c in encrypted_inputted_code])

            if encrypted_inputted_code == code_to_match:
                with open('flag.txt', mode='r') as flag:
                    return f'<h1>[Vault Unlocked!]</h1><p>Here is the flag:</p><pre>{flag.read()}</pre>'
            else:
                return '<h1>The vault won\'t budge...</h1>'
        except:
            return '<p>Invalid inputs. Try again.</p>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
