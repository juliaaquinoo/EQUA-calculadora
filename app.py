from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/calcular', methods=['POST'])
def calcular():
    data = request.get_json()
    expressao = data.get('expressao', '')

    try:
        # Corrigir divisão e operadores visuais para Python
        expressao = expressao.replace('÷', '/').replace('×', '*').replace('%', '/100')
        resultado = eval(expressao)
        return jsonify({'resultado': str(resultado)})
    except Exception as e:
        return jsonify({'resultado': 'Erro'})

if __name__ == '__main__':
    app.run(debug=True)
