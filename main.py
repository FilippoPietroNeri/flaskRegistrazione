from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('homepage.html')


@app.route('/profile', methods=['POST'])
def registerData():
    nome = request.form['nome']
    cognome = request.form['cognome']
    datanascita = request.form['datanascita']
    nazione = request.form['nazione']
    username = request.form['username']
    password = request.form['password']
    passwordconfirm = request.form['password_confirm']
    email = request.form['email']
    lingua = request.form.getlist('lingua')
    consenso_informazione = request.form['consenso_informazione']
    print(consenso_informazione)
    if str(password) == str(passwordconfirm):
        return render_template('riepilogo.html', nome=nome, cognome=cognome, datanascita=datanascita, nazione=nazione, username=username, password=password, passwordconfirm=passwordconfirm, email=email, lingua=lingua, consenso_informazione=consenso_informazione)
    else:
        return render_template('errori.html', message="La password non è uguale in entrambi i campi, ricontrolla e riprova.")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)
