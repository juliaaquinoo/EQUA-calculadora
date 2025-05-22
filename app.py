from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)
CORS(app) 
@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    expressao = data.get('expressao', '')
    try:
        expressao = expressao.replace('×', '*').replace('÷', '/')
        resultado = eval(expressao)
        return jsonify({'resultado': str(resultado)})
    except:
        return jsonify({'resultado': 'Erro'})
if __name__ == '__main__':
    app.run(debug=True)
