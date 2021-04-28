#import os
import flask
import json
from flask import Flask,request, jsonify
from flask import render_template
import pycep_correios


app = Flask(__name__)

@app.route('/')
@app.route('/index/')
def index():
    return render_template('index.html')

@app.route ('/Teste', methods=['POST'])
def teste():
    print('chamou')
    recebido = request.form['variavel4'] 
    teste = np.array([[request.form['variavel'],request.form['variavel2'],request.form['variavel3'],request.form['variavel4']]])
    classe = model.predict(teste)[0]
    

    
    return 'tudo ok'
 

@app.route('/zipcode/<zipcode>') # http://localhost:5000/zipcode/60050111
def validar_cep(zipcode):
    '''Função valida de número de cep junto ao site dos Correios.
        - Parâmetro: cep.
        - Retorna: json com as infomações:
            - Cep válidos: Logradouro/Nome; Bairro/Distrito; Localidade/UF; CEP.
            - Inválidos: msn: "Cep inválido"
    '''
    try:
        endereco = pycep_correios.get_address_from_cep(zipcode)
        #exemplo: http://localhost:5000/Cep/60050220
        res = endereco
        return json.dumps(res, ensure_ascii=False).encode('utf8')
        #return jsonify(endereco)#f'<h1>Cep {endereco}</h1>'
    except:
        res = f'zip code invalid.:{zipcode}.'
        return json.dumps(res, ensure_ascii=False).encode('utf8')
        #return jsonify(f'Cep inválido:{cep}.')

#teste localhost
'''if __name__ == '__main__':
    app.run(debug=True)'''

#teste heroku
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
